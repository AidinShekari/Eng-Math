#!/usr/bin/env python3
"""Figures whose curves come from special functions that PGFPlots cannot evaluate.

The values are computed here from the defining functions (scipy.special) and written as
plain coordinate lists into template/figures/*.tex; everything else about the figures is
ordinary PGFPlots.  Re-run only if a figure needs to change:   python3 tools/genfigs.py
"""
from pathlib import Path
import numpy as np
from scipy import special

OUT = Path(__file__).resolve().parent.parent / "template" / "figures"


def coords(x, y, fmt="{:.4f}"):
    return " ".join(f"({fmt.format(a)},{fmt.format(b)})" for a, b in zip(x, y))


def write(name, text):
    (OUT / f"{name}.tex").write_text(text, encoding="utf-8")


# --- Si(u) and sin(u)/u -------------------------------------------------------------------
u = np.linspace(-20, 20, 801)
si = special.sici(u)[0]
sinc = np.sinc(u / np.pi)
write("m10-si", rf"""% Si(u) = integral of sin(w)/w from 0 to u (solid) and sin(u)/u (dashed); values from scipy.special.sici
\begin{{tikzpicture}}
  \begin{{axis}}[EMplot,width=11.5cm,height=5.2cm,xmin=-20,xmax=20,ymin=-1.9,ymax=1.9,
      xtick={{-20,-10,10,20}},ytick={{-1.571,1.571}},yticklabels={{$-\pi/2$,$\pi/2$}},
      xlabel={{$u$}},clip=false]
    \draw[EMdash] (axis cs:-20,1.5708)--(axis cs:20,1.5708);\draw[EMdash] (axis cs:-20,-1.5708)--(axis cs:20,-1.5708);
    \addplot[EMcurve2,dashed,thick,line width=0.8pt] coordinates{{{coords(u, sinc)}}};
    \addplot[EMcurve,line width=1.3pt] coordinates{{{coords(u, si)}}};
  \end{{axis}}
\end{{tikzpicture}}
""")

# --- the error function ------------------------------------------------------------------
x = np.linspace(-2, 2, 201)
write("m12-erf", rf"""% The error function; values from scipy.special.erf
\begin{{tikzpicture}}
  \begin{{axis}}[EMplot,width=10cm,height=5.4cm,xmin=-2.2,xmax=2.4,ymin=-1.25,ymax=1.25,
      xtick={{-2,-1,1,2}},ytick={{-1,-0.5,0.5,1}},xlabel={{$x$}},ylabel={{$\operatorname{{erf}}\,x$}}]
    \draw[EMdash] (axis cs:-2.2,1)--(axis cs:2.4,1);\draw[EMdash] (axis cs:-2.2,-1)--(axis cs:2.4,-1);
    \addplot[EMcurve,line width=1.3pt] coordinates{{{coords(x, special.erf(x))}}};
  \end{{axis}}
\end{{tikzpicture}}
""")

# --- heat on an infinite rod: u(x,t) for a pulse U0 = 100, c = 1 ---------------------------
x = np.linspace(-3, 3, 241)
curves = []
styles = {0: "EMcurve", 0.125: "EMcurve", 0.5: "EMcurve2", 1: "EMcurve3", 2: "EMcurve2", 8: "EMcurve3"}
dash = {0: "", 0.125: "", 0.5: "", 1: "dashed", 2: "densely dotted", 8: "dashed"}
lab = {0.125: r"$t=\tfrac18$", 0.5: r"$t=\tfrac12$", 1: r"$t=1$", 2: r"$t=2$", 8: r"$t=8$"}
body = ""
for t in (0.125, 0.5, 1, 2, 8):
    s = 2 * np.sqrt(t)
    ux = 50 * (special.erf((1 + x) / s) + special.erf((1 - x) / s))
    body += f"    \\addplot[{styles[t]},{dash[t]},line width=1.1pt] coordinates{{{coords(x, ux)}}};\n"
write("m12-heat-pulse", rf"""% u(x,t) = (U0/2) [erf((1+x)/(2c sqrt t)) + erf((1-x)/(2c sqrt t))], U0 = 100, c = 1
\begin{{tikzpicture}}
  \begin{{axis}}[EMplot,width=11.5cm,height=6.4cm,xmin=-3.3,xmax=3.5,ymin=-8,ymax=118,
      xtick={{-3,-2,-1,1,2,3}},ytick={{0,100}},xlabel={{$x$}},ylabel={{$u(x,t)$}},clip=false]
    \draw[EMcurve,line width=1.3pt] (axis cs:-3,0)--(axis cs:-1,0)--(axis cs:-1,100)--(axis cs:1,100)--(axis cs:1,0)--(axis cs:3,0);
    \draw[EMdash] (axis cs:-1,0)--(axis cs:-1,100);\draw[EMdash] (axis cs:1,0)--(axis cs:1,100);
{body}    \node[EMlabs,anchor=west] at (axis cs:1.1,104){{$t=0$}};
    \node[EMlabs,anchor=south west] at (axis cs:0.12,91.5){{$t=\tfrac18$}};
    \node[EMlabs,anchor=south west] at (axis cs:0.12,60.5){{$t=\tfrac12$}};
    \node[EMlabs,anchor=south west] at (axis cs:0.12,42){{$t=1$}};
    \node[EMlabs,anchor=south west] at (axis cs:0.12,26.5){{$t=2$}};
    \node[EMlabs,anchor=south west] at (axis cs:0.12,8){{$t=8$}};
  \end{{axis}}
\end{{tikzpicture}}
""")

# --- the plucked string: snapshots of u(x,t) = (1/2)[f(x+ct) + f(x-ct)] -----------------------
L, k = 1.0, 1.0
def tri(xx):  # odd, 2L-periodic extension of the triangle  f = 2k x / L (x<L/2),  2k (L-x)/L
    r = np.mod(xx + L, 2 * L) - L
    return np.where(np.abs(r) <= L / 2, 2 * k * r / L, np.sign(r) * 2 * k * (L - np.abs(r)) / L)
xs = np.linspace(0, L, 201)
times = [(0, "0"), (0.2, r"L/5c"), (0.4, r"2L/5c"), (0.5, r"L/2c"), (0.6, r"3L/5c")]
panels = ""
for i, (tt, name) in enumerate(times):
    ct = tt * L
    ux = 0.5 * (tri(xs + ct) + tri(xs - ct))
    shown = f"t={name}" if tt else "t=0"
    panels += rf"""    \nextgroupplot[ymin=-0.45,ymax=1.1,ytick=\empty,xtick=\empty,axis x line=none,axis y line=none]
    \draw[EMax] (axis cs:-0.05,0)--(axis cs:1.08,0);
    \addplot[EMcurve,line width=1.3pt] coordinates{{{coords(xs, ux)}}};
    \node[EMlabs,anchor=west] at (axis cs:1.1,0){{${shown}$}};
"""
write("m11-triangle-time", rf"""% u(x,t) of the plucked string at t = 0, L/5c, 2L/5c, L/2c, 3L/5c (computed from d'Alembert's formula)
\begin{{tikzpicture}}
  \begin{{groupplot}}[group style={{group size=2 by 3,vertical sep=0.15cm,horizontal sep=1.6cm}},EMplot,width=5.8cm,height=2.2cm,xmin=-0.05,xmax=1.5,clip=false]
{panels}  \end{{groupplot}}
\end{{tikzpicture}}
""")

# --- Bessel functions --------------------------------------------------------------------
xj = np.linspace(0.0, 10, 400)
cols = ["EMrose", "EMamber", "EMjade", "EMindigo", "EMviolet"]
body_j = ""
body_y = ""
for n in range(5):
    body_j += f"    \\addplot[{cols[n]},line width=1.1pt] coordinates{{{coords(xj, special.jv(n, xj))}}};\n"
    xy = np.linspace(0.12 + 0.35 * n, 10, 400)
    yy = special.yv(n, xy)
    keep = yy > -2.2
    body_y += f"    \\addplot[{cols[n]},line width=1.1pt] coordinates{{{coords(xy[keep], yy[keep])}}};\n"
labj = "".join(f"    \\node[EMlabs,text={cols[n]}] at (axis cs:{0.45 + 0.9 * n:.2f},{0.95 - 0.17 * n:.2f}){{$J_{n}$}};\n" for n in range(5))
laby = "".join(f"    \\node[EMlabs,text={cols[n]}] at (axis cs:{0.75 + 0.95 * n:.2f},0.52){{$Y_{n}$}};\n" for n in range(5))
write("m13-bessel", rf"""% Bessel functions of the first kind J_0..J_4 and of the second kind Y_0..Y_4 (scipy.special.jv, yv)
\begin{{tikzpicture}}
  \begin{{groupplot}}[group style={{group size=2 by 1,horizontal sep=1.7cm}},EMplot,width=7.2cm,height=5.2cm,xmin=0,xmax=10.4,xtick={{0,5,10}},clip=true]
    \nextgroupplot[ymin=-0.5,ymax=1.1,ytick={{-0.5,0,0.5,1}},xlabel={{$x$}},title style={{font=\small}},title={{$J_n(x)$}}]
{body_j}{labj}    \nextgroupplot[ymin=-2.2,ymax=0.75,ytick={{-2,-1,0}},xlabel={{$x$}},title style={{font=\small}},title={{$Y_n(x)$}}]
{body_y}{laby}  \end{{groupplot}}
\end{{tikzpicture}}
""")

# --- J0 and its first three roots ----------------------------------------------------------
zeros = special.jn_zeros(0, 3)
xj = np.linspace(0, 10.4, 400)
marks = "".join(f"    \\node[EMhole] at (axis cs:{z:.4f},0){{}};\\node[EMlabs,above right] at (axis cs:{z:.4f},0){{$\\alpha_{i + 1}$}};\n"
                for i, z in enumerate(zeros))
write("m13-j0-zeros", rf"""% J_0(x) and its first three roots (scipy.special.jv, jn_zeros)
\begin{{tikzpicture}}
  \begin{{axis}}[EMplot,width=10cm,height=5cm,xmin=0,xmax=10.8,ymin=-0.55,ymax=1.1,xtick={{0,5,10}},ytick={{-0.5,0,0.5,1}},xlabel={{$x$}},ylabel={{$J_0(x)$}}]
    \addplot[EMrose,line width=1.3pt] coordinates{{{coords(xj, special.jv(0, xj))}}};
{marks}  \end{{axis}}
\end{{tikzpicture}}
""")
print("figures written to", OUT)
