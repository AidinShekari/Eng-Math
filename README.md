# Engineering Mathematics — Lecture Notes / جزوهٔ ریاضی مهندسی

Typeset lecture notes of the course *Engineering Mathematics* (Fourier analysis, partial differential
equations and the Laplace transform, complex analysis), in Persian (RTL) and English (LTR).

- **Instructor / استاد:** Abbas Ebrahimi Moghadam / عباس ابراهیمی مقدم
- **Compiled and edited by / جمع‌آوری و تنظیم:** Aidin Shekari / آیدین شکاری

The slides of the instructor determine the mathematics; the notes keep their order and notation.
Corrections and additions are listed in [REVIEW.md](REVIEW.md).

## Complete books / کتاب کامل
- [English](00-full-notes/en/EngineeringMath-en.pdf)
- [فارسی](00-full-notes/fa/EngineeringMath-fa.pdf)

## Chapters (English)
| # | Chapter | PDF |
|---|---|---|
| 01 | Fourier Series | [PDF](01-fourier-series/en/module01-fourier-series.pdf) |
| 02 | Properties of Fourier Series, Parseval's Theorem and the Complex Form | [PDF](02-fourier-properties/en/module02-fourier-properties.pdf) |
| 03 | The Fourier Integral | [PDF](03-fourier-integral/en/module03-fourier-integral.pdf) |
| 04 | The One-Dimensional Wave Equation and Separation of Variables | [PDF](04-wave-equation-1d/en/module04-wave-equation-1d.pdf) |
| 05 | d'Alembert's Method and the One-Dimensional Heat Equation | [PDF](05-heat-equation-1d/en/module05-heat-equation-1d.pdf) |
| 06 | Two-Dimensional Wave and Heat Equations: Rectangle and Disc | [PDF](06-pde-2d/en/module06-pde-2d.pdf) |
| 07 | The Laplace Transform | [PDF](07-laplace-transform/en/module07-laplace-transform.pdf) |
| 08 | Complex Numbers | [PDF](08-complex-numbers/en/module08-complex-numbers.pdf) |
| 09 | Complex Functions, the Derivative and the Cauchy–Riemann Conditions | [PDF](09-complex-functions/en/module09-complex-functions.pdf) |
| 10 | Elementary Complex Functions | [PDF](10-elementary-functions/en/module10-elementary-functions.pdf) |
| 11 | Linear Mappings | [PDF](11-linear-mappings/en/module11-linear-mappings.pdf) |
| 12 | Integration of Complex Functions | [PDF](12-complex-integration/en/module12-complex-integration.pdf) |
| 13 | Laurent Series, Singularities and Residues | [PDF](13-laurent-residues/en/module13-laurent-residues.pdf) |
| 14 | Evaluating Definite Integrals by Residues | [PDF](14-residue-integrals/en/module14-residue-integrals.pdf) |

## فصل‌ها (فارسی)
| # | فصل | PDF |
|---|---|---|
| 01 | سری فوریه | [PDF](01-fourier-series/fa/module01-fourier-series.pdf) |
| 02 | خواص سری فوریه، قضیهٔ پارسوال و صورت مختلط | [PDF](02-fourier-properties/fa/module02-fourier-properties.pdf) |
| 03 | انتگرال فوریه | [PDF](03-fourier-integral/fa/module03-fourier-integral.pdf) |
| 04 | معادلهٔ موجی یک‌بعدی و روش جداسازی متغیرها | [PDF](04-wave-equation-1d/fa/module04-wave-equation-1d.pdf) |
| 05 | روش دالامبر و معادلهٔ انتقال حرارت یک‌بعدی | [PDF](05-heat-equation-1d/fa/module05-heat-equation-1d.pdf) |
| 06 | معادلات دو‌بعدی موج و گرما: مستطیل و دایره | [PDF](06-pde-2d/fa/module06-pde-2d.pdf) |
| 07 | تبدیل لاپلاس | [PDF](07-laplace-transform/fa/module07-laplace-transform.pdf) |
| 08 | اعداد مختلط | [PDF](08-complex-numbers/fa/module08-complex-numbers.pdf) |
| 09 | توابع مختلط، مشتق و شرایط کشی–ریمان | [PDF](09-complex-functions/fa/module09-complex-functions.pdf) |
| 10 | توابع مختلط مقدماتی | [PDF](10-elementary-functions/fa/module10-elementary-functions.pdf) |
| 11 | نگاشت‌های خطی | [PDF](11-linear-mappings/fa/module11-linear-mappings.pdf) |
| 12 | انتگرال توابع مختلط | [PDF](12-complex-integration/fa/module12-complex-integration.pdf) |
| 13 | سری لورنت، نقاط تکین و مانده‌ها | [PDF](13-laurent-residues/fa/module13-laurent-residues.pdf) |
| 14 | محاسبهٔ انتگرال‌های معین به روش مانده‌ها | [PDF](14-residue-integrals/fa/module14-residue-integrals.pdf) |

## Build / ساخت
Needs `pandoc` ≥ 3 and XeLaTeX (`latexmk`, or `tectonic`) with TeX Gyre Termes, Heros and Termes Math; `scipy` only to regenerate the data figures.

```bash
python3 tools/build.py                 # everything
python3 tools/build.py --chapter 05    # one chapter, both languages
python3 tools/build.py --only fa       # one language
python3 tools/genfigs.py               # regenerate data-driven figures
```

Layout: `NN-slug/{fa,en}/moduleNN-slug.md` (source) → `.tex` → `.pdf`; `template/` holds the style,
fonts (Vazirmatn, OFL), figures (native TikZ/PGFPlots) and the chapter-opener motifs;
`tools/` holds the build scripts (md → LaTeX filter included).
