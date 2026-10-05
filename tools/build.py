#!/usr/bin/env python3
"""Build the Engineering Mathematics lecture notes.

Layout (one folder per chapter, languages inside):
  NN-slug/{fa,en}/moduleNN-slug.md        source (Markdown + $maths$)
  NN-slug/{fa,en}/content.tex             generated body
  NN-slug/{fa,en}/moduleNN-slug.tex       standalone chapter  → .pdf
  00-full-notes/{fa,en}/                  the complete book
  template/figures/<name>.tex             drawings (```{.figure #name} in the sources)

Usage:  python3 tools/build.py [--no-pdf] [--only fa|en] [--chapter 05] [--book-only]
Needs:  pandoc >= 3 and XeLaTeX (latexmk, or tectonic) with TeX Gyre Termes / Heros / Termes Math.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILTER = ROOT / "tools" / "md2tex.lua"
PANDOC_FROM = "markdown+fenced_divs-auto_identifiers-implicit_figures-superscript-subscript-strikeout"
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
BOOK = "EngineeringMath"

# the three parts follow the three sets of slides
PARTS = [
    ("1", {"fa": "۱", "en": "I"},
     {"fa": "تحلیل فوریه", "en": "Fourier Analysis"}, 1, 3),
    ("2", {"fa": "۲", "en": "II"},
     {"fa": "معادلات دیفرانسیل با مشتقات جزئی", "en": "Partial Differential Equations"}, 4, 7),
    ("3", {"fa": "۳", "en": "III"},
     {"fa": "آنالیز مختلط", "en": "Complex Analysis"}, 8, 14),
]
COVER_SUBTITLE = {
    "fa": "تحلیل فوریه \\ \\textbullet\\ معادلات دیفرانسیل با مشتقات جزئی \\ \\textbullet\\ آنالیز مختلط",
    "en": "Fourier Analysis \\ \\textbullet\\ Partial Differential Equations \\ \\textbullet\\ Complex Analysis",
}
COURSE = {"fa": "ریاضی مهندسی", "en": "Engineering Mathematics"}
COURSE_NOTES = {"fa": "جزوهٔ کامل درس", "en": "Complete Lecture Notes"}


def md_title(md: Path):
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md.stem


_INLINE = {}


def inline_tex(text: str, lang: str) -> str:
    """A title rendered by the filter (inline maths, Latin runs in Persian)."""
    key = (text, lang)
    if key not in _INLINE:
        env = dict(os.environ, EM_LANG=lang, EM_FIGDIR=str(ROOT / "template" / "figures"))
        # a heading-less rendering: wrap the title in a paragraph
        tex = subprocess.run(
            ["pandoc", "-f", PANDOC_FROM, "-t", "latex", "--wrap=none",
             "--lua-filter", str(FILTER)],
            input=text, check=True, capture_output=True, text=True, env=env).stdout
        _INLINE[key] = tex.strip()
    return _INLINE[key]


def pandoc_body(md: Path, lang: str) -> str:
    env = dict(os.environ, EM_LANG=lang, EM_FIGDIR=str(ROOT / "template" / "figures"))
    tex = subprocess.run(
        ["pandoc", "-f", PANDOC_FROM, "-t", "latex", "--wrap=preserve",
         "--lua-filter", str(FILTER), str(md)],
        check=True, capture_output=True, text=True, env=env).stdout
    return postprocess(tex, lang)


def postprocess(tex: str, lang: str) -> str:
    """Tables: centred, in the house style; lists: compact."""
    tex = tex.replace("\\begin{longtable}[]", "\\begin{longtable}[c]")
    tex = tex.replace("\\toprule\\noalign{}\n", "\\toprule\\noalign{}\n\\rowcolor{EMindigoL}")
    # short tables never split across pages
    def keep(m):
        rows = m.group(0).count("\\\\\n")
        need = min(int(rows * 1.8) + 3, 22)
        return f"\\Needspace{{{need}\\baselineskip}}\n" + m.group(0)
    tex = re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", keep, tex, flags=re.S)
    return tex


def section_list(body: str):
    """The titles of the numbered sections of a generated body, in order."""
    out = []
    for line in body.splitlines():
        m = re.match(r"\\EMsection\{(.*)\}\{[^{}]*\}\s*$", line)
        if m:
            out.append(m.group(1))
    return out


def minitoc(titles):
    items = "".join(f"\\EMtocitem{{{i}}}{{{t}}}\n" for i, t in enumerate(titles, 1))
    return f"\\begin{{EMminitoc}}\n{items}\\end{{EMminitoc}}\n"


def main_file(lang, preamble_extra, body):
    return (
        "% !TEX program = xelatex\n"
        f"% Engineering Mathematics — lecture notes ({'Persian' if lang == 'fa' else 'English'})\n"
        "% Instructor: Abbas Ebrahimi Moghadam — compiled and edited by Aidin Shekari.\n"
        "% Compile with XeLaTeX (or tectonic) from this folder.\n"
        "\\documentclass[11pt]{article}\n"
        "\\def\\EMroot{../../template}\n"
        f"\\input{{\\EMroot/em-{lang}}}\n"
        f"{preamble_extra}"
        "\\begin{document}\n"
        f"{body}"
        "\\end{document}\n")


def num(n, lang):
    return str(n).translate(FA_DIGITS) if lang == "fa" else str(n)


def chapter_dirs():
    for topic in sorted(ROOT.glob("[0-9][0-9]-*")):
        n, slug = topic.name.split("-", 1)
        if n != "00":
            yield int(n), n, slug, topic


def build_sources(lang, only=None, book_only=False):
    other = "en" if lang == "fa" else "fa"
    texs, chapters = [], {}
    for n, nn, slug, topic in chapter_dirs():
        md = topic / lang / f"module{nn}-{slug}.md"
        if not md.exists():
            continue
        title = inline_tex(md_title(md), lang)
        other_md = topic / other / md.name
        other_title = inline_tex(md_title(other_md), other) if other_md.exists() else ""
        folder = md.parent
        skip = book_only or bool(only and nn != only)
        if skip and (folder / "content.tex").exists():
            body = (folder / "content.tex").read_text(encoding="utf-8")
        else:
            body = pandoc_body(md, lang)
            (folder / "content.tex").write_text(body, encoding="utf-8")
        secs = section_list(body)
        chapters[n] = (title, other_title, folder, secs)
        if skip:
            continue
        (folder / f"{md.stem}.tex").write_text(main_file(
            lang, f"\\EMsetmodule{{{n}}}{{{title}}}{{{other_title}}}\n",
            f"\\EMchapterpage{{{n}}}{{{n}}}{{{title}}}{{{other_title}}}\n"
            f"{minitoc(secs)}\\EMchapterend\n\\input{{content}}\n"), encoding="utf-8")
        texs.append(folder / f"{md.stem}.tex")

    if not only:
        folder = ROOT / "00-full-notes" / lang
        folder.mkdir(parents=True, exist_ok=True)
        parts = [f"\\EMcoverpage{{{COURSE[lang]}}}{{{COVER_SUBTITLE[lang]}}}{{{COURSE[other]}}}\n",
                 "\\pagenumbering{roman}\\setcounter{page}{1}\n\\EMcolophon\n"]
        # contents
        toc = ["\\EMsetmodule{0}{\\EMlangContents}{}\n\\begin{EMbooktoc}\n"]
        for pk, pnum, ptitle, lo, hi in PARTS:
            toc.append(f"\\EMtocpart{{{pnum[lang]}}}{{{ptitle[lang]}}}\n")
            for n in range(lo, hi + 1):
                if n not in chapters:
                    continue
                title, _, _, secs = chapters[n]
                toc.append(f"\\EMtocchapter{{{n}}}{{{num(n, lang)}}}{{{title}}}\n")
                for i, t in enumerate(secs, 1):
                    toc.append(f"\\EMtocitemk{{{n}}}{{{i}}}{{{num(n, lang)}.{num(i, lang)}}}{{{t}}}\n")
        toc.append("\\end{EMbooktoc}\n")
        parts.append("".join(toc))
        parts.append("\\clearpage\\pagenumbering{arabic}\\setcounter{page}{1}\n")
        for pk, pnum, ptitle, lo, hi in PARTS:
            rng = (f"فصل‌های {num(lo, lang)} تا {num(hi, lang)}" if lang == "fa"
                   else f"Chapters {lo}--{hi}")
            parts.append(f"\\EMpartpage{{{pk}}}{{{pnum[lang]}}}{{{ptitle[lang]}}}"
                         f"{{{ptitle[other]}}}{{{rng}}}\n")
            for n in range(lo, hi + 1):
                if n not in chapters:
                    continue
                title, other_title, cfolder, secs = chapters[n]
                rel = cfolder.relative_to(ROOT).as_posix()
                parts.append(f"\\EMsetmodule{{{n}}}{{{title}}}{{{other_title}}}\n"
                             f"\\EMchapterpage{{{n}}}{{{n}}}{{{title}}}{{{other_title}}}\n"
                             f"{minitoc(secs)}\\EMchapterend\n\\input{{../../{rel}/content}}\n")
        name = f"{BOOK}-{lang}"
        (folder / f"{name}.tex").write_text(main_file(lang, "", "".join(parts)), encoding="utf-8")
        texs.append(folder / f"{name}.tex")
    return texs


def compile_tex(tex: Path):
    if shutil.which("latexmk"):
        cmd = ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", tex.name]
    else:
        cmd = ["tectonic", "--keep-logs", "--chatter", "minimal", tex.name]
    r = subprocess.run(cmd, cwd=tex.parent, capture_output=True, text=True)
    log = tex.with_suffix(".log")
    missing, overfull, undef, underfull = set(), 0, 0, 0
    if log.exists():
        text = log.read_text(errors="replace")
        missing = set(re.findall(r"Missing character: There is no (.) ", text))
        big = [float(x) for x in re.findall(r"^Overfull \\hbox \((\d+\.\d+)pt", text, flags=re.M)]
        overfull = sum(1 for x in big if x > 2.0)
        undef = len(re.findall(r"Reference `[^']*' on page \d+ undefined", text))
    status = "ok" if r.returncode == 0 else "FAILED"
    msg = f"[{status}] {tex.relative_to(ROOT)}"
    if overfull:
        msg += f"  overfull>2pt: {overfull}"
    if undef:
        msg += f"  undefined refs: {undef}"
    if missing:
        msg += f"  missing glyphs: {''.join(sorted(missing))}"
    if r.returncode != 0:
        msg += "\n" + (r.stderr + r.stdout)[-3000:]
    return r.returncode == 0, msg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-pdf", action="store_true", help="generate the .tex files only")
    ap.add_argument("--only", choices=["fa", "en"], help="one language")
    ap.add_argument("--chapter", help="one chapter, e.g. 05 (the book is not rebuilt)")
    ap.add_argument("--book-only", action="store_true", help="only the complete book")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    texs = []
    for lang in ([a.only] if a.only else ["fa", "en"]):
        texs += build_sources(lang, a.chapter, a.book_only)
    print(f"generated {len(texs)} LaTeX files")
    if a.no_pdf:
        return
    ok = True
    with ThreadPoolExecutor(a.jobs) as ex:
        for good, msg in ex.map(compile_tex, texs):
            ok &= good
            print(msg, flush=True)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
