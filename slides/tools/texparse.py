"""Parse the generated chapter bodies (NN-slug/{fa,en}/content.tex) into a block model.

The model keeps the order and the wording of the notes; nothing is summarised.

    Chapter(num, title, other_title, blocks)
    blocks: Heading(level, title) | Box(kind, title, groups) | Group(elements)
    Group: the elements of one paragraph group (text between blank lines)
    elements: Para(tex) | Disp(tex) | Fig(name, caption) | ListBlock(kind, items) | Table(tex)
"""
import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Para:
    tex: str
    kind: str = "para"


@dataclass
class Disp:
    tex: str
    kind: str = "disp"


@dataclass
class Fig:
    name: str
    caption: str
    kind: str = "fig"


@dataclass
class ListBlock:
    ordered: bool
    items: List[List[object]]  # each item: list of elements
    kind: str = "list"


@dataclass
class Table:
    tex: str
    kind: str = "table"


@dataclass
class Group:
    elements: List[object]
    unit: Optional[int] = None  # EMunit id (figures are laid out next to the text of their unit)
    kind: str = "group"


@dataclass
class Box:
    env: str  # EMtheorem, EMexample, ...
    title: str
    groups: List[Group]
    number: Optional[str] = None
    kind: str = "box"


@dataclass
class Heading:
    level: int  # 1 section, 2 subsection
    title: str
    kind: str = "heading"


@dataclass
class Chapter:
    num: int
    slug: str
    title: str
    blocks: List[object] = field(default_factory=list)
    sections: List[str] = field(default_factory=list)


BOX_ENVS = ["EMdefinition", "EMtheorem", "EMlemma", "EMproposition", "EMcorollary",
            "EMexample", "EMexercise", "EMremark", "EMimportant", "EMproof"]
NUMBERED = {"EMdefinition", "EMtheorem", "EMlemma", "EMproposition", "EMcorollary",
            "EMexample", "EMexercise", "EMimportant"}


def balanced(s: str, i: int):
    """s[i] == '{' ; return (content, index after the closing brace)."""
    assert s[i] == "{", s[i:i + 30]
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces: " + s[i:i + 80])


def skip_ws(s, i):
    while i < len(s) and s[i] in " \t\n":
        i += 1
    return i


def find_env_end(s: str, i: int, env: str):
    """index of the matching \\end{env} starting the search at i (handles nesting)."""
    depth = 1
    pat = re.compile(r"\\(begin|end)\{" + re.escape(env) + r"\}")
    for m in pat.finditer(s, i):
        depth += 1 if m.group(1) == "begin" else -1
        if depth == 0:
            return m.start(), m.end()
    raise ValueError("no end for " + env)


def parse_group_text(text: str) -> List[object]:
    """One paragraph group: text runs, \\EMdisp, \\EMfigure, lists, tables."""
    out = []
    buf = []
    i = 0

    def flush():
        t = "".join(buf).strip()
        buf.clear()
        if t:
            out.append(Para(t))

    while i < len(text):
        if text.startswith("\\EMdisp{", i):
            flush()
            body, i = balanced(text, i + len("\\EMdisp"))
            out.append(Disp(body.strip()))
            continue
        if text.startswith("\\EMfigure{", i):
            flush()
            name, i = balanced(text, i + len("\\EMfigure"))
            i = skip_ws(text, i)
            cap, i = balanced(text, i)
            out.append(Fig(name.strip(), " ".join(cap.split())))
            continue
        m = re.match(r"\\begin\{(itemize|enumerate)\}", text[i:])
        if m:
            flush()
            env = m.group(1)
            a = i + m.end()
            e0, e1 = find_env_end(text, a, env)
            out.append(parse_list(text[a:e0], env == "enumerate"))
            i = e1
            continue
        if text.startswith("\\begin{longtable}", i):
            flush()
            e0, e1 = find_env_end(text, i + len("\\begin{longtable}"), "longtable")
            out.append(Table(text[i:e1]))
            i = e1
            continue
        if text.startswith("\\Needspace", i):
            _, i = balanced(text, i + len("\\Needspace"))
            continue
        if text.startswith("\\tightlist", i):
            i += len("\\tightlist")
            continue
        buf.append(text[i])
        i += 1
    flush()
    return out


def parse_list(body: str, ordered: bool) -> ListBlock:
    body = body.replace("\\tightlist", "")
    # split on top-level \item
    parts = []
    depth = 0
    start = None
    i = 0
    while i < len(body):
        c = body[i]
        if c == "\\" and body.startswith("\\item", i) and depth == 0 and not body[i + 5:i + 6].isalpha():
            if start is not None:
                parts.append(body[start:i])
            start = i + 5
            i += 5
            continue
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    if start is not None:
        parts.append(body[start:])
    items = []
    for p in parts:
        p = p.strip()
        if p.startswith("[") and "]" in p:  # \item[label]
            p = p[p.index("]") + 1:]
        els = []
        for g in split_groups(p):
            els.extend(parse_group_text(g))
        items.append(els)
    return ListBlock(ordered, items)


def split_groups(text: str) -> List[str]:
    """Split on blank lines, but never inside braces or environments."""
    groups = []
    cur = []
    depth = 0
    env_depth = 0
    lines = text.split("\n")
    for ln in lines:
        if ln.strip() == "" and depth == 0 and env_depth == 0:
            if cur:
                groups.append("\n".join(cur))
                cur = []
            continue
        cur.append(ln)
        # track braces / environments across lines
        j = 0
        while j < len(ln):
            c = ln[j]
            if c == "\\":
                if ln.startswith("\\begin{", j):
                    env_depth += 1
                elif ln.startswith("\\end{", j):
                    env_depth -= 1
                j += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
    if cur:
        groups.append("\n".join(cur))
    return [g for g in groups if g.strip()]


SKIP_LINE = re.compile(r"^\s*(\\EMhold|\\begin\{EMjoin\}|\\end\{EMjoin\}|\\Needspace\{[^}]*\})\s*$")


def parse_content(tex: str, chapnum: int):
    blocks = []
    unit_id = 0
    in_unit = None
    i = 0
    n = len(tex)
    counter = 0
    pending = []  # raw text lines outside boxes, collected until a structural token

    def flush_pending():
        txt = "\n".join(pending)
        pending.clear()
        for g in split_groups(txt):
            els = parse_group_text(g)
            if els:
                blocks.append(Group(els, in_unit))

    lines_re = re.compile(r"\\(EMsection|EMsubsection)\{|\\begin\{(EM[a-z]+)\}|\\end\{(EMunit)\}|\\EMhold\b|\\(begin|end)\{EMjoin\}")
    while i < n:
        m = lines_re.search(tex, i)
        if not m:
            pending.append(tex[i:])
            break
        pending.append(tex[i:m.start()])
        if m.group(1):
            flush_pending()
            t1, j = balanced(tex, m.end() - 1)
            j = skip_ws(tex, j)
            _, j = balanced(tex, j)
            blocks.append(Heading(1 if m.group(1) == "EMsection" else 2, t1.strip()))
            i = j
            continue
        env = m.group(2)
        if env == "EMunit":
            flush_pending()
            unit_id += 1
            in_unit = unit_id
            i = m.end()
            continue
        if m.group(3) == "EMunit":
            flush_pending()
            in_unit = None
            i = m.end()
            continue
        if env == "EMjoin" or m.group(4):
            flush_pending()
            i = m.end()
            continue
        if env in BOX_ENVS:
            flush_pending()
            title, j = balanced(tex, m.end())
            e0, e1 = find_env_end(tex, j, env)
            body = tex[j:e0]
            number = None
            if env in NUMBERED:
                counter += 1
                number = f"{chapnum}.{counter}"
            groups = [Group(parse_group_text(g)) for g in split_groups(body)]
            groups = [g for g in groups if g.elements]
            blocks.append(Box(env, " ".join(title.split()), groups, number))
            i = e1
            continue
        if m.group(0).startswith("\\EMhold"):
            flush_pending()
            i = m.end()
            continue
        # some other \begin{EM...}: keep as text
        pending.append(m.group(0))
        i = m.end()
    flush_pending()
    return blocks


def chapter_title(module_tex: str):
    m = re.search(r"\\EMsetmodule\{(\d+)\}\{(.*?)\}\{(.*?)\}\n", module_tex)
    return int(m.group(1)), m.group(2), m.group(3)


def minitoc(module_tex: str):
    return re.findall(r"\\EMtocitem\{\d+\}\{(.*)\}", module_tex)
