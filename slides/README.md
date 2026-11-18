# Slides / اسلایدها

Slide decks made from the lecture notes, one per language. The text, the formulas, the figures and
the order are those of the notes (`NN-slug/<lang>/content.tex`); nothing is summarised or rewritten.

| | PowerPoint | Beamer source |
|---|---|---|
| English | `EngineeringMath-slider-en.pptx` | `main-en.tex` + `en/*.tex` |

## Presenting
Every slide opens with its title (and, on an example or an exercise, its statement). Each press of
**Next** (pointer, → or Space) shows one more step: a paragraph, a formula with its lead-in, a
list item, a figure with its caption. After the last step the next press goes to the next slide.

* PowerPoint: entrance effect *Fade*, 0.25 s, *Start: On Click* for the first piece of a step,
  *With Previous* for the other pieces of the same step. No triggers, no automatic timings.
  The chapters are PowerPoint *sections*.
* Beamer: `\begin{uncoverenv}<n->` per step (the room of hidden steps is kept, so nothing moves).

A topic that needs more than one slide keeps its title, followed by «(ادامه)» / “(continued)”.

## Editing
Titles, text and captions are text boxes. Formulas are PowerPoint equations (OMML), each with a
picture of the same formula as the fallback for programs without equation support. A formula
that contains Persian words is a picture (PowerPoint equations do not shape Persian text), as is a
formula that could not be converted. Figures (TikZ) and tables are pictures.

## Building
```bash
python3 slides/tools/build_slides.py              # both languages: Beamer source + PowerPoint
python3 slides/tools/build_slides.py --lang fa --no-pptx
cd slides && xelatex main-fa.tex                  # or: tectonic main-fa.tex
python3 slides/tools/check_pptx.py slides/EngineeringMath-slider-fa.pptx 12 40   # titles and click order
```
Needs `tectonic`, `pandoc` ≥ 3, and the Python packages `python-pptx`, `pymupdf`, `lxml`, `pillow`.
Every piece is measured with XeLaTeX in the fonts of the PowerPoint file (Tahoma / Calibri /
Cambria Math, read from macOS and Microsoft Office) and in those of the Beamer deck (Vazirmatn /
TeX Gyre); the larger size decides the pagination, so both outputs share the same slides.
Compiling the Beamer source needs only the fonts of the repository (`template/fonts`) and TeX Gyre.
