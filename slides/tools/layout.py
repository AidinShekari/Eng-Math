"""From the parsed notes to slides: units (one click each), measurement, pagination.

Geometry is in points on a 960 x 540 pt (13.333 x 7.5 in, 16:9) slide; the PowerPoint files and
the Beamer decks use the same numbers.
"""
import re
from dataclasses import dataclass, field
from typing import List, Optional

import texparse as T

# ---------- geometry ----------
SW, SH = 960.0, 540.0
BAR = dict(x=22.0, y=14.0, w=916.0, h=48.0)
CX0, CX1 = 40.0, 920.0           # content column
CY0, CY1 = 80.0, 506.0           # content top / bottom
CW = CX1 - CX0                   # 880
FIGW = 360.0                     # side column for a figure
COLGAP = 20.0
NW = CW - FIGW - COLGAP          # text column next to a figure: 500
BOXPAD_X, BOXBAR, BOXPAD_T, BOXPAD_B = 12.0, 5.0, 6.0, 8.0
BOX_IN = 2 * BOXPAD_X + BOXBAR   # width lost inside a box
LIST_IND = 26.0
GAP = 7.0                        # between units
GAP_BOX = 9.0                    # around a box
SLACK = 1.05                     # heights are taken 5 % larger than measured (font differences)
BODY = 20
CAPTION = 15
HEAD = 19
TITLE = 26

BOX_KIND = {
    "EMdefinition": "def", "EMtheorem": "thm", "EMlemma": "thm", "EMproposition": "thm",
    "EMcorollary": "thm", "EMimportant": "imp", "EMexample": "ex", "EMexercise": "exe",
    "EMremark": "rem", "EMproof": "prf",
}
STATEMENT_FIRST = {"EMexample", "EMexercise"}

LABELS = {
    "fa": {"EMdefinition": "تعریف", "EMtheorem": "قضیه", "EMlemma": "لم", "EMproposition": "گزاره",
           "EMcorollary": "نتیجه", "EMimportant": "نتیجهٔ مهم", "EMexample": "مثال", "EMexercise": "تمرین",
           "EMremark": "نکته", "EMproof": "اثبات", "cont": "(ادامه)", "chapter": "فصل", "part": "بخش",
           "figure": "شکل", "contents": "مطالب این فصل"},
    "en": {"EMdefinition": "Definition", "EMtheorem": "Theorem", "EMlemma": "Lemma",
           "EMproposition": "Proposition", "EMcorollary": "Corollary", "EMimportant": "Key result",
           "EMexample": "Example", "EMexercise": "Exercise", "EMremark": "Remark", "EMproof": "Proof",
           "cont": "(continued)", "chapter": "Chapter", "part": "Part", "figure": "Figure",
           "contents": "In this chapter"},
}
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
# the labels written with the single letter U+06C0 (B Nazanin has no combining hamza)
LABELS["fa"] = {k: v.replace("\u0647\u0654", "\u06c0") for k, v in LABELS["fa"].items()}


def num(lang, s):
    return s.translate(FA_DIGITS) if lang == "fa" else s


# ---------- units ----------
@dataclass
class El:
    """One drawable element of a unit."""
    kind: str               # para | disp | fig | item | table | cap
    tex: str = ""
    name: str = ""          # figure name
    ordered: bool = False
    index: int = 0          # list item number
    lines: list = None      # display lines (decided per width)
    jid: str = ""
    in_item: bool = False   # a piece of a list item after its first paragraph


@dataclass
class Unit:
    els: List[El]
    box: Optional[object] = None    # BoxInfo
    initial: bool = False           # visible when the slide opens
    keep: Optional[str] = None      # units with the same key prefer the same slide
    uid: int = 0


@dataclass
class BoxInfo:
    env: str
    kind: str
    head: str        # label + number (+ title), TeX
    bid: int


@dataclass
class Flow:
    """Everything of one chapter in reading order: ('title', text) | ('break',) | Unit."""
    items: list = field(default_factory=list)


def box_head(lang, box: T.Box):
    """(label with number, title) of a box."""
    lab = LABELS[lang][box.env]
    if box.number:
        lab += " " + num(lang, box.number)
    return lab, box.title


def elements_of(e) -> List[List[El]]:
    """A parsed element -> a list of units (each a list of El)."""
    if e.kind == "para":
        return [[El("para", e.tex)]]
    if e.kind == "disp":
        return [[El("disp", e.tex)]]
    if e.kind == "fig":
        return [[El("fig", e.caption, name=e.name)]]
    if e.kind == "table":
        return [[El("table", e.tex)]]
    if e.kind == "list":
        out = []
        for k, it in enumerate(e.items):
            els = []
            for sub in it:
                if sub.kind == "para":
                    els.append(El("item", sub.tex, ordered=e.ordered, index=k + 1) if not els
                               else El("para", sub.tex, in_item=True))
                elif sub.kind == "disp":
                    if not els:
                        els.append(El("item", "", ordered=e.ordered, index=k + 1))
                    els.append(El("disp", sub.tex, in_item=True))
                elif sub.kind == "list":
                    for u in elements_of(sub):
                        for x in u:
                            x.in_item = True
                        els.extend(u)
            out.append(els)
        return out
    raise ValueError(e.kind)


def group_units(group: T.Group) -> List[List[El]]:
    """Units of one paragraph group: a lead-in paragraph goes with the display it introduces."""
    if getattr(group, "single", False):
        return [[El(e.kind, e.tex) for e in group.elements]]
    units = []
    els = group.elements
    i = 0
    while i < len(els):
        e = els[i]
        if e.kind == "para" and i + 1 < len(els) and els[i + 1].kind == "disp":
            units.append([El("para", e.tex), El("disp", els[i + 1].tex)])
            i += 2
            continue
        units.extend(elements_of(e))
        i += 1
    return units


def build_flow(lang, blocks) -> Flow:
    fl = Flow()
    bid = 0
    uid = 0
    for b in blocks:
        if b.kind == "heading":
            fl.items.append(("title", b.title, b.level))
            continue
        if b.kind == "group":
            for u in group_units(b):
                uid += 1
                fl.items.append(Unit(u, keep=("u%d" % b.unit) if b.unit else None, uid=uid))
            continue
        if b.kind == "box":
            bid += 1
            info = BoxInfo(b.env, BOX_KIND[b.env], box_head(lang, b), bid)
            if b.env in STATEMENT_FIRST:
                fl.items.append(("break",))
            units = []
            for gi, g in enumerate(b.groups):
                for u in group_units(g):
                    units.append((gi, u))
            # the statement: the first paragraph group (when the solution follows it)
            ngroups = len(b.groups)
            for k, (gi, u) in enumerate(units):
                uid += 1
                initial = False
                if b.env in STATEMENT_FIRST:
                    if ngroups > 1:
                        initial = gi == 0
                    else:
                        initial = k == 0
                fl.items.append(Unit(u, box=info, initial=initial, keep="b%d" % bid if initial else None,
                                     uid=uid))
            continue
        raise ValueError(b.kind)
    return fl


# ---------- display lines ----------
def split_segments(tex: str) -> List[str]:
    out = []
    for p in tex.split(r"\EMbr"):
        q = p.strip()
        if re.search(r"(?<!\\)(\\\\)*\\$", q):  # ends with a control space "\ "
            q += " "
        if q:
            out.append(q)
    return out


def break_lines(segw: List[float], width: float) -> List[List[int]]:
    """Greedy filling of display lines from the measured widths of the break segments."""
    lines, cur, w = [], [], 0.0
    for k, sw in enumerate(segw):
        add = sw + (5.0 if cur else 0.0)
        if cur and w + add > width:
            lines.append(cur)
            cur, w = [], 0.0
            add = sw
        cur.append(k)
        w += add
    if cur:
        lines.append(cur)
    return lines


def clean_title(t: str) -> str:
    return " ".join(t.split())


def title_style(width):
    """(font size, two lines) of a slide title whose width at TITLE size is `width`."""
    room = BAR["w"] - 36
    if not width or width <= room:
        return TITLE, False
    if width * 20 / TITLE <= room:
        return max(20, int(TITLE * room / width)), False
    return 17, True


# ---------- B Nazanin lacks a few characters ----------
FA_MISSING = "\u2014\u2013\u2022|\u066b\u066a"   # em dash, en dash, bullet, bar, Arabic decimal separator


def fa_fix(tex):
    """Persian text for B Nazanin: he + hamza above -> the single letter heh with yeh (U+06C0);
    the characters the font lacks are set in the Latin font (\\lr{...}), outside formulas."""
    if not tex:
        return tex
    tex = tex.replace("\u0647\u0654", "\u06c0").replace("\u0647\u200c\u0654", "\u06c0")
    out = []
    i = 0
    n = len(tex)
    while i < n:
        if tex.startswith("\\EMim{", i):
            j = _skip_braced(tex, i + 5)
            out.append(tex[i:j])
            i = j
            continue
        if tex[i] == "$":
            j = tex.find("$", i + 1)
            j = n if j < 0 else j + 1
            out.append(tex[i:j])
            i = j
            continue
        m = re.match(r"\\(dots|ldots|textbar)(?![A-Za-z])", tex[i:])
        if m:  # characters B Nazanin lacks, written as commands
            out.append("\\lr{%s}" % m.group(0))
            i += m.end()
            continue
        if tex[i] == "\\" and i + 1 < n:
            out.append(tex[i:i + 2])
            i += 2
            continue
        if tex.startswith("--", i):  # an en or em dash (TeX ligature)
            k = 3 if tex.startswith("---", i) else 2
            out.append("\\lr{%s}" % tex[i:i + k])
            i += k
            continue
        c = tex[i]
        out.append("\\lr{%s}" % c if c in FA_MISSING else c)
        i += 1
    return "".join(out)


def _skip_braced(s, i):
    depth = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return i
