#!/usr/bin/env python3
"""Check a generated PowerPoint file: titles on every slide, the click sequence of every slide.

    python3 slides/tools/check_pptx.py slides/EngineeringMath-slider-fa.pptx [slide numbers]

For every slide: the title text, and per click the shapes that appear.  It fails when a slide has
no title, when an animation is not an entrance Fade started On Click (first effect of a click)
or With Previous (the others), when a duration is not 0.25 s, or when a trigger or an automatic
timing is present.
"""
import re
import sys
import zipfile

from lxml import etree

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
      "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main"}


def slide_order(z):
    pres = etree.fromstring(z.read("ppt/presentation.xml"))
    rels = etree.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
    rmap = {r.get("Id"): r.get("Target") for r in rels}
    ids = []
    for s in pres.find("p:sldIdLst", NS):
        rid = s.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        ids.append((s.get("id"), "ppt/" + rmap[rid]))
    sections = []
    for sec in pres.iter("{%s}section" % NS["p14"]):
        sections.append((sec.get("name"), [x.get("id") for x in sec.iter("{%s}sldId" % NS["p14"])]))
    return ids, sections


def check(path, show=None):
    z = zipfile.ZipFile(path)
    ids, sections = slide_order(z)
    problems = []
    total_clicks = 0
    report = []
    for n, (sid, part) in enumerate(ids, 1):
        x = etree.fromstring(z.read(part))
        names = {}
        title = None
        for el in x.iter("{%s}cNvPr" % NS["p"]):
            names[el.get("id")] = el.get("name")
        for sp in x.iter("{%s}sp" % NS["p"]):
            nm = sp.find(".//p:cNvPr", NS).get("name")
            if nm.startswith("Title "):
                title = "".join(t.text or "" for t in sp.iter("{%s}t" % NS["a"]))
        if n > 1 and not (title or "").strip():
            problems.append("slide %d: no title" % n)
        clicks = []
        seq = x.find(".//p:timing//p:cTn[@nodeType='mainSeq']", NS)
        if x.find(".//p:timing", NS) is not None and seq is None:
            problems.append("slide %d: timing without a main sequence" % n)
        if seq is not None:
            if x.findall(".//p:timing//p:seq[@concurrent]", NS) and len(x.findall(".//p:timing//p:seq", NS)) > 1:
                problems.append("slide %d: interactive (trigger) sequence present" % n)
            for click in seq.find("p:childTnLst", NS):
                ctn = click.find("p:cTn", NS)
                cond = ctn.find("p:stCondLst/p:cond", NS)
                if cond.get("delay") != "indefinite":
                    problems.append("slide %d: a step does not wait for a click" % n)
                shapes = []
                for k, eff in enumerate(ctn.iter("{%s}cTn" % NS["p"])):
                    nt = eff.get("nodeType")
                    if nt in ("clickEffect", "withEffect", "afterEffect"):
                        want = "clickEffect" if not shapes else "withEffect"
                        if nt != want:
                            problems.append("slide %d: effect %s where %s expected" % (n, nt, want))
                        if eff.get("presetClass") != "entr" or eff.get("presetID") != "10":
                            problems.append("slide %d: not an entrance Fade" % n)
                        d = eff.find(".//p:animEffect/p:cBhvr/p:cTn", NS)
                        if d is None or d.get("dur") != "250":
                            problems.append("slide %d: fade duration is not 0.25 s" % n)
                        tg = eff.find(".//p:spTgt", NS).get("spid")
                        shapes.append(names.get(tg, "?" + tg))
                        dl = eff.find("p:stCondLst/p:cond", NS).get("delay")
                        if dl != "0":
                            problems.append("slide %d: delayed effect" % n)
                clicks.append(shapes)
        if x.find(".//p:transition", NS) is not None and x.find(".//p:transition", NS).get("advTm"):
            problems.append("slide %d: automatic advance" % n)
        total_clicks += len(clicks)
        if show is None or n in show:
            report.append("%3d  %s  [%d clicks]" % (n, title, len(clicks)))
            for k, c in enumerate(clicks, 1):
                report.append("       click %d: %s" % (k, ", ".join(c)))
    return ids, sections, total_clicks, problems, report


if __name__ == "__main__":
    show = set(int(a) for a in sys.argv[2:]) if len(sys.argv) > 2 else set()
    ids, sections, clicks, problems, report = check(sys.argv[1], show)
    print("\n".join(report))
    print("%d slides, %d clicks, %d sections" % (len(ids), clicks, len(sections)))
    for name, sl in sections:
        print("   section %-60s %3d slides" % (name, len(sl)))
    print("problems:", len(problems))
    for p in problems[:50]:
        print("  ", p)
    sys.exit(1 if problems else 0)
