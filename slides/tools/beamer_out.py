"""Write the Beamer source of a deck: slides/main-<lang>.tex and slides/<lang>/*.tex."""
import re
from pathlib import Path

import layout as L

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"


def esc_title(t):
    return t


def table_tex(tex):
    from build_slides import table_tex as tt
    return tt(tex)


def unit_tex(unit, slide, pager, narrow):
    out = []
    for k, e in enumerate(unit.els):
        if k:
            out.append(r"\vspace{3bp}")
        if e.kind == "para":
            out.append(r"\EMp{%s}" % e.tex)
        elif e.kind == "item":
            mark = r"%d." % e.index if e.ordered else r"\lr{\textbullet}"
            if slide["lang"] == "fa" and e.ordered:
                mark = L.num("fa", str(e.index)) + "."
            out.append(r"\EMitem{%s}{\dimexpr\linewidth-26bp\relax}{%s}" % (mark, e.tex))
        elif e.kind == "disp":
            w = pager_width(unit, e, narrow)
            lines = e.lines_by_w[w]
            body = r" \\[4pt] ".join(" ".join(e.segs[i] for i in ln) for ln in lines)
            key = "%s_l%s" % (e.jid, "-".join(str(len(x)) for x in lines))
            s = pager.S[key]
            sc = min(1.0, (w - 4) / s["wd"])
            if sc < 0.999:
                out.append(r"\EMeq[%.3f]{%s}" % (sc, body))
            else:
                out.append(r"\EMeq{%s}" % body)
        elif e.kind == "fig":
            if pager.fig_side(e):
                continue  # drawn in the side column
            sc = pager.fig_full_scale(e)
            out.append(r"\EMfigure{%.3f}{%s}{%s}" % (sc, e.name, e.tex))
        elif e.kind == "table":
            sc = pager.table_scale(e)
            out.append(r"{\EMbody\centering\scalebox{%.3f}{\parbox{%dbp}{%s}}\par}" % (sc, int(L.CW), table_tex(e.tex)))
    return "\n".join(x for x in out if x)


def pager_width(unit, e, narrow):
    from build_slides import widths_for
    return widths_for(unit, e)[1 if narrow else 0]


def content_frame(slide, pager, lang):
    title = slide["title"] + ((" " + L.LABELS[lang]["cont"]) if slide["cont"] else "")
    narrow = slide["narrow"]
    lines = []
    fs = title_fontsize(slide, pager, title)
    lines.append(tdef(fs))
    lines.append(r"\begin{frame}{%s}" % title)
    if slide.get("shrink", 1.0) < 0.999:
        lines.append(r"\EMshrink{%.3f}{" % slide["shrink"])
    if narrow:
        lines.append(r"\begin{minipage}[t]{%dbp}\vspace{0pt}" % int(L.NW))
    prev_box = None
    first = True
    for u, st in zip(slide["units"], slide["steps"]):
        if u.box is not prev_box:
            if prev_box is not None:
                lines.append(r"\end{EMbox}")
            elif not first:
                lines.append(r"\EMgap")
            if u.box is not None:
                head = ""
                if u.box.bid in slide["heads"]:
                    lab, t = u.box.head
                    if slide["lang"] == "fa":
                        lab = re.sub(r"([۰-۹0-9]+\.[۰-۹0-9]+)", r"\\lr{\\persianfont \1}", lab)
                    head = r"\textbf{%s}%s" % (lab, (r"\ \ \lr{|}\ \ " + t) if t else "")
                lines.append(r"\begin{EMbox}{%s}{%d}{%s}" % (u.box.kind, max(st, 1), head))
        elif not first:
            lines.append(r"\EMgap")
        body = unit_tex(u, slide, pager, narrow)
        if body:
            if st > 0:
                lines.append(r"\begin{uncoverenv}<%d->" % (st + 1))
                lines.append(body)
                lines.append(r"\end{uncoverenv}")
            else:
                lines.append(body)
        prev_box = u.box
        first = False
    if prev_box is not None:
        lines.append(r"\end{EMbox}")
    if narrow:
        lines.append(r"\end{minipage}")
        for it in slide["items"]:
            if it["kind"] == "fig":
                e = it["el"]
                off = it["y"] - L.CY0
                st = it["step"]
                fig = r"\EMfigure{%.3f}{%s}{%s}" % (it["scale"], e.name, e.tex)
                if st > 0:
                    fig = r"\uncover<%d->{%s}" % (st + 1, fig)
                lines.append(r"\EMside{%.1fbp}{%s}" % (off, fig))
    if slide.get("shrink", 1.0) < 0.999:
        lines.append("}")
    lines.append(r"\end{frame}")
    return "\n".join(lines)


def tdef(size):
    return r"\def\EMtitlesize{%d}\def\EMtitleskip{%d}" % (size, round(size * 1.2))


def title_fontsize(slide, pager, title):
    size, two = L.title_style(pager.deck.title_w.get(title))
    return size


def cover_frame(deck):
    c = deck.cover if hasattr(deck, "cover") else None
    s = deck.slides[0]["cover"]
    course, subtitle, other, other_sub = s
    rtl = deck.lang == "fa"
    title, sub, sec = course, subtitle, other  # the cover of the notes of this language
    who = (r"استاد: عباس ابراهیمی مقدم \quad\textbullet\quad جمع‌آوری و تنظیم: آیدین شکاری" if rtl else
           r"Instructor: Abbas Ebrahimi Moghadam \quad\textbullet\quad Compiled by: Aidin Shekari")
    uni = r"دانشگاه فردوسی مشهد" if rtl else "Ferdowsi University of Mashhad"
    sec_t = (r"\lr{%s}" % sec) if rtl else (r"\rl{%s}" % sec)
    return r"""\begin{frame}[plain]
\begin{tikzpicture}[remember picture,overlay]
\node at ([yshift=-80bp]current page.north) {\includegraphics[height=78bp]{\EMroot/ferdowsi-logo.png}};
\node[fill=SLbar,draw=SLbarEdge,line width=0.8bp,rounded corners=4bp,minimum width=640bp,minimum height=190bp] (b) at ([yshift=-262bp]current page.north) {};
\node[text=SLtitle,font=\bfseries\fontsize{40}{48}\selectfont] at ([yshift=52bp]b.center) {\EMdir{%s}};
\node[text=SLdef,font=\fontsize{20}{26}\selectfont,text width=600bp,align=center] at ([yshift=-4bp]b.center) {\EMdir{%s}};
\node[text=EMmuted,font=\fontsize{18}{22}\selectfont] at ([yshift=-58bp]b.center) {\EMdir{%s}};
\node[text=EMink,font=\fontsize{16}{20}\selectfont] at ([yshift=-410bp]current page.north) {\EMdir{%s}};
\node[text=EMmuted,font=\fontsize{14}{18}\selectfont] at ([yshift=-440bp]current page.north) {\EMdir{%s}};
\end{tikzpicture}
\end{frame}""" % (title, sub, sec_t, who, uni)


def part_frame(slide, lang):
    numeral, title, first, rng = slide["part"]
    return tdef(L.TITLE) + r"""
\begin{frame}{%s}
\begin{tikzpicture}[remember picture,overlay]
\node[fill=SLbar,draw=SLbarEdge,line width=0.8bp,rounded corners=4bp,minimum width=520bp,minimum height=170bp] (b) at ([yshift=-20bp]current page.center) {};
\node[text=SLthm,font=\bfseries\fontsize{30}{36}\selectfont] at ([yshift=36bp]b.center) {\EMdir{%s}};
\node[text=SLdef,font=\fontsize{24}{30}\selectfont] at ([yshift=-30bp]b.center) {\EMdir{%s}};
\end{tikzpicture}
\end{frame}""" % (slide["title"], slide["title"], title)


def chapter_frame(slide, lang):
    ch = slide["ch"]
    items = "\n".join(r"\EMitem{\lr{\textbullet}}{\dimexpr\linewidth-26bp\relax}{%s}" % t for t in ch.sections)
    return tdef(title_fontsize(slide, deck_pager[0], slide["title"])) + r"""
\begin{frame}{%s}
{\fontsize{20}{26}\selectfont\bfseries\color{SLdef}\EMalign %s\par}
\vspace{10bp}
%s
\end{frame}""" % (slide["title"], L.LABELS[lang]["contents"], items)


deck_pager = [None]


def write(deck):
    lang = deck.lang
    deck_pager[0] = deck.pager
    outdir = SLIDES / lang
    outdir.mkdir(exist_ok=True)
    for f in outdir.glob("*.tex"):
        f.unlink()
    pager = deck.pager
    files = []
    cur = []
    curname = "front"
    chap_title = {ch.num: ch.title for ch in deck.chapters}

    def flush(name, frames):
        if frames:
            (outdir / (name + ".tex")).write_text("\n\n".join(frames) + "\n", encoding="utf-8")
            files.append(name)

    for s in deck.slides:
        s["lang"] = lang
        if s["kind"] in ("part", "chapter") and s["chapter"] != (cur and cur[0][0]):
            pass
        if s["kind"] == "part" or (s["kind"] == "chapter" and not (cur and cur[-1][1] == "part")):
            flush(curname, [f for _, _, f in cur])
            cur = []
            curname = "ch%02d" % s["chapter"]
        if s["kind"] == "cover":
            fr = cover_frame(deck)
        elif s["kind"] == "part":
            fr = part_frame(s, lang)
        elif s["kind"] == "chapter":
            foot = L.LABELS[lang]["chapter"] + " " + L.num(lang, str(s["chapter"])) + r" \ \textbullet\ " + chap_title[s["chapter"]]
            fr = (r"\section{%s}" % chap_title[s["chapter"]]) + "\n" + r"\def\EMfootchapter{%s}" % foot + "\n" + chapter_frame(s, lang)
        else:
            fr = content_frame(s, pager, lang)
        if lang == "fa":  # B Nazanin has no bullet: take it from the Latin font
            fr = re.sub(r"(?<!\\lr\{)\\textbullet", r"\\lr{\\textbullet}", fr)
        cur.append((s["chapter"], s["kind"], fr))
    flush(curname, [f for _, _, f in cur])
    rtl = lang == "fa"
    main = [r"% !TEX program = xelatex",
            "% Engineering Mathematics — slides (" + ("Persian" if rtl else "English") + ").  Generated by tools/build_slides.py from the",
            "% chapter bodies NN-slug/" + lang + "/content.tex; compile with XeLaTeX (or tectonic) from this folder.",
            r"% Every click shows one step: \begin{uncoverenv}<n-> keeps the room of what is still hidden.",
            r"\documentclass[t,12pt]{beamer}",
            r"\newif\ifEMrtl " + (r"\EMrtltrue" if rtl else r"\EMrtlfalse"),
            r"\def\EMroot{../template}",
            r"\def\EMslidefonts{fonts/}",
            (r"\def\EMfigdir{figures-fa}" if rtl else ""),
            r"\input{em-slides-common}",
            (r"\usepackage{xepersian}" if rtl else r"\usepackage{fontspec}\newfontfamily\persianfont[Path=\EMslidefonts,Script=Arabic]{BNazanin.ttf}\TeXXeTstate=1 \newcommand{\lr}[1]{#1}\newcommand{\rl}[1]{{\persianfont\beginR #1\endR}}"),
            r"\input{em-fonts-%s}" % lang,
            r"\input{em-beamer}",
            r"\title{%s}" % ("ریاضی مهندسی" if rtl else "Engineering Mathematics"),
            r"\begin{document}",
            r"\def\EMfootchapter{%s}" % ("ریاضی مهندسی" if rtl else "Engineering Mathematics")]
    main += [r"\input{%s/%s}" % (lang, f) for f in files]
    main.append(r"\end{document}")
    (SLIDES / f"main-{lang}.tex").write_text("\n".join(main) + "\n", encoding="utf-8")
