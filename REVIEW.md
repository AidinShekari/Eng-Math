# Review notes

Places where the typeset notes deliberately differ from, or add a caveat to, the
instructor's slides. The slides remain the source of truth; each entry says what
the slide shows, what the notes show, and why. Page numbers are slide numbers in the
source PDF named in brackets (CA = complex analysis, FA = Fourier analysis,
PDE = partial differential equations).

## Corrections (unambiguous errors)

| Where | Slide shows | Notes show | Why |
|---|---|---|---|
| Ch. 1, De Moivre consequence (CA p. 9) | $z^k=\lvert z\rvert^k(\cos k\theta+\sin k\theta)$ | $\ldots+i\sin k\theta$ | the imaginary unit is missing; the next line of the slide has it |
| Ch. 1, Lagrange identity (CA p. 12) | $\sin\left[(n+\tfrac32)\theta\right]$ | $\sin\left[(n+\tfrac12)\theta\right]$ | $n=0$ gives $1$ only with $\tfrac12$ |
| Ch. 2, constants of integration (CA pp. 28–29) | $\varphi(x)=c,\ c\in\mathbb{C}$ | $c\in\mathbb{R}$ | $v$ is real-valued, so its constant is real |
| Ch. 2, polar Laplace exercise (CA p. 31) | $\nabla^2u=u_{rr}+\tfrac1{r^2}u_{\theta\theta}+\tfrac1ru_r$ | $\ldots=0$ | the exercise asks to show that $u,v$ satisfy Laplace's equation |

| Ch. 3, periodicity of $\cos z$ (CA p. 43) | $\cos x\cosh y\,i\sin x\sinh y$ | $\cos x\cosh y-i\sin x\sinh y$ | the minus sign is missing; the line above has it |
| Ch. 5, $\int\bar z\,dz$ along $z(t)=t+i$ (CA p. 60) | $=t^2+it\big\rvert_{-1}^{1}=0+i2$ | $=\big(\tfrac{t^2}2-it\big)\big\rvert_{-1}^{1}=0-i2$ | $\int(t-i)\,dt$ is $\tfrac{t^2}2-it$; the conclusion (the integral depends on the path) is unchanged |
| Ch. 5, $\int e^{z/2}dz$ (CA p. 63) | $2\big(e^{4-3\pi i/2}-e^{4+3\pi i/2}\big)=0$ | $2\big(e^{4-3\pi i/2}-e^{4+\pi i/2}\big)=0$ | the lower limit is $8+\pi i$; with $3\pi i/2$ the value would be $4ie^{4}$, not $0$ |
| Ch. 5, Cauchy's theorem with several points (CA p. 77) | last line of the proof: $\oint_C=\oint_{C_1}+\oint_{C_2}-\cdots-\oint_{C_n}$ | $\oint_C=\oint_{C_1}+\cdots+\oint_{C_n}$ | the signs contradict the theorem just stated and the line above; the proof is now written with the circles' orientation spelled out |
| Ch. 5, $\int\cos\omega x/(1+x^2)\,dx$ (CA pp. 73–75) | the last two lines use $\cos x$; $\omega$ is not restricted | $\cos\omega x$; $\omega>0$ stated | $\cos x$ is a typo; $\omega>0$ is needed for $e^{-\omega R\sin t}\to0$ |
| Ch. 5, bounded entire functions (CA p. 85) | $\dfrac1{2\pi}\dfrac{M}{R^2}\oint_C dz=\dfrac{M}{2\pi R^2}\times0=0$ | $\dfrac1{2\pi}\dfrac{M}{R^2}\oint_C\lvert dz\rvert=\dfrac MR\to0$ | $\oint dz=0$ does not bound a modulus; the arc length $2\pi R$ gives the required bound |

| Ch. 6, residue at a pole of order $p$ (CA pp. 94, 107) | $\dfrac1{(p-k)!}\dfrac{d^{p-1}}{dz^{p-1}}\big[\cdots\big]$ for $A_1$ | $\dfrac1{(p-1)!}\dfrac{d^{p-1}}{dz^{p-1}}\big[\cdots\big]$ | $A_1$ is the case $k=1$; in the simple-pole proof $p=1$ gives $0!$ |
| Ch. 6, Laurent series of $\dfrac{z}{(z+1)(z+4)^3}$ about $z=-1$ (CA pp. 102–103) | $\ldots-\tfrac1{27}\tfrac1{z+1}-\tfrac2{27}+\tfrac1{81}(z+1)+\cdots$ (the intermediate coefficients are printed as $\tfrac{2^2\cdot3}{3^4}-\tfrac2{3^2}$ and $\tfrac3{3^3}-\tfrac{8\cdot3}{3^4\cdot3}$) | $-\tfrac1{27}\tfrac1{z+1}+\tfrac2{27}-\tfrac5{81}(z+1)+\cdots$ | the first two coefficients of $z/(z+4)^3$ are $-\tfrac1{27}$ and $+\tfrac2{27}$, then $-\tfrac5{81}$ (checked at $z=-\tfrac12$: the corrected series gives $\approx-0.0212$ after three terms, the exact value is $-0.0233$); the residue $-\tfrac1{27}$ and the pole type are unchanged |
| Ch. 7, class-1 example (CA p. 111) | the integral along the semicircle is printed with denominator $1+R^2e^{i2t}$ | $(1+R^2e^{i2t})^2$ | the integrand of this example has the squared denominator; $\omega>0$ stated |
| Ch. 7, second-class formula (CA p. 112) | $\displaystyle\int_0^{2\pi}f(a\cos t,b\sin t)\,dt=\oint_C f(\ldots)\,dz$ | $\ldots\oint_C f(\ldots)\,\dfrac{dz}{iz}$ | $dt=dz/(iz)$ was derived on the same slide; the worked example uses it |
| Ch. 7, example $\int_0^{2\pi}\frac{dx}{2+\cos x}$ (CA p. 113) | labelled "first class" | labelled by its type: second class | it is a trigonometric integral, i.e. the second class |

| Ch. 8, trigonometric review (FA p. 5) | $\sin2\alpha=2\sin\alpha\cos\beta$ | $2\sin\alpha\cos\alpha$ | typo; the next slide's identities depend on it |
| Ch. 8, integrals review (FA pp. 6, 8) | $\int_{-\pi}^{\pi}\cos nt\,dt=0$, $\int\sin^2nt\,dt=\pi$, $\int\cos^2nt\,dt=\pi$ for $n\in\mathbb{Z}$ | for $n\in\mathbb{Z}\setminus\{0\}$ | at $n=0$ the integrals are $2\pi$, $0$ and $2\pi$ |
| Ch. 8, derivation of the coefficients (FA pp. 11–12) | the sums run over $n=-\infty$ to $\infty$ | $n=1$ to $\infty$ | the series starts at $n=1$ |
| Ch. 8, Lemma 2 (FA p. 46) | $\int e^{ax}\sin nx\,dx=\dfrac{e^{ax}}{a^2+n^2}(a\sin nx-n\sin nx)$ | $\ldots(a\sin nx-n\cos nx)$ | the slide's own summary a few lines below has $\cos nx$ |
| Ch. 8, $b_n$ of $e^{-\alpha x}$ (FA p. 48) | $(-a\sin nx-n\sin nx)$ | $(-\alpha\sin nx-n\cos nx)$ | Lemma 2 with $\alpha\to-\alpha$; the printed result is consistent with $\cos nx$ |
| Ch. 8, problem 3 notation (FA pp. 45–48) | the parameter is $\alpha$ in the statement and $a$ in the solution | $\alpha$ throughout | same quantity, one symbol |
| Ch. 9, best approximation (FA p. 49) | $f(x)=f(x+\pi)$ | $f(x)=f(x+2\pi)$ | the integrals run over $[-\pi,\pi]$, i.e. a period of $2\pi$ |
| Ch. 9, best approximation (FA p. 51) | $\beta_m=\frac1\pi\int f(x)\cos mx\,dx=b_m$ | $\sin mx$ | $b_m$ is the sine coefficient |
| Ch. 9, power example (FA p. 57) | the numerator uses $\dfrac{4k}{n\pi}(1-\cos n\pi)$ | $\dfrac{2k}{n\pi}(1-\cos n\pi)$ | this is $b_n$ (printed two lines above on the slide); the printed values $0.9496$ and $0.9331$ are those of the corrected sum |
| Ch. 10, Example 3 (FA p. 72) | $B(\omega)=\int e^{-x}\sin\omega x\,dx$ over $(-\infty,\infty)$ | $\int e^{-\lvert x\rvert}\sin\omega x\,dx=0$ | the function of the example is $e^{-\lvert x\rvert}$ |
| Ch. 10, frequency derivative (FA p. 77) | $\int(xf)\sin\omega x\,dx=B'(\omega)$ | $\int(xf)\cos\omega x\,dx=B'(\omega)$ | $B'(\omega)=\int xf\cos\omega x\,dx$ on the line above |
| Ch. 10, exercise 1 (FA p. 78) | $\ldots\,dx$ | $\ldots\,dw$ | the integration variable is $w$ |

| Ch. 11, separation of variables (PDE p. 7) | $X''+\lambda X=0$ | $X''+\lambda^2X=0$ | the separation constant is $-\lambda^2$ on the same slide; the solution $A\cos\lambda x+B\sin\lambda x$ needs $\lambda^2$ |
| Ch. 12, d'Alembert (PDE p. 21) | $\Psi(x)=\tfrac12 f'(x)-\tfrac1{2c}\int g\,ds+k_2$ | $\tfrac12 f(x)-\cdots$ | the antiderivative of $\tfrac12f'$ is $\tfrac12f$ (the line for $\Phi$ above has $f$) |
| Ch. 12, error function series (PDE p. 44) | $\tfrac{2}{\sqrt\pi}\sum(-1)^{n+1}\dfrac{x^{2n-1}}{n!\,(2n-1)}$ | $\dfrac{x^{2n-1}}{(n-1)!\,(2n-1)}$ | the expanded series on the same slide ($x-\tfrac{x^3}{1!\cdot3}+\tfrac{x^5}{2!\cdot5}-\cdots$) corresponds to $(n-1)!$; with $n!$ the second term would be $x^3/6$ instead of $x^3/3$ |
| Ch. 13, polar coordinates (PDE p. 66) | the second row of the table lists $\theta_{xx}=\dfrac{-2xy}{r^4}$ | $\theta_{yy}=\dfrac{-2xy}{r^4}$ | the second row is about $y$ |
| Ch. 14, example 6 (PDE p. 73) | $\mathcal{L}\{\sin\omega t\}=\int\sin e^{-st}dt$ and $(-s\sin\omega t-\omega\sin\omega t)$ | $\int\sin\omega t\,e^{-st}dt$ and $(-s\sin\omega t-\omega\cos\omega t)$ | typos; the lemma printed next to it has $\cos nx$ and the result is unchanged |
| Ch. 14, unit step (PDE p. 76) | $u(t)=0$ for $t<\mathrm{o}$ | $t<0$ | letter "o" for zero |

## Small additions (derived from the surrounding slide, not new content)

| Where | Addition |
|---|---|
| Ch. 4, linear-mapping example (CA p. 52) | the four vertex images $w(0),w(1),w(i),w(1+i)$ are listed; they are exactly the corners of the diamond drawn on the slide |
| Ch. 4, chapter opener | one introductory sentence |
| Ch. 5, proof of the generalized Cauchy theorem (CA p. 77) | the orientation of the small circles is stated explicitly (see the correction table) |
| Ch. 13, notation (PDE pp. 52–53) | the constants of $Y_m(y)$ are written $B_n$ on the slide and $B_m$ here (the index of the function) |
| Ch. 8, the Fourier-series history slide (FA p. 9) | the portrait of Fourier is not reproduced (a raster picture; the surrounding text is kept) |

## Statements kept as written but worth a second look

| Where | Remark |
|---|---|
| Ch. 3, logarithm (CA pp. 47–48) | "Analytic in the whole plane except the origin" holds for a branch only off its cut (the principal branch is discontinuous on the negative real axis); the properties $\ln(z_1z_2)=\ln z_1+\ln z_2$ etc. hold up to multiples of $2\pi i$. |
| Ch. 5, exercise 1 (CA p. 86) | The slide prints the denominator as "$(2z-1)4$"; read as $(2z-1)^4$, in line with the generalized formula on the preceding slides. |
| Ch. 2, example $w=\lvert z\rvert^2$ (CA p. 26) | The slide says "analytic nowhere except at the origin". Strictly, $\lvert z\rvert^2$ is differentiable only at the origin and analytic nowhere (analyticity needs a neighbourhood). |
