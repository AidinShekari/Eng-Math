"""Embed TrueType fonts in a .pptx (File > Options > Save > Embed fonts, done by hand).

PowerPoint keeps an embedded font as ppt/fonts/fontN.fntdata in Embedded OpenType (EOT) form;
here an uncompressed EOT (version 0x00020001) wraps the whole font file.
"""
import re
import struct
import zipfile
from pathlib import Path

from fontTools.ttLib import TTFont

REL_FONT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"


def _name(tt, nid):
    for rec in tt["name"].names:
        if rec.nameID == nid and rec.platformID == 3:
            return rec.toUnicode()
    return tt["name"].getDebugName(nid) or ""


def eot(path: Path) -> bytes:
    data = path.read_bytes()
    tt = TTFont(str(path))
    os2 = tt["OS/2"]
    head = tt["head"]
    pan = os2.panose
    panose = bytes([pan.bFamilyType, pan.bSerifStyle, pan.bWeight, pan.bProportion, pan.bContrast,
                    pan.bStrokeVariation, pan.bArmStyle, pan.bLetterForm, pan.bMidline, pan.bXHeight])
    italic = 1 if (os2.fsSelection & 1) else 0

    def s(t):
        b = t.encode("utf-16-le")
        return struct.pack("<H", len(b)) + b
    names = (struct.pack("<H", 0) + s(_name(tt, 1)) + struct.pack("<H", 0) + s(_name(tt, 2)) +
             struct.pack("<H", 0) + s(_name(tt, 5)) + struct.pack("<H", 0) + s(_name(tt, 4)) +
             struct.pack("<H", 0) + struct.pack("<H", 0))  # Padding5, RootStringSize = 0
    fixed = (struct.pack("<LL", 0x00020001, 0) + panose + struct.pack("<BB", 1, italic) +
             struct.pack("<LHH", os2.usWeightClass, 0, 0x504C) +
             struct.pack("<LLLL", os2.ulUnicodeRange1, os2.ulUnicodeRange2, os2.ulUnicodeRange3, os2.ulUnicodeRange4) +
             struct.pack("<LL", os2.ulCodePageRange1, os2.ulCodePageRange2) +
             struct.pack("<L", head.checkSumAdjustment) + struct.pack("<LLLL", 0, 0, 0, 0))
    body = struct.pack("<L", len(data)) + fixed + names
    total = 4 + len(body) + len(data)
    return struct.pack("<L", total) + body + data


def embed(pptx: Path, fonts):
    """fonts: [(typeface, panose hex, pitchFamily, charset, {'regular': path, 'bold': path, ...})]"""
    src = zipfile.ZipFile(pptx)
    items = {n: src.read(n) for n in src.namelist()}
    src.close()
    rels = items["ppt/_rels/presentation.xml.rels"].decode("utf-8")
    pres = items["ppt/presentation.xml"].decode("utf-8")
    ct = items["[Content_Types].xml"].decode("utf-8")
    used = [int(x) for x in re.findall(r'Id="rId(\d+)"', rels)]
    nxt = max(used) + 1
    k = 1
    lst = []
    for face, panose, pitch, charset, files in fonts:
        parts = []
        for style in ("regular", "bold", "italic", "boldItalic"):
            f = files.get(style)
            if not f:
                continue
            name = "ppt/fonts/font%d.fntdata" % k
            items[name] = eot(Path(f))
            rid = "rId%d" % nxt
            rels = rels.replace("</Relationships>",
                                '<Relationship Id="%s" Type="%s" Target="fonts/font%d.fntdata"/></Relationships>' % (rid, REL_FONT, k))
            parts.append('<p:%s r:id="%s"/>' % (style, rid))
            k += 1
            nxt += 1
        lst.append('<p:embeddedFont><p:font typeface="%s" panose="%s" pitchFamily="%d" charset="%d"/>%s</p:embeddedFont>'
                   % (face, panose, pitch, charset, "".join(parts)))
    block = "<p:embeddedFontLst>%s</p:embeddedFontLst>" % "".join(lst)
    pres = re.sub(r"<p:embeddedFontLst>.*?</p:embeddedFontLst>", "", pres, flags=re.S)
    m = re.search(r"<p:notesSz[^>]*/>", pres)
    pres = pres[:m.end()] + block + pres[m.end():]
    if "embedTrueTypeFonts" not in pres:
        pres = re.sub(r"<p:presentation ", '<p:presentation embedTrueTypeFonts="1" ', pres, count=1)
    if 'Extension="fntdata"' not in ct:
        ct = ct.replace("<Default ", '<Default Extension="fntdata" ContentType="application/x-fontdata"/><Default ', 1)
    items["ppt/_rels/presentation.xml.rels"] = rels.encode("utf-8")
    items["ppt/presentation.xml"] = pres.encode("utf-8")
    items["[Content_Types].xml"] = ct.encode("utf-8")
    tmp = pptx.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        order = ["[Content_Types].xml"] + [n for n in items if n != "[Content_Types].xml"]
        for n in order:
            z.writestr(n, items[n])
    tmp.replace(pptx)
