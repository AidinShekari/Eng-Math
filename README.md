# Engineering Mathematics — Lecture Notes / جزوهٔ ریاضی مهندسی

Typeset lecture notes of the course *Engineering Mathematics* (complex analysis, Fourier analysis,
partial differential equations and the Laplace transform), in Persian (RTL) and English (LTR).

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
| 01 | Complex Numbers | [PDF](01-complex-numbers/en/module01-complex-numbers.pdf) |
| 02 | Complex Functions, the Derivative and the Cauchy–Riemann Conditions | [PDF](02-complex-functions/en/module02-complex-functions.pdf) |
| 03 | Elementary Complex Functions | [PDF](03-elementary-functions/en/module03-elementary-functions.pdf) |
| 04 | Linear Mappings | [PDF](04-linear-mappings/en/module04-linear-mappings.pdf) |
| 05 | Integration of Complex Functions | [PDF](05-complex-integration/en/module05-complex-integration.pdf) |
| 06 | Laurent Series, Singularities and Residues | [PDF](06-laurent-residues/en/module06-laurent-residues.pdf) |
| 07 | Evaluating Definite Integrals by Residues | [PDF](07-residue-integrals/en/module07-residue-integrals.pdf) |
| 08 | Fourier Series | [PDF](08-fourier-series/en/module08-fourier-series.pdf) |
| 09 | Properties of Fourier Series, Parseval's Theorem and the Complex Form | [PDF](09-fourier-properties/en/module09-fourier-properties.pdf) |
| 10 | The Fourier Integral | [PDF](10-fourier-integral/en/module10-fourier-integral.pdf) |
| 11 | The One-Dimensional Wave Equation and Separation of Variables | [PDF](11-wave-equation-1d/en/module11-wave-equation-1d.pdf) |
| 12 | d'Alembert's Method and the One-Dimensional Heat Equation | [PDF](12-heat-equation-1d/en/module12-heat-equation-1d.pdf) |
| 13 | Two-Dimensional Wave and Heat Equations: Rectangle and Disc | [PDF](13-pde-2d/en/module13-pde-2d.pdf) |
| 14 | The Laplace Transform | [PDF](14-laplace-transform/en/module14-laplace-transform.pdf) |

## فصل‌ها (فارسی)
| # | فصل | PDF |
|---|---|---|
| 01 | اعداد مختلط | [PDF](01-complex-numbers/fa/module01-complex-numbers.pdf) |
| 02 | توابع مختلط، مشتق و شرایط کشی–ریمان | [PDF](02-complex-functions/fa/module02-complex-functions.pdf) |
| 03 | توابع مختلط مقدماتی | [PDF](03-elementary-functions/fa/module03-elementary-functions.pdf) |
| 04 | نگاشت‌های خطی | [PDF](04-linear-mappings/fa/module04-linear-mappings.pdf) |
| 05 | انتگرال توابع مختلط | [PDF](05-complex-integration/fa/module05-complex-integration.pdf) |
| 06 | سری لورنت، نقاط تکین و مانده‌ها | [PDF](06-laurent-residues/fa/module06-laurent-residues.pdf) |
| 07 | محاسبهٔ انتگرال‌های معین به روش مانده‌ها | [PDF](07-residue-integrals/fa/module07-residue-integrals.pdf) |
| 08 | سری فوریه | [PDF](08-fourier-series/fa/module08-fourier-series.pdf) |
| 09 | خواص سری فوریه، قضیهٔ پارسوال و صورت مختلط | [PDF](09-fourier-properties/fa/module09-fourier-properties.pdf) |
| 10 | انتگرال فوریه | [PDF](10-fourier-integral/fa/module10-fourier-integral.pdf) |
| 11 | معادلهٔ موجی یک‌بعدی و روش جداسازی متغیرها | [PDF](11-wave-equation-1d/fa/module11-wave-equation-1d.pdf) |
| 12 | روش دالامبر و معادلهٔ انتقال حرارت یک‌بعدی | [PDF](12-heat-equation-1d/fa/module12-heat-equation-1d.pdf) |
| 13 | معادلات دو‌بعدی موج و گرما: مستطیل و دایره | [PDF](13-pde-2d/fa/module13-pde-2d.pdf) |
| 14 | تبدیل لاپلاس | [PDF](14-laplace-transform/fa/module14-laplace-transform.pdf) |

## Build / ساخت
Needs `pandoc` ≥ 3 and `tectonic` (XeLaTeX); `scipy` only to regenerate the data figures.

```bash
python3 tools/build.py                 # everything
python3 tools/build.py --chapter 05    # one chapter, both languages
python3 tools/build.py --only fa       # one language
python3 tools/genfigs.py               # regenerate data-driven figures
```

Layout: `NN-slug/{fa,en}/moduleNN-slug.md` (source) → `.tex` → `.pdf`; `template/` holds the style,
fonts (Vazirmatn, OFL), figures (native TikZ/PGFPlots) and the chapter-opener motifs;
`tools/` holds the build scripts (md → LaTeX filter included).
