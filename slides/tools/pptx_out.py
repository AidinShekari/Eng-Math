"""Write a deck as PowerPoint: slides/EngineeringMath-slider-<lang>.pptx

* titles, text, captions: editable text boxes (Tahoma for Persian, Calibri for English);
* formulas: editable PowerPoint equations (OMML, converted from the LaTeX by pandoc), each with a
  picture of the same formula as the fallback that applications without equation support show;
  a formula pandoc cannot convert is the picture alone;
* figures and tables: pictures rendered from the TikZ / LaTeX of the notes;
* every step: an entrance "Fade" (0.25 s) starting On Click; the pieces of one step start
  With Previous, so one click shows the whole step;
* every chapter is a PowerPoint section.
"""
import html
import re
import subprocess
import uuid
import zipfile
from pathlib import Path

import fitz  # pymupdf
from lxml import etree
from pptx import Presentation
from pptx.util import Emu

import layout as L

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"
WORK = SLIDES / "build"

NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
NS_MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
NS_A14 = "http://schemas.microsoft.com/office/drawing/2010/main"
NS_P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
NSDECL = f'xmlns:a="{NS_A}" xmlns:p="{NS_P}" xmlns:r="{NS_R}"'

PT = 12700  # EMU per point

COL = dict(bar="CFE2F3", bar2="EEF5FB", barline="9DBEDF", title="1E2A4A", foot="7A7F93", ink="1E1F3B",
           muted="6B6B85")
BOXCOL = {"def": ("E3F1FB", "2E6DA4"), "thm": ("E8F6DE", "3F7F2A"), "imp": ("FFF6C7", "A07800"),
          "ex": ("EAF4FB", "1F6FA8"), "exe": ("FCEFDF", "B5650F"), "rem": ("FDEBDD", "C0572A"),
          "prf": ("F3F3F8", "5A5C7A")}


def emu(v):
    return int(round(v * PT))


def esc(s):
    return html.escape(s, quote=False)


def lighten(hexc, f):
    r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
    return "%02X%02X%02X" % tuple(int(c + (255 - c) * f) for c in (r, g, b))


# ============================================================ TeX text -> runs
def tex_runs(tex, bold=False, italic=False):
    """[('t', text, bold, italic) | ('m', latex) | ('br',)]"""
    out = []
    i = 0
    buf = []

    def flush():
        if buf:
            out.append(("t", "".join(buf), bold, italic))
            buf.clear()
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)\*?|\\(.)", tex[i:])
            name = m.group(1) or m.group(2)
            j = i + m.end()
            if name == "EMim":
                flush()
                from texparse import balanced
                body, j = balanced(tex, j)
                out.append(("m", body))
                i = j
                continue
            if name in ("textbf", "textit", "emph", "lr", "rl", "texttt", "textsf", "mbox", "text", "textrm",
                        "EMlatin", "EMfarsiin"):
                from texparse import balanced
                while j < len(tex) and tex[j] == " ":
                    j += 1
                if j < len(tex) and tex[j] == "{":
                    body, j = balanced(tex, j)
                    flush()
                    out.extend(tex_runs(body, bold or name == "textbf", italic or name in ("textit", "emph")))
                    i = j
                    continue
            simple = {"EMcheck": "✓", "dots": "…", "ldots": "…", "textbullet": "•", "quad": "  ", "qquad": "   ",
                      ",": " ", " ": " ", "%": "%", "&": "&", "_": "_", "#": "#", "$": "$", "{": "{", "}": "}",
                      "textbar": "|", "-": ""}
            if name == "\\":
                flush()
                out.append(("br",))
                i = j
                continue
            if name in simple:
                buf.append(simple[name])
                i = j
                if name.isalpha():
                    # a control word swallows the following space only when followed by text
                    pass
                continue
            # unknown command: drop it, keep a braced argument
            i = j
            continue
        if c in "{}":
            i += 1
            continue
        if c == "~":
            buf.append("\u00a0")
            i += 1
            continue
        if tex.startswith("---", i):
            buf.append("—")
            i += 3
            continue
        if tex.startswith("--", i):
            buf.append("–")
            i += 2
            continue
        if tex.startswith("``", i):
            buf.append("“")
            i += 2
            continue
        if tex.startswith("''", i):
            buf.append("”")
            i += 2
            continue
        if c == "\n":
            buf.append(" ")
            i += 1
            continue
        buf.append(c)
        i += 1
    flush()
    # collapse spaces
    res = []
    for r in out:
        if r[0] == "t":
            t = re.sub(r"[ \t]+", " ", r[1])
            res.append(("t", t, r[2], r[3]))
        else:
            res.append(r)
    if res and res[0][0] == "t":
        res[0] = ("t", res[0][1].lstrip(), res[0][2], res[0][3])
    if res and res[-1][0] == "t":
        res[-1] = ("t", res[-1][1].rstrip(), res[-1][2], res[-1][3])
    return [r for r in res if not (r[0] == "t" and r[1] == "")]


def plain_title(tex):
    """A title as plain text (formulas in titles are short: their symbols are kept)."""
    out = []
    for r in tex_runs(tex):
        if r[0] == "t":
            out.append(r[1])
        elif r[0] == "m":
            m = r[1]
            m = re.sub(r"\\operatorname\{(\w+)\}", r"\1", m)
            m = m.replace(r"\pi", "π").replace(r"\infty", "∞").replace(r"\,", "")
            m = re.sub(r"\\[A-Za-z]+", "", m).replace("{", "").replace("}", "")
            out.append(m)
    return "".join(out)


# ============================================================ OMML
MACROS_FA = r"""\newcommand{\EMt}[1]{\text{#1}}\newcommand{\EMtx}[2]{\text{#2}}\newcommand{\EMcheck}{\checkmark}
\newcommand{\EMbr}{}"""
MACROS_EN = r"""\newcommand{\EMt}[1]{\text{#1}}\newcommand{\EMtx}[2]{\text{#1}}\newcommand{\EMcheck}{\checkmark}
\newcommand{\EMbr}{}"""


def omml_batch(formulas, lang):
    """{latex: <m:oMath ...> xml string | None}"""
    formulas = sorted(set(formulas))
    out = {}
    if not formulas:
        return out
    cache = WORK / f"omml-{lang}.json"
    import json
    old = json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else {}
    todo = [f for f in formulas if f not in old and not re.search(r"[\u0600-\u06FF]", f)]
    if todo:
        src = (MACROS_FA if lang == "fa" else MACROS_EN) + "\n\n" + "\n\n".join(
            "MARK%d \\(%s\\)" % (k, f.replace("\\tfrac", "\\frac")) for k, f in enumerate(todo))
        (WORK / "omml.tex").write_text(src, encoding="utf-8")
        r = subprocess.run(["pandoc", "-f", "latex", "-t", "docx", "-o", str(WORK / "omml.docx"),
                            str(WORK / "omml.tex")], capture_output=True, text=True)
        xml = zipfile.ZipFile(WORK / "omml.docx").read("word/document.xml")
        doc = etree.fromstring(xml)
        W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        for p in doc.iter("{%s}p" % W):
            texts = "".join(t.text or "" for t in p.iter("{%s}t" % W))
            m = re.search(r"MARK(\d+)", texts)
            if not m:
                continue
            k = int(m.group(1))
            maths = list(p.iter("{%s}oMath" % NS_M))
            rest = re.sub(r"MARK\d+", "", texts).strip()
            if len(maths) == 1 and not rest:
                old[todo[k]] = etree.tostring(maths[0], encoding="unicode")
            else:
                old[todo[k]] = None
        for f in todo:
            old.setdefault(f, None)
        cache.write_text(json.dumps(old, ensure_ascii=False), encoding="utf-8")
    for f in formulas:
        # Persian words inside a formula: PowerPoint equations do not shape them right to left,
        # so such a formula is kept as its picture
        out[f] = None if re.search(r"[\u0600-\u06FF]", f) else old.get(f)
    return out


def omml_runs_fix(xml, size, lang):
    """Give every math run the PowerPoint run properties (Cambria Math, the size)."""
    root = etree.fromstring(xml)
    for r in root.iter("{%s}r" % NS_M):
        rpr = r.find("{%s}rPr" % NS_M)
        sty = None
        nor = False
        if rpr is not None:
            s = rpr.find("{%s}sty" % NS_M)
            sty = s.get("{%s}val" % NS_M) if s is not None else None
            nor = rpr.find("{%s}nor" % NS_M) is not None
        t = r.find("{%s}t" % NS_M)
        txt = t.text if t is not None and t.text else ""
        is_fa = bool(re.search(r"[\u0600-\u06FF]", txt))
        face = ("Tahoma" if lang == "fa" else "Calibri") if (nor and is_fa) or (nor and txt.strip() and txt.isalpha() and len(txt) > 3) else "Cambria Math"
        ital = "0" if (sty in ("p", "b") or nor) else "1"
        a = etree.Element("{%s}rPr" % NS_A, nsmap={"a": NS_A})
        a.set("lang", "fa-IR" if is_fa else "en-US")
        a.set("sz", str(int(size * 100)))
        a.set("i", ital)
        if sty == "b":
            a.set("b", "1")
        fill = etree.SubElement(a, "{%s}solidFill" % NS_A)
        etree.SubElement(fill, "{%s}srgbClr" % NS_A).set("val", COL["ink"])
        etree.SubElement(a, "{%s}latin" % NS_A).set("typeface", face)
        etree.SubElement(a, "{%s}cs" % NS_A).set("typeface", face)
        idx = 1 if rpr is not None else 0
        r.insert(idx, a)
        # a function name (sin, cos, ln ...) set as a plain run: keep a thin space after it
        if sty == "p" and t is not None and txt in FUNCS and r.getnext() is not None:
            t.text = txt + "\u2006"
    return etree.tostring(root, encoding="unicode")


FUNCS = {"sin", "cos", "tan", "cot", "sec", "csc", "sinh", "cosh", "tanh", "coth", "ln", "log", "exp", "arg",
         "Re", "Im", "Si", "Res", "arcsin", "arccos", "arctan", "arccot", "arcsinh", "arccosh", "Ln", "Arg", "erf",
         "lim", "max", "min", "sup", "inf", "det"}


# ============================================================ XML builders
class SlideXML:
    def __init__(self, slide, lang):
        self.slide = slide
        self.lang = lang
        self.rtl = lang == "fa"
        self.font = "Tahoma" if self.rtl else "Calibri"
        self.tree = slide.shapes._spTree
        self.next_id = 2 + len(self.tree.xpath("./p:sp|./p:pic"))
        self.anim = {}  # step -> [ids]

    def nid(self):
        self.next_id += 1
        return self.next_id

    def add(self, xml, step=None, sid=None):
        el = etree.fromstring(xml)
        self.tree.append(el)
        if step is not None and step > 0:
            self.anim.setdefault(step, []).append(sid)

    def rpr(self, size, bold=False, italic=False, color=None, latin=False):
        color = color or COL["ink"]
        lang = "fa-IR" if self.rtl and not latin else "en-US"
        return ('<a:rPr lang="%s" sz="%d"%s%s dirty="0"><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
                '<a:latin typeface="%s"/><a:cs typeface="Tahoma"/></a:rPr>') % (
            lang, int(size * 100), ' b="1"' if bold else "", ' i="1"' if italic else "", color, self.font)

    def para_xml(self, runs, size, align, color=None, omml=None, bold_all=False):
        """One <a:p>; omml: {latex: xml} for inline formulas (None -> plain text of the formula)."""
        algn = {"r": "r", "l": "l", "c": "ctr"}[align]
        parts = ['<a:p><a:pPr algn="%s" rtl="%d"/>' % (algn, 1 if self.rtl else 0)]
        for r in runs:
            if r[0] == "t":
                latin = not re.search(r"[\u0600-\u06FF]", r[1])
                parts.append("<a:r>%s<a:t>%s</a:t></a:r>" % (self.rpr(size, r[2] or bold_all, r[3], color, latin), esc(r[1])))
            elif r[0] == "br":
                parts.append("<a:br>%s</a:br>" % self.rpr(size, color=color))
            else:
                x = omml.get(r[1]) if omml else None
                if x:
                    parts.append('<a14:m xmlns:a14="%s">%s</a14:m>' % (NS_A14, omml_runs_fix(x, size, self.lang)))
                else:
                    parts.append("<a:r>%s<a:t>%s</a:t></a:r>" % (self.rpr(size, italic=True, color=color, latin=True), esc(plain_title("\\EMim{" + r[1] + "}"))))
        parts.append('<a:endParaRPr lang="%s" sz="%d" dirty="0"/></a:p>' % ("fa-IR" if self.rtl else "en-US", int(size * 100)))
        return "".join(parts)

    def sp_text(self, sid, x, y, w, h, paras_xml, name="Text", anchor="t", fill=None, line=None, ins=0, geom="rect"):
        fillx = '<a:solidFill><a:srgbClr val="%s"/></a:solidFill>' % fill if fill else "<a:noFill/>"
        linex = ('<a:ln w="%d"><a:solidFill><a:srgbClr val="%s"/></a:solidFill></a:ln>' % (line[1], line[0])) if line else "<a:ln><a:noFill/></a:ln>"
        return ('<p:sp %s><p:nvSpPr><p:cNvPr id="%d" name="%s %d"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
                '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="%s"><a:avLst/></a:prstGeom>%s%s</p:spPr>'
                '<p:txBody><a:bodyPr wrap="square" lIns="%d" tIns="%d" rIns="%d" bIns="%d" rtlCol="0" anchor="%s"><a:noAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody></p:sp>') % (
            NSDECL, sid, name, sid, emu(x), emu(y), emu(w), emu(max(h, 1)), geom, fillx, linex,
            emu(ins), emu(ins), emu(ins), emu(ins), anchor, paras_xml)

    def pic(self, sid, x, y, w, h, rid, name="Picture"):
        return ('<p:pic %s><p:nvPicPr><p:cNvPr id="%d" name="%s %d"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
                '<p:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
                '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>') % (
            NSDECL, sid, name, sid, rid, emu(x), emu(y), emu(w), emu(h))

    def alt(self, choice_xml, fallback_xml):
        return ('<mc:AlternateContent xmlns:mc="%s"><mc:Choice xmlns:a14="%s" Requires="a14">%s</mc:Choice>'
                '<mc:Fallback>%s</mc:Fallback></mc:AlternateContent>') % (NS_MC, NS_A14, choice_xml, fallback_xml)

    def rect(self, sid, x, y, w, h, fill, line=None, name="Shape", grad=None, round_=False):
        if grad:
            fillx = ('<a:gradFill rotWithShape="1"><a:gsLst><a:gs pos="0"><a:srgbClr val="%s"/></a:gs><a:gs pos="100000"><a:srgbClr val="%s"/></a:gs></a:gsLst>'
                     '<a:lin ang="%d" scaled="0"/></a:gradFill>') % (grad[0], grad[1], grad[2])
        else:
            fillx = '<a:solidFill><a:srgbClr val="%s"/></a:solidFill>' % fill
        linex = ('<a:ln w="%d"><a:solidFill><a:srgbClr val="%s"/></a:solidFill></a:ln>' % (line[1], line[0])) if line else "<a:ln><a:noFill/></a:ln>"
        geom = "roundRect" if round_ else "rect"
        av = '<a:avLst><a:gd name="adj" fmla="val 8000"/></a:avLst>' if round_ else "<a:avLst/>"
        return ('<p:sp %s><p:nvSpPr><p:cNvPr id="%d" name="%s %d"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
                '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="%s">%s</a:prstGeom>%s%s</p:spPr>'
                '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>') % (
            NSDECL, sid, name, sid, emu(x), emu(y), emu(w), emu(h), geom, av, fillx, linex)

    def timing(self):
        if not self.anim:
            return
        ids = iter(range(3, 100000))
        pars = []
        bld = []
        for step in sorted(self.anim):
            effs = []
            for k, sid in enumerate(self.anim[step]):
                node = "clickEffect" if k == 0 else "withEffect"
                effs.append(
                    '<p:par><p:cTn id="%d" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="%s">'
                    '<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                    '<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
                    '<p:tgtEl><p:spTgt spid="%d"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
                    '<p:to><p:strVal val="visible"/></p:to></p:set>'
                    '<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="%d" dur="250"/><p:tgtEl><p:spTgt spid="%d"/></p:tgtEl></p:cBhvr></p:animEffect>'
                    '</p:childTnLst></p:cTn></p:par>' % (next(ids), node, next(ids), sid, next(ids), sid))
                bld.append('<p:bldP spid="%d" grpId="0" animBg="1"/>' % sid)
            pars.append('<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
                        '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>%s</p:childTnLst></p:cTn></p:par>'
                        '</p:childTnLst></p:cTn></p:par>' % (next(ids), next(ids), "".join(effs)))
        xml = ('<p:timing %s><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
               '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>%s</p:childTnLst></p:cTn>'
               '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
               '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
               '</p:childTnLst></p:cTn></p:par></p:tnLst><p:bldLst>%s</p:bldLst></p:timing>') % (NSDECL, "".join(pars), "".join(bld))
        el = etree.fromstring(xml)
        sld = self.slide._element
        # p:timing goes after p:clrMapOvr (or p:cSld)
        anchor = sld.find("{%s}clrMapOvr" % NS_P)
        if anchor is None:
            anchor = sld.find("{%s}cSld" % NS_P)
        anchor.addnext(el)


# ============================================================ images
class Images:
    def __init__(self, deck):
        self.doc = fitz.open(str(deck.pdf))
        self.pages = deck.pages
        self.dir = WORK / ("img-" + deck.lang)
        self.dir.mkdir(parents=True, exist_ok=True)

    def png(self, jid, zoom=3.0):
        f = self.dir / (jid + ".png")
        if not f.exists():
            pg = self.doc[self.pages[jid]]
            pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
            pix.save(str(f))
        return f


def rid_for(slide, path):
    _, rid = slide.part.get_or_add_image_part(str(path))
    return rid


# ============================================================ slides
def write(deck):
    lang = deck.lang
    rtl = lang == "fa"
    S = deck.sizes
    imgs = Images(deck)
    # formulas
    formulas = set()
    for s in deck.slides:
        for it in s.get("items", []):
            e = it["el"]
            if it["kind"] in ("para", "item", "cap"):
                formulas.update(r[1] for r in tex_runs(e.tex) if r[0] == "m")
            elif it["kind"] == "disp":
                for ln in it["lines"]:
                    formulas.add(" ".join(e.segs[k] for k in ln))
        for b in s.get("boxes", []):
            lab, t = b["box"].head
            formulas.update(r[1] for r in tex_runs(t) if r[0] == "m")
    omml = omml_batch(formulas, lang)
    failed = [f for f, x in omml.items() if not x]
    deck.omml_failed = failed

    prs = Presentation()
    prs.slide_width = Emu(emu(L.SW))
    prs.slide_height = Emu(emu(L.SH))
    blank = prs.slide_layouts[6]
    font = "Tahoma" if rtl else "Calibri"
    algn = "r" if rtl else "l"
    chap_title = {ch.num: ch.title for ch in deck.chapters}
    stats = dict(eq=0, eqpic=0, textmath=0)

    for si, s in enumerate(deck.slides):
        sl = prs.slides.add_slide(blank)
        X = SlideXML(sl, lang)
        kind = s["kind"]
        # ---- title bar (every slide but the cover) ----
        if kind != "cover":
            title = plain_title(s["title"]) + ((" " + L.LABELS[lang]["cont"]) if s.get("cont") else "")
            tw = deck.title_w.get(s["title"] + ((" " + L.LABELS[lang]["cont"]) if s.get("cont") else ""))
            size = L.TITLE
            if tw and tw > L.BAR["w"] - 36:
                size = max(14, int(L.TITLE * (L.BAR["w"] - 36) / tw))
            sid = X.nid()
            X.add(X.rect(sid, L.BAR["x"], L.BAR["y"], L.BAR["w"], L.BAR["h"], None, line=(COL["barline"], 10160),
                         name="Title bar", grad=(COL["bar"], COL["bar2"], 10800000 if rtl else 0), round_=True))
            sid = X.nid()
            p = X.para_xml([("t", title, True, False)], size, algn, color=COL["title"])
            X.add(X.sp_text(sid, L.BAR["x"] + 16, L.BAR["y"], L.BAR["w"] - 32, L.BAR["h"], p, name="Title", anchor="ctr"))
            # footer
            if s.get("chapter") not in (None, "front"):
                foot = L.LABELS[lang]["chapter"] + " " + L.num(lang, str(s["chapter"])) + " • " + plain_title(chap_title[s["chapter"]])
            else:
                foot = "ریاضی مهندسی" if rtl else "Engineering Mathematics"
            sid = X.nid()
            X.add(X.sp_text(sid, L.CX0, 512, 700, 16, X.para_xml([("t", foot, False, False)], 10, algn, color=COL["foot"]),
                            name="Footer") if not rtl else
                  X.sp_text(sid, L.CX1 - 700, 512, 700, 16, X.para_xml([("t", foot, False, False)], 10, algn, color=COL["foot"]), name="Footer"))
            sid = X.nid()
            numtxt = L.num(lang, str(si + 1))
            X.add(X.sp_text(sid, (L.CX0 if rtl else L.CX1 - 60), 512, 60, 16,
                            X.para_xml([("t", numtxt, False, False)], 10, "l" if rtl else "r", color=COL["foot"]), name="Slide number"))
        if kind == "cover":
            course, sub, other, other_sub = s["cover"]
            logo = ROOT / "template" / "ferdowsi-logo.png"
            rid = rid_for(sl, logo)
            from PIL import Image
            iw, ih = Image.open(logo).size
            h = 78
            w = iw * h / ih
            X.add(X.pic(X.nid(), (L.SW - w) / 2, 41, w, h, rid, "Logo"))
            X.add(X.rect(X.nid(), 160, 167, 640, 190, "D6E6F5", line=(COL["barline"], 10160), round_=True, name="Cover box"))
            sid = X.nid()
            paras = (X.para_xml([("t", course, True, False)], 40, "c", color=COL["title"]) +
                     X.para_xml([("t", plain_title(sub).replace("\\", ""), False, False)], 20, "c", color="2E6DA4") +
                     X.para_xml([("t", other, False, False)], 18, "c", color=COL["muted"]))
            X.add(X.sp_text(sid, 170, 177, 620, 170, paras, name="Course", anchor="ctr"))
            who = ("استاد: عباس ابراهیمی مقدم   •   جمع‌آوری و تنظیم: آیدین شکاری" if rtl else
                   "Instructor: Abbas Ebrahimi Moghadam   •   Compiled by: Aidin Shekari")
            uni = "دانشگاه فردوسی مشهد" if rtl else "Ferdowsi University of Mashhad"
            X.add(X.sp_text(X.nid(), 100, 396, 760, 60, X.para_xml([("t", who, False, False)], 16, "c") +
                            X.para_xml([("t", uni, False, False)], 14, "c", color=COL["muted"]), name="Authors"))
        elif kind == "part":
            numeral, ptitle, first, rng = s["part"]
            X.add(X.rect(X.nid(), 220, 165, 520, 170, "D6E6F5", line=(COL["barline"], 10160), round_=True, name="Part box"))
            X.add(X.sp_text(X.nid(), 230, 175, 500, 150,
                            X.para_xml([("t", s["title"], True, False)], 30, "c", color="3F7F2A") +
                            X.para_xml([("t", ptitle, False, False)], 24, "c", color="2E6DA4"), name="Part", anchor="ctr"))
        elif kind == "chapter":
            ch = s["ch"]
            paras = X.para_xml([("t", L.LABELS[lang]["contents"], True, False)], 20, algn, color="2E6DA4")
            for t in ch.sections:
                paras += X.para_xml([("t", "•  " + plain_title(t), False, False)], 18, algn)
            X.add(X.sp_text(X.nid(), L.CX0, L.CY0, L.CW, L.CY1 - L.CY0, paras, name="Contents"))
        elif kind == "content":
            write_content(X, s, deck, imgs, omml, stats)
        X.timing()
    # sections
    add_sections(prs, deck)
    out = SLIDES / f"EngineeringMath-slider-{lang}.pptx"
    prs.save(str(out))
    print(f"  wrote {out.name}: {len(deck.slides)} slides; equations {stats['eq']} (as pictures only: {stats['eqpic']}); "
          f"OMML failures {len(failed)}; text with formulas {stats['textmath']} (as pictures: {stats.get('textpic', 0)})")


def write_content(X, s, deck, imgs, omml, stats):
    lang = deck.lang
    rtl = lang == "fa"
    algn = "r" if rtl else "l"
    sc_all = s.get("shrink", 1.0)
    # boxes first (behind)
    for b in s["boxes"]:
        light, dark = BOXCOL[b["box"].kind]
        x, w = b["x"], b["w"]
        y0, y1 = b["y0"], b["y1"]
        st = b["step"]
        sid = X.nid()
        X.add(X.rect(sid, x, y0, w, y1 - y0, light, line=(lighten(dark, 0.65), 7620), name="Box"), st, sid)
        sid = X.nid()
        bx = x + w - L.BOXBAR if rtl else x
        X.add(X.rect(sid, bx, y0, L.BOXBAR, y1 - y0, dark, name="Box bar"), st, sid)
        if b["head"]:
            hd = b["head"]
            lab, t = b["box"].head
            runs = [("t", lab, True, False)] + ([("t", "  |  ", False, False)] + tex_runs(t) if t else [])
            hx = x + L.BOXPAD_X + (0 if rtl else L.BOXBAR)
            sid = X.nid()
            p = X.para_xml(runs, L.HEAD, algn, color=dark, omml=omml)
            X.add(X.sp_text(sid, hx, hd["y"], hd["w"], hd["h"], p, name="Box heading"), st, sid)
    for it in s["items"]:
        e = it["el"]
        st = it["step"]
        k = it["kind"]
        if k in ("para", "item", "cap"):
            size = L.CAPTION if k == "cap" else L.BODY
            size = size * (it.get("scale_all", 1.0))
            runs = tex_runs(e.tex)
            x, y, w = it["x"], it["y"], it["w"]
            al = "c" if k == "cap" else algn
            color = COL["muted"] if k == "cap" else None
            if k == "item":
                mark = (L.num(lang, str(e.index)) + ".") if e.ordered else "•"
                bxx = x + w if rtl else x - L.LIST_IND
                sid = X.nid()
                X.add(X.sp_text(sid, bxx, y, L.LIST_IND, 24, X.para_xml([("t", mark, False, False)], size, "c", color="2E6DA4"),
                                name="Bullet"), st, sid)
            hp = deck.sizes[it["jid"]]["hp"] * it.get("scale_all", 1.0)
            has_math = any(r[0] == "m" for r in runs)
            sid = X.nid()
            choice = X.sp_text(sid, x, y, w, it["h"], X.para_xml(runs, size, al, color=color, omml=omml))
            if has_math:
                stats["textmath"] += 1
                rid = rid_for(X.slide, imgs.png(it["jid"]))
                pic = X.pic(sid, x, y, w, hp, rid, "Text (picture)")
                if all(omml.get(r[1]) for r in runs if r[0] == "m"):
                    X.add(X.alt(choice, pic), st, sid)
                else:
                    # a formula of this paragraph has no equation form: the paragraph as a picture
                    stats["textpic"] = stats.get("textpic", 0) + 1
                    X.add(pic, st, sid)
            else:
                X.add(choice, st, sid)
        elif k == "disp":
            lines = [" ".join(e.segs[j] for j in ln) for ln in it["lines"]]
            stats["eq"] += 1
            scale = it.get("scale", 1.0) * it.get("scale_all", 1.0)
            nw, nh = it["nat"]
            nw *= it.get("scale_all", 1.0)
            nh *= it.get("scale_all", 1.0)
            x, y, w = it["x"], it["y"], it["w"]
            px = x + (w - nw) / 2
            sid = X.nid()
            rid = rid_for(X.slide, imgs.png(it["jid"]))
            picxml = X.pic(sid, px, y, nw, nh, rid, "Equation (picture)")
            if all(omml.get(ln) for ln in lines):
                paras = []
                for ln in lines:
                    m = omml_runs_fix(omml[ln], L.BODY * scale, lang)
                    m = m.replace("<m:oMath", "<m:oMathPara><m:oMathParaPr><m:jc m:val=\"centerGroup\"/></m:oMathParaPr><m:oMath", 1) if False else m
                    paras.append('<a:p><a:pPr algn="ctr" rtl="0"/><a14:m xmlns:a14="%s"><m:oMathPara xmlns:m="%s"><m:oMathParaPr><m:jc m:val="centerGroup"/></m:oMathParaPr>%s</m:oMathPara></a14:m>'
                                 '<a:endParaRPr lang="en-US" sz="%d" dirty="0"/></a:p>' % (NS_A14, NS_M, m, int(L.BODY * scale * 100)))
                choice = X.sp_text(sid, x, y, w, it["h"], "".join(paras), name="Equation")
                X.add(X.alt(choice, picxml), st, sid)
            else:
                stats["eqpic"] += 1
                X.add(picxml, st, sid)
        elif k == "fig":
            f = imgs.png(e.jid + "_fig", zoom=4.0)
            rid = rid_for(X.slide, f)
            sid = X.nid()
            X.add(X.pic(sid, it["x"], it["y"], it["w"], it["h"], rid, "Figure"), st, sid)
        elif k == "table":
            f = imgs.png(it["jid"], zoom=3.0)
            rid = rid_for(X.slide, f)
            sid = X.nid()
            X.add(X.pic(sid, it["x"] + (it.get("w0", it["w"]) - it["w"]) / 2 if False else (L.CX0 + (L.CW - it["w"]) / 2),
                        it["y"], it["w"], it["h"], rid, "Table"), st, sid)


def add_sections(prs, deck):
    lang = deck.lang
    pres = prs.part._element
    ids = [s.get("id") for s in pres.find("{%s}sldIdLst" % NS_P)]
    bounds = []
    for k, (sec, first) in enumerate(deck.sections):
        last = deck.sections[k + 1][1] if k + 1 < len(deck.sections) else len(ids)
        if sec == "front":
            name = "مقدمه" if lang == "fa" else "Front matter"
        else:
            name = L.LABELS[lang]["chapter"] + " " + L.num(lang, str(sec.num)) + ": " + plain_title(sec.title)
        bounds.append((name, ids[first:last]))
    secs = "".join('<p14:section name="%s" id="{%s}"><p14:sldIdLst>%s</p14:sldIdLst></p14:section>' % (
        html.escape(n), str(uuid.uuid4()).upper(), "".join('<p14:sldId id="%s"/>' % i for i in sl)) for n, sl in bounds)
    xml = ('<p:extLst xmlns:p="%s"><p:ext uri="{521415D9-36F7-43E2-AB2F-B90AF26B5E84}">'
           '<p14:sectionLst xmlns:p14="%s">%s</p14:sectionLst></p:ext></p:extLst>') % (NS_P, NS_P14, secs)
    old = pres.find("{%s}extLst" % NS_P)
    if old is not None:
        pres.remove(old)
    pres.append(etree.fromstring(xml))
