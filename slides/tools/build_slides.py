#!/usr/bin/env python3
"""Build the slide decks of the Engineering Mathematics notes.

    python3 slides/tools/build_slides.py --lang fa      # or en; both when omitted
    options: --no-pptx  --no-beamer  --chapters 1-3

From the chapter bodies NN-slug/<lang>/content.tex (generated from the notes; not modified) it
writes
    slides/main-<lang>.tex + slides/<lang>/chNN.tex     Beamer source (overlays: \\uncover<n->)
    slides/EngineeringMath-slider-<lang>.pptx           PowerPoint (On Click fade per step)
One pagination serves both: every piece is measured with XeLaTeX (tectonic) in the fonts of
the PowerPoint file and in those of the Beamer deck, and the larger size is used.
Needs: tectonic, pandoc (LaTeX -> OMML), python-pptx, pymupdf; for the PowerPoint fonts the
measuring run reads Tahoma (macOS) and Calibri / Cambria Math (Microsoft Office).
"""
import argparse
import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import texparse as T  # noqa: E402
import layout as L  # noqa: E402
import measure as M  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"
WORK = SLIDES / "build"
MODES = ("pptx", "beamer")


# ============================================================ sources
def chapter_dirs():
    return sorted(p for p in ROOT.iterdir() if re.match(r"\d\d-", p.name) and not p.name.startswith("00"))


def load(lang, only=None):
    chapters = []
    for d in chapter_dirs():
        n = int(d.name[:2])
        if only and n not in only:
            continue
        mod = next((d / lang).glob("module*.tex")).read_text(encoding="utf-8")
        num, title, other = T.chapter_title(mod)
        blocks = T.parse_content((d / lang / "content.tex").read_text(encoding="utf-8"), n)
        ch = T.Chapter(n, d.name, title, blocks, T.minitoc(mod))
        ch.other = other
        chapters.append(ch)
    return chapters


def book_parts(lang):
    """Parts of the book (from the complete notes): [(numeral, title, first chapter, range text)]."""
    src = (ROOT / "00-full-notes" / lang / f"EngineeringMath-{lang}.tex").read_text(encoding="utf-8")
    parts = []
    for m in re.finditer(r"\\EMpartpage\{(\d+)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}", src):
        key = int(m.group(1))
        rest = src[m.end():]
        first = int(re.search(r"\\EMsetmodule\{(\d+)\}", rest).group(1))
        parts.append((m.group(2), m.group(3), first, m.group(5)))
    cover = re.search(r"\\EMcoverpage\{(.*?)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}\n", src)
    return parts, cover.groups()


def front_matter(lang):
    """The course information and the formula sheet of the complete notes, as blocks."""
    src = (ROOT / "template" / "em-front.tex").read_text(encoding="utf-8")
    strings = (ROOT / "template" / f"em-{lang}.tex").read_text(encoding="utf-8")
    def s(name):
        return re.search(r"\\def\\" + name + r"\{(.*)\}", strings).group(1)
    a = src.index(r"\newcommand{\EMcourseinfo}")
    body = src[a:src.index(r"% ---------- the formula sheet")]
    rtl_a = body.index(r"\ifEMrtl") + len(r"\ifEMrtl")
    else_i = body.index(r"\else", rtl_a)
    fi_i = body.rindex(r"\fi")
    info = body[rtl_a:else_i] if lang == "fa" else body[else_i + len(r"\else"):fi_i]
    blocks = [T.Heading(1, s("EMlangInfoTitle"))]
    i = 0
    tiles = []
    while i < len(info):
        if info.startswith(r"\EMinfohead{", i):
            t, i = T.balanced(info, i + len(r"\EMinfohead"))
            blocks.append(T.Heading(2, t))
            continue
        if info.startswith(r"\EMinfo{", i):
            a1, j = T.balanced(info, i + len(r"\EMinfo"))
            a2, i = T.balanced(info, j)
            a2 = a2.replace("\\\\\n", " ").replace(r"\hspace*{1.2em}", "")
            txt = r"\textbf{" + a1 + "}" + (" — " + " ".join(a2.split()) if a2.strip() else "")
            blocks.append(T.Group([T.Para(txt)]))
            continue
        if info.startswith(r"\EMtile{", i):
            a1, j = T.balanced(info, i + len(r"\EMtile"))
            a2, i = T.balanced(info, j)
            tiles.append(r"\textbf{" + a1 + "} — " + a2.replace("\\\\", " "))
            if not re.match(r"\s*\\hfill\s*\\EMtile", info[i:]):
                blocks.append(T.Group([T.ListBlock(False, [[T.Para(t)] for t in tiles])]))
                tiles = []
            continue
        if info.startswith(r"\begin{itemize}", i):
            e0, e1 = T.find_env_end(info, i + len(r"\begin{itemize}"), "itemize")
            blocks.append(T.Group([T.parse_list(info[i + len(r"\begin{itemize}"):e0], False)]))
            i = e1
            continue
        i += 1
    # formula sheet: one slide per box, one step per group of rows
    sheet = src[src.index(r"\newcommand{\EMcheatsheet}"):]
    sheet_blocks = [T.Heading(1, s("EMlangSheetTitle"))]
    for m in re.finditer(r"\\EMsheetbox\{\\(EMlang\w+)\}\{", sheet):
        body, _ = T.balanced(sheet, m.end() - 1)
        sheet_blocks.append(T.Heading(2, s("EMlangSheetTitle") + " — " + s(m.group(1))))
        k = 0
        while True:
            k = body.find(r"\EMrows{", k)
            if k < 0:
                break
            rows, k = T.balanced(body, k + len(r"\EMrows"))
            lines = [r.strip() for r in re.split(r"\\\\(?:\\noalign\{\\vskip \d+pt\})?", rows) if r.strip()]
            els = [T.Disp(ln.replace("&", "=", 1)) for ln in lines]
            g = T.Group(els)
            g.single = True  # one group of rows = one step
            sheet_blocks.append(g)
    return blocks, sheet_blocks


# ============================================================ model
class Deck:
    def __init__(self, lang):
        self.lang = lang
        self.slides = []        # dicts
        self.sections = []      # (name, first slide index)
        self.warnings = []


def all_els(flow):
    for it in flow.items:
        if isinstance(it, L.Unit):
            for e in it.els:
                yield it, e


def widths_for(unit, el):
    base = [L.CW, L.NW]
    out = []
    for w in base:
        if unit.box:
            w -= L.BOX_IN
        if el.kind == "item" or getattr(el, "in_item", False):
            w -= L.LIST_IND
        out.append(round(w, 2))
    return out


def text_of_tex(tex):
    return tex


def prep_title(t):
    return " ".join(t.split())


def table_tex(tex):
    t = tex.replace(r"\begin{longtable}[c]", r"\begin{tabular}").replace(r"\begin{longtable}", r"\begin{tabular}")
    t = t.replace(r"\end{longtable}", r"\end{tabular}")
    t = re.sub(r"\\endhead|\\endlastfoot|\\endfirsthead|\\endfoot", "", t)
    t = re.sub(r"\\bottomrule\\noalign\{\}\s*\n", "", t, count=1)
    t = t.rstrip()
    t = t[:-len(r"\end{tabular}")] + "\\bottomrule\n\\end{tabular}"
    return r"\setlength{\columnwidth}{%dpt}\centering " % int(L.CW * 0.9) + t


# ============================================================ measuring
def measure_all(lang, flows, titles, workdir):
    """Two measuring passes (segments, then everything) in both font set-ups."""
    align = "r" if lang == "fa" else "l"
    # pass A: segments of the displays
    segjobs = []
    dispsegs = {}
    n = 0
    for fl in flows:
        for unit, e in all_els(fl):
            if e.kind == "disp":
                n += 1
                e.jid = "d%d" % n
                segs = L.split_segments(e.tex)
                e.segs = segs
                for k, sg in enumerate(segs):
                    segjobs.append(("%s_%d" % (e.jid, k), "hmath", 0, sg))
    sa = {m: M.run(segjobs, lang, m, workdir, "segs")[0] for m in MODES}
    # lines per width
    pages_jobs = []
    for fl in flows:
        for unit, e in all_els(fl):
            if e.kind != "disp":
                continue
            segw = [max(sa[m]["%s_%d" % (e.jid, k)][0] for m in MODES) for k in range(len(e.segs))]
            e.segw = segw
            e.lines_by_w = {}
            for w in widths_for(unit, e):
                lines = L.break_lines(segw, w - 8)
                e.lines_by_w[w] = lines
    # pass B
    jobs = []
    seen = set()

    def add(job):
        if job[0] not in seen:
            seen.add(job[0])
            jobs.append(job)
    n = 0
    for fl in flows:
        for unit, e in all_els(fl):
            n += 1
            if not e.jid:
                e.jid = "e%d" % n
            if e.kind in ("para", "item"):
                for w in widths_for(unit, e):
                    add(("%s_w%d" % (e.jid, w), "para", w, e.tex, align, L.BODY))
            elif e.kind == "disp":
                for w, lines in e.lines_by_w.items():
                    key = "%s_l%s" % (e.jid, "-".join(str(len(x)) for x in lines))
                    tex = r" \\[4pt] ".join(" ".join(e.segs[k] for k in ln) for ln in lines)
                    add((key, "eq", 0, tex))
            elif e.kind == "fig":
                add((e.jid + "_fig", "fig", 0, e.name))
                for w in (L.FIGW, 640):
                    add(("%s_cap%d" % (e.jid, w), "para", w, e.tex, "c", L.CAPTION))
            elif e.kind == "table":
                add((e.jid + "_tab", "vraw", L.CW, table_tex(e.tex)))
        for it in fl.items:
            if isinstance(it, L.Unit) and it.box and not getattr(it.box, "jid", None):
                b = it.box
                b.jid = "h%d_%s" % (b.bid, fl.key)
                lab, title = b.head
                tex = r"\textbf{" + lab + "}" + ((r"\ \ |\ \ " + title) if title else "")
                b.headtex = tex
                for w in (L.CW - L.BOX_IN, L.NW - L.BOX_IN):
                    add(("%s_w%d" % (b.jid, w), "para", w, tex, align, L.HEAD))
    for k, t in enumerate(titles):
        add(("t%d" % k, "raw", 0, r"\fontsize{%d}{%d}\selectfont\bfseries " % (L.TITLE, L.TITLE + 4) + t))
    res = {m: M.run(jobs, lang, m, workdir, "all") for m in MODES}
    sizes = {}
    for jid in seen:
        vals = [res[m][0].get(jid) for m in MODES]
        if None in vals:
            raise SystemExit("missing size for " + jid)
        sizes[jid] = dict(wd=max(v[0] for v in vals), h=max(v[1] + v[2] for v in vals),
                          hp=vals[0][1] + vals[0][2], wp=vals[0][0])
    return sizes, res["pptx"][1], res["pptx"][2]


# ============================================================ pagination
class Pager:
    def __init__(self, lang, sizes, deck):
        self.lang = lang
        self.S = sizes
        self.deck = deck

    # --- sizes of pieces ---
    def el_h(self, unit, e, narrow):
        w = widths_for(unit, e)[1 if narrow else 0]
        if e.kind in ("para", "item"):
            return self.S["%s_w%d" % (e.jid, w)]["h"] * L.SLACK
        if e.kind == "disp":
            lines = e.lines_by_w[w]
            key = "%s_l%s" % (e.jid, "-".join(str(len(x)) for x in lines))
            s = self.S[key]
            sc = min(1.0, (w - 4) / s["wd"])
            return s["h"] * sc * L.SLACK + 6
        if e.kind == "table":
            s = self.S[e.jid + "_tab"]
            sc = min(1.0, L.CW / s["wd"])
            return s["h"] * sc + 4
        if e.kind == "fig":
            if self.fig_side(e):
                return 0.0
            sc = self.fig_full_scale(e)
            return self.S[e.jid + "_fig"]["h"] * sc + 6 + self.S["%s_cap640" % e.jid]["h"]
        raise ValueError(e.kind)

    def fig_side_scale(self, e):
        s = self.S[e.jid + "_fig"]
        cap = self.S["%s_cap%d" % (e.jid, L.FIGW)]["h"]
        return min(L.FIGW / s["wd"], 1.5, (L.CY1 - L.CY0 - cap - 8) / s["h"])

    def fig_side(self, e):
        return self.fig_side_scale(e) >= 0.72

    def fig_full_scale(self, e):
        s = self.S[e.jid + "_fig"]
        cap = self.S["%s_cap640" % e.jid]["h"]
        return min(L.CW * 0.85 / s["wd"], 1.5, (L.CY1 - L.CY0 - cap - 12) / s["h"])

    def unit_h(self, unit, narrow):
        hs = [self.el_h(unit, e, narrow) for e in unit.els]
        hs = [h for h in hs if h > 0]
        return sum(hs) + 3.0 * max(0, len(hs) - 1)

    def side_fig(self, units):
        figs = [e for u in units for e in u.els if e.kind == "fig" and self.fig_side(e)]
        return figs

    def column_h(self, units, head_boxes):
        """Height of the text column; head_boxes: boxes whose head is drawn on this slide."""
        narrow = bool(self.side_fig(units))
        y = 0.0
        prev_box = None
        first = True
        for u in units:
            if u.box is not prev_box:
                if prev_box is not None:
                    y += L.BOXPAD_B + L.GAP_BOX
                elif not first:
                    y += L.GAP_BOX if u.box else 0
                if u.box is not None:
                    y += L.BOXPAD_T
                    if u.box.bid in head_boxes:
                        w = (L.NW if narrow else L.CW) - L.BOX_IN
                        y += self.S["%s_w%d" % (u.box.jid, w)]["h"] + 4
            elif not first:
                y += L.GAP
            uh = self.unit_h(u, narrow)
            y += uh
            prev_box = u.box
            first = False
        if prev_box is not None:
            y += L.BOXPAD_B
        return y

    def fits(self, units, head_boxes):
        figs = self.side_fig(units)
        if len(figs) > 1:
            return False
        for f in figs:
            s = self.S[f.jid + "_fig"]
            sc = self.fig_side_scale(f)
            if s["h"] * sc + self.S["%s_cap%d" % (f.jid, L.FIGW)]["h"] + 8 > L.CY1 - L.CY0:
                return False
        if figs:
            # a formula that fits the full width must not be shrunk to make room for a figure
            for u in units:
                for e in u.els:
                    if e.kind == "disp":
                        wf, wn = widths_for(u, e)
                        if self.disp_scale(e, wn) < 0.97 and self.disp_scale(e, wf) >= 0.97:
                            return False
        return self.column_h(units, head_boxes) <= L.CY1 - L.CY0

    def disp_scale(self, e, w):
        lines = e.lines_by_w[w]
        key = "%s_l%s" % (e.jid, "-".join(str(len(x)) for x in lines))
        return min(1.0, (w - 4) / self.S[key]["wd"])

    # --- slides ---
    def paginate(self, flow, chapter_label, default_title=None):
        slides = []
        cur = None
        title = default_title
        title_level = 1

        def new_slide():
            nonlocal cur
            cont = bool(slides) and slides[-1]["title"] == title and slides[-1]["chapter"] == chapter_label
            cur = dict(kind="content", title=title, cont=cont, units=[], heads=set(), chapter=chapter_label)
            slides.append(cur)

        def heads_of(units):
            hs = set()
            seen = set()
            for u in units:
                if u.box and u.box.bid not in seen:
                    seen.add(u.box.bid)
            return hs

        queue = list(flow.items)
        while queue:
            it = queue.pop(0)
            if isinstance(it, tuple):
                if it[0] == "title":
                    title = L.clean_title(it[1])
                    title_level = it[2]
                    cur = None
                elif it[0] == "break":
                    cur = None
                continue
            u = it
            if cur is None or not cur["units"]:
                if cur is None:
                    new_slide()
            trial = cur["units"] + [u]
            heads = set(cur["heads"])
            if u.box and u.box.bid not in self.box_started:
                heads.add(u.box.bid)
            if self.fits(trial, heads):
                cur["units"] = trial
                cur["heads"] = heads
                if u.box:
                    self.box_started.add(u.box.bid)
                continue
            if not cur["units"] and len(u.els) > 1:
                # a step taller than a slide: split it between its pieces
                head = []
                for e in u.els:
                    t = copy.copy(u)
                    t.els = head + [e]
                    if head and not self.fits([t], heads):
                        break
                    head.append(e)
                rest = u.els[len(head):]
                a = copy.copy(u)
                a.els = head
                b = copy.copy(u)
                b.els = rest
                if rest:
                    queue[0:0] = [a, b]
                    continue
            if not cur["units"]:
                # alone it does not fit: keep it (it will be scaled down to the slide)
                cur["units"] = trial
                cur["heads"] = heads
                if u.box:
                    self.box_started.add(u.box.bid)
                self.deck.warnings.append("too tall for one slide: %s / %s" % (chapter_label, title))
                continue
            # move the trailing units that belong with this one (same EMunit / statement), unless
            # they are all that is on the slide
            moved = []
            if u.keep:
                k = len(cur["units"])
                while k > 0 and cur["units"][k - 1].keep == u.keep:
                    k -= 1
                if k > 0:
                    moved = cur["units"][k:]
                    cur["units"] = cur["units"][:k]
            for mu in moved:
                if mu.box and mu.box.bid in cur["heads"] and not any(x.box is mu.box for x in cur["units"]):
                    cur["heads"].discard(mu.box.bid)
                    self.box_started.discard(mu.box.bid)
            new_slide()
            queue[0:0] = moved + [u]
        return [s for s in slides if s["units"]]


# ============================================================ placement
def place(slide, pager, lang):
    """Positions of everything on a content slide; steps of every shape."""
    S = pager.S
    units = slide["units"]
    figs = pager.side_fig(units)
    narrow = bool(figs)
    colw = L.NW if narrow else L.CW
    rtl = lang == "fa"
    if rtl:
        colx = L.CX1 - colw
        figx = L.CX0
    else:
        colx = L.CX0
        figx = L.CX1 - L.FIGW
    # steps
    step = 0
    steps = []
    for u in units:
        if u.initial:
            steps.append(0)
        else:
            step += 1
            steps.append(step)
    slide["nsteps"] = step
    slide["steps"] = steps
    items = []
    boxes = []
    y = L.CY0
    prev_box = None
    first = True
    curbox = None
    total = pager.column_h(units, slide["heads"])
    room = L.CY1 - L.CY0
    shrink = min(1.0, room / total) if total > 0 else 1.0
    slide["shrink"] = shrink
    for u, st in zip(units, steps):
        if u.box is not prev_box:
            if prev_box is not None:
                curbox["y1"] = y + L.BOXPAD_B
                y += L.BOXPAD_B + L.GAP_BOX
            elif not first:
                y += L.GAP_BOX if u.box else 0
            if u.box is not None:
                curbox = dict(box=u.box, y0=y, step=st, head=None, x=colx, w=colw)
                boxes.append(curbox)
                y += L.BOXPAD_T
                if u.box.bid in slide["heads"]:
                    w = colw - L.BOX_IN
                    hh = S["%s_w%d" % (u.box.jid, w)]["h"]
                    curbox["head"] = dict(y=y, h=hh, w=w, jid="%s_w%d" % (u.box.jid, w))
                    y += hh + 4
        elif not first:
            y += L.GAP
        x0 = colx + ((L.BOXPAD_X + (L.BOXBAR if not rtl else 0)) if u.box else 0)
        if u.box and rtl:
            x0 = colx + L.BOXPAD_X
        k = 0
        for e in u.els:
            w = widths_for(u, e)[1 if narrow else 0]
            if e.kind == "fig" and pager.fig_side(e):
                fs = S[e.jid + "_fig"]
                sc = pager.fig_side_scale(e)
                fw, fh = fs["wd"] * sc, fs["h"] * sc
                cap = S["%s_cap%d" % (e.jid, L.FIGW)]
                total_h = fh + 6 + cap["h"]
                fy = min(max(y, L.CY0), L.CY1 - total_h)
                items.append(dict(kind="fig", el=e, x=figx + (L.FIGW - fw) / 2, y=fy, w=fw, h=fh, step=st,
                                  scale=sc))
                items.append(dict(kind="cap", el=e, x=figx, y=fy + fh + 6, w=L.FIGW, h=cap["h"], step=st,
                                  jid="%s_cap%d" % (e.jid, L.FIGW)))
                continue
            if k:
                y += 3.0
            k += 1
            h = pager.el_h(u, e, narrow)
            ex = x0
            if e.kind == "item" or getattr(e, "in_item", False):
                ex = x0 + (0 if rtl else L.LIST_IND)
            if e.kind in ("para", "item"):
                items.append(dict(kind=e.kind, el=e, x=ex, y=y, w=w, h=h, step=st, jid="%s_w%d" % (e.jid, w)))
            elif e.kind == "disp":
                lines = e.lines_by_w[w]
                key = "%s_l%s" % (e.jid, "-".join(str(len(x)) for x in lines))
                s = S[key]
                sc = min(1.0, (w - 4) / s["wd"])
                if sc < 0.999:
                    pager.deck.warnings.append("display scaled to %.0f%%: %s" % (sc * 100, slide["title"]))
                items.append(dict(kind="disp", el=e, x=ex, y=y + 3, w=w, h=h - 6, step=st, jid=key, lines=lines,
                                  scale=sc, nat=(s["wp"] * sc, S[key]["hp"] * sc)))
            elif e.kind == "table":
                s = S[e.jid + "_tab"]
                sc = min(1.0, L.CW / s["wd"])
                items.append(dict(kind="table", el=e, x=ex, y=y, w=s["wd"] * sc, h=s["h"] * sc, step=st,
                                  jid=e.jid + "_tab", scale=sc))
            elif e.kind == "fig":
                fs = S[e.jid + "_fig"]
                sc = pager.fig_full_scale(e)
                fw, fh = fs["wd"] * sc, fs["h"] * sc
                items.append(dict(kind="fig", el=e, x=colx + (colw - fw) / 2, y=y, w=fw, h=fh, step=st, scale=sc))
                cap = S["%s_cap640" % e.jid]
                items.append(dict(kind="cap", el=e, x=colx + (colw - 640) / 2, y=y + fh + 6, w=640, h=cap["h"],
                                  step=st, jid="%s_cap640" % e.jid))
            y += h
        prev_box = u.box
        first = False
    if prev_box is not None:
        curbox["y1"] = y + L.BOXPAD_B
    if shrink < 1.0:
        # squeeze vertically (only when a single piece is taller than a slide)
        for it in items:
            if it["kind"] in ("fig", "cap") and narrow:
                continue
            it["y"] = L.CY0 + (it["y"] - L.CY0) * shrink
            it["h"] *= shrink
            it["w"] *= shrink
            it["scale_all"] = shrink
        for b in boxes:
            b["y0"] = L.CY0 + (b["y0"] - L.CY0) * shrink
            b["y1"] = L.CY0 + (b["y1"] - L.CY0) * shrink
            if b["head"]:
                b["head"]["y"] = L.CY0 + (b["head"]["y"] - L.CY0) * shrink
    slide["items"] = items
    slide["boxes"] = boxes
    slide["narrow"] = narrow
    slide["colx"], slide["colw"] = colx, colw


# ============================================================ main
def build(lang, args):
    only = None
    if args.chapters:
        a, _, b = args.chapters.partition("-")
        only = set(range(int(a), int(b or a) + 1))
    chapters = load(lang, only)
    parts, cover = book_parts(lang)
    info_blocks, sheet_blocks = front_matter(lang)
    deck = Deck(lang)
    flows = []
    fr = L.build_flow(lang, info_blocks + sheet_blocks)
    fr.key = "front"
    flows.append(fr)
    for ch in chapters:
        fl = L.build_flow(lang, ch.blocks)
        fl.key = "c%d" % ch.num
        ch.flow = fl
        flows.append(fl)
    # titles to check
    titles = set()
    for fl in flows:
        for it in fl.items:
            if isinstance(it, tuple) and it[0] == "title":
                titles.add(L.clean_title(it[1]))
    for ch in chapters:
        titles.add(L.LABELS[lang]["chapter"] + " " + L.num(lang, str(ch.num)) + ": " + ch.title)
    titles = sorted(titles)
    cont = L.LABELS[lang]["cont"]
    all_titles = titles + [t + " " + cont for t in titles]
    WORK.mkdir(parents=True, exist_ok=True)
    sizes, pdf, pages = measure_all(lang, flows, all_titles, WORK)
    title_w = {t: sizes["t%d" % k]["wd"] for k, t in enumerate(all_titles)}
    pager = Pager(lang, sizes, deck)
    pager.box_started = set()
    # ---- slides
    deck.slides.append(dict(kind="cover", title=None, cover=cover, cont=False, chapter=None))
    deck.sections.append(("front", 0))
    for s in pager.paginate(fr, "front"):
        deck.slides.append(s)
    part_at = {p[2]: p for p in parts}
    for ch in chapters:
        deck.sections.append((ch, len(deck.slides)))
        if ch.num in part_at:
            p = part_at[ch.num]
            deck.slides.append(dict(kind="part", title=L.LABELS[lang]["part"] + " " + p[0], part=p, cont=False,
                                    chapter=ch.num))
        ctitle = L.LABELS[lang]["chapter"] + " " + L.num(lang, str(ch.num)) + ": " + ch.title
        deck.slides.append(dict(kind="chapter", title=ctitle, ch=ch, cont=False, chapter=ch.num))
        for s in pager.paginate(ch.flow, ch.num, ch.title):
            deck.slides.append(s)
    for s in deck.slides:
        if s["kind"] == "content":
            place(s, pager, lang)
    deck.title_w = title_w
    deck.pager = pager
    deck.sizes, deck.pdf, deck.pages = sizes, pdf, pages
    deck.chapters = chapters
    deck.parts = parts
    return deck


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["fa", "en"])
    ap.add_argument("--chapters")
    ap.add_argument("--no-pptx", action="store_true")
    ap.add_argument("--no-beamer", action="store_true")
    args = ap.parse_args()
    for lang in ([args.lang] if args.lang else ["fa", "en"]):
        deck = build(lang, args)
        n = len(deck.slides)
        steps = sum(s.get("nsteps", 0) for s in deck.slides)
        print(f"[{lang}] {n} slides, {steps} click steps")
        for w in deck.warnings:
            print("  warning:", w)
        if not args.no_beamer:
            import beamer_out
            beamer_out.write(deck)
        if not args.no_pptx:
            import pptx_out
            pptx_out.write(deck)


if __name__ == "__main__":
    main()
