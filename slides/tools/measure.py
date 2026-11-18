"""Measuring runs: typeset every piece once with XeLaTeX (tectonic) and read its size back.

A run gets a list of jobs (id, kind, width, tex).  Every job becomes one page of a PDF whose
size is the size of the box, and one line of sizes.txt:  id|wd|ht|dp  (in pt).
kind:  'hmath'  display maths on one line, natural width
       'para'   text at the given width
       'eq'     several display lines, centred (\\\\ separated)
       'fig'    a figure, natural size
       'raw'    any material in an hbox (tables, headings)
"""
import hashlib
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"
WORD_FONTS = "/Applications/Microsoft Word.app/Contents/Resources/DFonts/"
SYS_FONTS = "/System/Library/Fonts/Supplemental/"

# font set-ups.  'pptx' = the fonts the PowerPoint files name (Tahoma / Calibri / Cambria Math);
# 'beamer' = the fonts of the Beamer decks (those of the notes: Vazirmatn, TeX Gyre).
FONTS = {
    ("fa", "pptx"): r"""
\settextfont[Path=%(sys)s,BoldFont={Tahoma Bold.ttf}]{Tahoma.ttf}
\setlatintextfont[Path=%(sys)s,BoldFont={Tahoma Bold.ttf},ItalicFont={Tahoma.ttf},ItalicFeatures={FakeSlant=0.2}]{Tahoma.ttf}
\setmathfont[Path=%(word)s,FontIndex=1]{Cambria.ttc}
\def\EMlead{1.207}""",
    ("en", "pptx"): r"""
\setmainfont[Path=%(word)s,BoldFont=Calibrib.ttf,ItalicFont=Calibrii.ttf,BoldItalicFont=Calibriz.ttf]{Calibri.ttf}
\setmathfont[Path=%(word)s,FontIndex=1]{Cambria.ttc}
\def\EMlead{1.221}""",
    ("fa", "beamer"): None,  # filled from slides/em-fonts-*.tex
    ("en", "beamer"): None,
}


def font_block(lang, mode):
    if mode == "beamer":
        return (SLIDES / f"em-fonts-{lang}.tex").read_text(encoding="utf-8")
    return FONTS[(lang, mode)] % {"sys": SYS_FONTS, "word": WORD_FONTS}


def preamble(lang, mode):
    rtl = lang == "fa"
    p = [r"\documentclass{article}", r"\newif\ifEMrtl " + (r"\EMrtltrue" if rtl else r"\EMrtlfalse"),
         r"\def\EMroot{" + str(ROOT / "template") + "}",
         r"\input{" + str(SLIDES / "em-slides-common") + "}"]
    if rtl:
        p.append(r"\usepackage{xepersian}")
    else:
        p.append(r"\usepackage{fontspec}\newfontfamily\persianfont[Path=\EMroot/fonts/,Extension=.ttf,Script=Arabic]{Vazirmatn-Regular}\TeXXeTstate=1 \newcommand{\lr}[1]{#1}\newcommand{\rl}[1]{{\persianfont\beginR #1\endR}}")
    p.append(font_block(lang, mode))
    p.append(r"""
\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}
\newwrite\EMsz \immediate\openout\EMsz=sizes.txt
\newcommand{\EMbody}{\fontsize{18}{\EMlead\dimexpr18pt\relax}\selectfont}
\newcommand{\EMship}[1]{%
  \immediate\write\EMsz{#1|\the\wd0|\the\ht0|\the\dp0}%
  \pdfpagewidth=\wd0 \pdfpageheight=\dimexpr\ht0+\dp0\relax
  \ifdim\pdfpageheight<1pt \pdfpageheight=1pt\fi\ifdim\pdfpagewidth<1pt \pdfpagewidth=1pt\fi
  \shipout\vbox{\box0}}
\newcommand{\EMjobhmath}[2]{\setbox0\hbox{\EMbody\ifEMrtl\beginL\fi$\displaystyle#2$\ifEMrtl\endL\fi}\EMship{#1}}
\newcommand{\EMjobpara}[5]{% id, width, align (l/r/c), size, text
  \setbox0\vbox{\hsize=#2\relax\fontsize{#4}{\EMlead\dimexpr#4pt\relax}\selectfont
    \if#3c\centering\else\ifEMrtl\raggedleft\else\raggedright\fi\fi
    \strut#5\strut\par}\EMship{#1}}
\newcommand{\EMjobeq}[2]{% id, lines
  \setbox0\hbox{\EMbody\ifEMrtl\beginL\fi$\displaystyle\begin{gathered}#2\end{gathered}$\ifEMrtl\endL\fi}\EMship{#1}}
\newcommand{\EMjobfig}[2]{\setbox0\hbox{\EMfig{#2}}\EMship{#1}}
\newcommand{\EMjobraw}[2]{\setbox0\hbox{\EMbody#2}\EMship{#1}}
\newcommand{\EMjobvraw}[3]{\setbox0\vbox{\hsize=#2\relax\EMbody#3\par}\EMship{#1}}
\hoffset=-1in \voffset=-1in
\begin{document}
""")
    return "\n".join(p)


def job_tex(job):
    jid, kind, width, tex = job[:4]
    align = job[4] if len(job) > 4 else "r"
    size = job[5] if len(job) > 5 else 18
    if kind == "hmath":
        return r"\EMjobhmath{%s}{%s}" % (jid, tex)
    if kind == "para":
        return r"\EMjobpara{%s}{%.2fpt}{%s}{%s}{%s}" % (jid, width, align, size, tex)
    if kind == "eq":
        return r"\EMjobeq{%s}{%s}" % (jid, tex)
    if kind == "fig":
        return r"\EMjobfig{%s}{%s}" % (jid, tex)
    if kind == "raw":
        return r"\EMjobraw{%s}{%s}" % (jid, tex)
    if kind == "vraw":
        return r"\EMjobvraw{%s}{%.2fpt}{%s}" % (jid, width, tex)
    raise ValueError(kind)


def run(jobs, lang, mode, workdir: Path, tag: str):
    """Returns ({id: (wd, ht, dp)}, pdf path, {id: page index})."""
    src = preamble(lang, mode) + "\n".join(job_tex(j) for j in jobs) + "\n\\end{document}\n"
    h = hashlib.sha1(src.encode()).hexdigest()[:12]
    d = workdir / f"{tag}-{lang}-{mode}"
    d.mkdir(parents=True, exist_ok=True)
    pdf = d / "m.pdf"
    stamp = d / "hash"
    if not (pdf.exists() and stamp.exists() and stamp.read_text() == h):
        (d / "m.tex").write_text(src, encoding="utf-8")
        r = subprocess.run(["tectonic", "-Z", "continue-on-errors", "--keep-logs", "m.tex"],
                           cwd=d, capture_output=True, text=True)
        if not pdf.exists():
            print(r.stdout[-3000:], r.stderr[-3000:])
            raise SystemExit("measuring run failed: " + str(d))
        stamp.write_text(h)
    sizes = {}
    pages = {}
    for k, line in enumerate((d / "sizes.txt").read_text(encoding="utf-8").splitlines()):
        jid, wd, ht, dp = line.split("|")
        sizes[jid] = (float(wd[:-2]), float(ht[:-2]), float(dp[:-2]))
        pages[jid] = k
    return sizes, pdf, pages
