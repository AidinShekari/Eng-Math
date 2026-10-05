# Fourier Series

## Periodic Functions

$$f(x+p)=f(x)\quad\Longrightarrow\quad f(x+np)=f(x)$$

```{.figure #m08-periodic caption="A periodic function with period $p$"}
```

- The smallest positive value of $p$ for which the function is periodic is called the fundamental period of the function.
- If a function is periodic with period $p$, it is also periodic with period $np$, where $n$ is a natural number.

### The Periodic Functions Sine and Cosine

::: {.example}
The function $\sin x$ is periodic with period $2\pi$, and $\sin2x$ is periodic with fundamental period $\pi$, although $2\pi$ is also a period of it. Likewise $\sin3x$ is periodic with period $2\pi/3$, although $2\pi$ is also a period of it.
:::

```{.figure #m08-sincos caption="The functions $\\sin nx$ and $\\cos nx$ for $n=1,2,3$ on $[0,2\\pi]$"}
```

## Review of Trigonometry

$$\begin{gathered}
\sin^2\alpha+\cos^2\alpha=1\\
\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta\\
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta\\
\cos2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha=\cos^2\alpha-\sin^2\alpha\\
\sin2\alpha=2\sin\alpha\cos\alpha\\
\sin^2\alpha=\frac{1-\cos2\alpha}{2}\qquad\cos^2\alpha=\frac{1+\cos2\alpha}{2}\\
\sin\alpha\sin\beta=\tfrac12\big[\cos(\alpha-\beta)-\cos(\alpha+\beta)\big]\\
\cos\alpha\cos\beta=\tfrac12\big[\cos(\alpha-\beta)+\cos(\alpha+\beta)\big]\\
\sin\alpha\cos\beta=\tfrac12\big[\sin(\alpha-\beta)+\sin(\alpha+\beta)\big]
\end{gathered}$$

## Review: Integrals and Orthogonality

$$\int_{-\pi}^{\pi}\sin nt\,dt=0,\qquad n\in\mathbb{Z}$$
$$\int_{-\pi}^{\pi}\cos nt\,dt=0,\qquad n\in\mathbb{Z}\setminus\{0\}$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin nt\,dt=-\frac1n\cos nt\Big|_{-\pi}^{\pi}=0,\qquad \int_{-\pi}^{\pi}\cos nt\,dt=\frac1n\sin nt\Big|_{-\pi}^{\pi}=0\qquad(n\neq0)$$
:::

### Orthogonality

$$\int_{-\pi}^{\pi}\sin nt\sin mt\,dt=0,\qquad n,m\in\mathbb{Z},\ n\neq m$$
$$\int_{-\pi}^{\pi}\cos nt\cos mt\,dt=0,\qquad n,m\in\mathbb{Z},\ n\neq m$$
$$\int_{-\pi}^{\pi}\sin nt\cos mt\,dt=0,\qquad n,m\in\mathbb{Z}\ \ (n\neq m\ \text{or}\ n=m)$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin nx\sin mx\,dx=\frac12\int_{-\pi}^{\pi}\cos(n-m)x\,dx-\frac12\int_{-\pi}^{\pi}\cos(n+m)x\,dx$$
$$\int_{-\pi}^{\pi}\cos nx\cos mx\,dx=\frac12\int_{-\pi}^{\pi}\cos(n+m)x\,dx+\frac12\int_{-\pi}^{\pi}\cos(n-m)x\,dx$$
$$\int_{-\pi}^{\pi}\sin nx\cos mx\,dx=\frac12\int_{-\pi}^{\pi}\sin(n+m)x\,dx+\frac12\int_{-\pi}^{\pi}\sin(n-m)x\,dx$$
:::

$$\int_{-\pi}^{\pi}\sin^2nt\,dt=\pi,\qquad \int_{-\pi}^{\pi}\cos^2nt\,dt=\pi,\qquad n\in\mathbb{Z}\setminus\{0\}$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin^2nt\,dt=\int_{-\pi}^{\pi}\frac{1-\cos2nt}{2}\,dt=\pi,\qquad \int_{-\pi}^{\pi}\cos^2nt\,dt=\int_{-\pi}^{\pi}\frac{1+\cos2nt}{2}\,dt=\pi$$
:::

## The Fourier Series

::: {.remark title="History"}
Joseph Fourier (1768–1830) put forward the idea of expressing periodic functions as a series of sinusoidal functions. When this revolutionary idea was presented, some mathematicians, Lagrange among them, objected to its generality, until Dirichlet stated the conditions for the convergence of the Fourier series.
:::

::: {.theorem title="The Fourier series"}
If the function $f(x)$ is periodic with period $2\pi$, it can be expressed as a trigonometric series as follows:
$$f(x)=a_0+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big)$$
where
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx,\qquad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx,\qquad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx$$
:::

::: {.proof}
Suppose the periodic function has been written as the trigonometric series above; it suffices to find the coefficients $a_0$, $a_n$ and $b_n$.

**Computing $a_0$.** Integrating both sides over an interval of length $2\pi$ gives
$$\int_{-\pi}^{\pi}f(x)\,dx=\int_{-\pi}^{\pi}\left[a_0+\sum_{n=1}^{\infty}(a_n\cos nx+b_n\sin nx)\right]dx=a_0\int_{-\pi}^{\pi}dx+\sum_{n=1}^{\infty}\left(a_n\underbrace{\int_{-\pi}^{\pi}\cos nx\,dx}_{0}+b_n\underbrace{\int_{-\pi}^{\pi}\sin nx\,dx}_{0}\right)=2\pi a_0$$
$$\Longrightarrow\quad a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx$$
$a_0$ is the mean value or DC level of the function.

**Computing $a_n$.** Multiplying both sides by $\cos mx$ and integrating over an interval of length $2\pi$:
$$\int_{-\pi}^{\pi}f(x)\cos mx\,dx=\int_{-\pi}^{\pi}a_0\cos mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}a_n\cos nx\cos mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}b_n\sin nx\cos mx\,dx=\pi a_m$$
$$\Longrightarrow\quad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx$$

**Computing $b_n$.** Multiplying both sides by $\sin mx$ and integrating over an interval of length $2\pi$:
$$\int_{-\pi}^{\pi}f(x)\sin mx\,dx=\int_{-\pi}^{\pi}a_0\sin mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}a_n\cos nx\sin mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}b_n\sin nx\sin mx\,dx=\pi b_m$$
$$\Longrightarrow\quad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx$$
:::

::: {.important title="The Fourier series and Euler's formulas"}
$$f(x)=a_0+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big),\qquad f(x+2\pi)=f(x)$$
$$a_0=\frac1{2\pi}\int_{2\pi}f(x)\,dx,\qquad a_n=\frac1\pi\int_{2\pi}f(x)\cos nx\,dx,\qquad b_n=\frac1\pi\int_{2\pi}f(x)\sin nx\,dx$$
(the integral is taken over one period of length $2\pi$.)
:::

::: {.remark}
At points of discontinuity of the function, the value of the Fourier series equals the average of the upper and lower limits at that point.
:::

## Review: The Definite Integral of a Product of Two Functions

By integration by parts:
$$\int_\alpha^\beta f(x)g(x)\,dx=\Big[f(x)G_1(x)-f^{(1)}(x)G_2(x)+f^{(2)}(x)G_3(x)-+\cdots\Big]_\alpha^\beta$$
where $f^{(k)}$ is the $k$-th derivative of $f$ and $G_k$ is the $k$-th integral of $g$:

| derivatives of $f$ | | integrals of $g$ |
|:---:|:---:|:---:|
| $f(x)$ | $\searrow$ | $g(x)$ |
| $f^{(1)}(x)$ | $\searrow$ | $G_1(x)$ |
| $f^{(2)}(x)$ | $\searrow$ | $G_2(x)$ |
| $f^{(3)}(x)$ | $\searrow$ | $G_3(x)$ |
| $\vdots$ | | $\vdots$ |

## Examples of Fourier Series

::: {.example}
Find the Fourier series of the following function:
$$f(x)=\begin{cases}-k&-\pi<x<0\\ \ \ k&0<x<\pi\end{cases}\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=0$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx=\frac1\pi\left[\int_{-\pi}^{0}(-k)\cos nx\,dx+\int_0^\pi k\cos nx\,dx\right]=\frac1\pi\left[-k\,\frac{\sin nx}{n}\Big|_{-\pi}^{0}+k\,\frac{\sin nx}{n}\Big|_0^\pi\right]=0$$
$$\begin{aligned}
b_n&=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx=\frac1\pi\left[\int_{-\pi}^{0}(-k)\sin nx\,dx+\int_0^\pi k\sin nx\,dx\right]\\
&=\frac1\pi\left[k\,\frac{\cos nx}{n}\Big|_{-\pi}^{0}-k\,\frac{\cos nx}{n}\Big|_0^\pi\right]=\frac k{n\pi}\big[\cos0-\cos(-n\pi)-\cos n\pi+\cos0\big]=\frac{2k}{n\pi}(1-\cos n\pi)
\end{aligned}$$
$$\cos n\pi=\begin{cases}-1&n\ \text{odd}\\ \ \ 1&n\ \text{even}\end{cases}\quad\Longrightarrow\quad1-\cos n\pi=\begin{cases}2&n\ \text{odd}\\ 0&n\ \text{even}\end{cases}$$
$$b_1=\frac{4k}{\pi},\quad b_2=0,\quad b_3=\frac{4k}{3\pi},\quad b_4=0,\quad b_5=\frac{4k}{5\pi},\ \dots$$
$$f(x)=\frac{4k}\pi\left(\sin x+\frac13\sin3x+\frac15\sin5x+\cdots\right)$$
:::
:::

```{.figure #m08-square-wave caption="A square wave $f(x)$ with period $2\\pi$ and values $\\pm k$"}
```

The partial sums of the series:

$$S_1=\frac{4k}\pi\sin x,\qquad S_2=\frac{4k}\pi\left(\sin x+\frac13\sin3x\right),\qquad S_3=\frac{4k}\pi\left(\sin x+\frac13\sin3x+\frac15\sin5x\right)$$

```{.figure #m08-partial-sums caption="The partial sums $S_1$, $S_2$ and $S_3$ of the Fourier series of the square wave (the dashed line is the square wave itself)"}
```

Setting $x=\pi/2$:
$$f(\pi/2)=\frac{4k}\pi\left(1-\frac13+\frac15-\frac17+-\cdots\right)=k\quad\Longrightarrow\quad\pi=4\left(1-\frac13+\frac15-\frac17+-\cdots\right)$$

::: {.example}
Find the Fourier series of the following function:
$$f(x)=x,\qquad -\pi\le x\le\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=0$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}x\cos nx\,dx=\frac1\pi\left[x\left(\frac1n\sin nx\right)-(1)\left(-\frac1{n^2}\cos nx\right)\right]_{-\pi}^{\pi}=\frac1\pi\left[\frac1{n^2}\big(\cos n\pi-\cos(-n\pi)\big)\right]=0$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}x\sin nx\,dx=\frac2\pi\int_0^\pi x\sin nx\,dx=\frac2\pi\left[x\left(\frac{-1}n\cos nx\right)-(1)\left(\frac{-1}{n^2}\sin nx\right)\right]_0^\pi=\frac2\pi\left[\frac{-\pi}n\cos n\pi\right]=\frac2n(-1)^{n+1}$$
$$f(x)=\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin nx=2\left(\sin x-\frac12\sin2x+\frac13\sin3x-+\cdots\right)$$
:::
:::

```{.figure #m08-sawtooth caption="The sawtooth wave $f(x)=x$ on $[-\\pi,\\pi]$ with its periodic extension"}
```

Setting $x=\pi/2$:
$$f\!\left(\frac\pi2\right)=\frac\pi2=\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin\!\left(n\frac\pi2\right)=2\left(1-\frac13+\frac15-\frac17+-\cdots\right)=\sum_{n=1}^{\infty}\frac2{2n-1}(-1)^{n+1}\ \Longrightarrow\ \pi=\sum_{n=1}^{\infty}\frac4{2n-1}(-1)^{n+1}$$

The value of the series at the point of discontinuity $x=\pi$:
$$f(\pi)=\;?\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin(n\pi)=0$$

::: {.important title="Important remarks"}
1. If a periodic function is odd, all the $a$ coefficients are zero.
2. At a point of discontinuity, the value of the Fourier series equals the average of the upper and lower limits at that point.
:::

::: {.example}
Find the Fourier series of the following function:
$$f(x)=x^2,\qquad -\pi\le x\le\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}x^2\,dx=\frac{2}{2\pi}\int_0^\pi x^2\,dx=\frac1\pi\left[\frac13x^3\right]_0^\pi=\frac{\pi^2}{3}$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}x^2\cos nx\,dx=\frac2\pi\int_0^\pi x^2\cos nx\,dx=\frac2\pi\left[x^2\left(\frac1n\sin nx\right)-2x\left(\frac{-1}{n^2}\cos nx\right)+2\left(\frac{-1}{n^3}\sin nx\right)\right]_0^\pi=\frac2\pi\left[\frac{2\pi}{n^2}\cos n\pi\right]=\frac4{n^2}(-1)^n$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}x^2\sin nx\,dx=0$$
$$f(x)=\frac{\pi^2}3+\sum_{n=1}^{\infty}\frac4{n^2}(-1)^n\cos nx$$
:::
:::

```{.figure #m08-parabola caption="The function $f(x)=x^2$ on $[-\\pi,\\pi]$ with its periodic extension"}
```

::: {.important title="Important remark"}
If a periodic function is even, all the $b$ coefficients are zero.
:::

Setting $x=0$:
$$f(0)=0=\frac{\pi^2}3+\sum_{n=1}^{\infty}\frac4{n^2}(-1)^n\cos(n\cdot0)\quad\Longrightarrow\quad\frac{\pi^2}3=\sum_{n=1}^{\infty}\frac4{n^2}(-1)^{n+1}$$
$$\pi^2=\sum_{n=1}^{\infty}\frac{12}{n^2}(-1)^{n+1}=12\left(1-\frac14+\frac19-\frac1{16}+-\cdots\right)$$

::: {.example}
Find the Fourier series of the following function:
$$f(x)=x^2,\qquad 0\le x\le2\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_0^{2\pi}x^2\,dx=\frac1{2\pi}\left[\frac13x^3\right]_0^{2\pi}=\frac1{2\pi}\cdot\frac138\pi^3=\frac{4\pi^2}3$$
$$a_n=\frac1\pi\int_0^{2\pi}x^2\cos nx\,dx=\frac1\pi\left[x^2\left(\frac1n\sin nx\right)-2x\left(\frac{-1}{n^2}\cos nx\right)+2\left(\frac{-1}{n^3}\sin nx\right)\right]_0^{2\pi}=\frac1\pi(2\times2\pi)\left(\frac1{n^2}\cos2\pi n\right)=\frac4{n^2}$$
$$b_n=\frac1\pi\int_0^{2\pi}x^2\sin nx\,dx=\frac1\pi\left[x^2\left(\frac{-1}n\cos nx\right)-2x\left(\frac{-1}{n^2}\sin nx\right)+2\left(\frac1{n^3}\cos nx\right)\right]_0^{2\pi}=\frac1\pi\left[(4\pi^2)\left(\frac{-1}n\right)+2\cdot\frac1{n^3}-2\cdot\frac1{n^3}\right]=-\frac{4\pi}n$$
$$f(x)=\frac{4\pi^2}3+\sum_{n=1}^{\infty}\left(\frac4{n^2}\cos nx-\frac{4\pi}n\sin nx\right)$$
:::
:::

```{.figure #m08-shifted-parabola caption="The function $f(x)=x^2$ on $[0,2\\pi]$ with its periodic extension"}
```

## Fourier Series of Functions with an Arbitrary Period

$$f(x+T)=f(x)$$
Using the auxiliary variable $t=\dfrac{2\pi}{T}x$ ($x:0\to T$ and $t:0\to2\pi$):
$$f\!\left(\frac T{2\pi}t\right)=a_0+\sum_{n=1}^{\infty}a_n\cos nt+b_n\sin nt$$
$$a_0=\frac1{2\pi}\int_{2\pi}f\!\left(\frac T{2\pi}t\right)dt,\qquad a_n=\frac1\pi\int_{2\pi}f\!\left(\frac T{2\pi}t\right)\cos nt\,dt,\qquad b_n=\frac1\pi\int_{2\pi}f\!\left(\frac T{2\pi}t\right)\sin nt\,dt$$
Returning to $x=\dfrac T{2\pi}t$:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$a_0=\frac1{2\pi}\int_Tf(x)\frac{2\pi}T\,dx=\frac1T\int_Tf(x)\,dx$$
$$a_n=\frac1\pi\int_Tf(x)\cos\!\left(\frac{2\pi}Tnx\right)\frac{2\pi}T\,dx=\frac2T\int_Tf(x)\cos\!\left(\frac{2\pi}Tnx\right)dx$$
$$b_n=\frac1\pi\int_Tf(x)\sin\!\left(\frac{2\pi}Tnx\right)\frac{2\pi}T\,dx=\frac2T\int_Tf(x)\sin\!\left(\frac{2\pi}Tnx\right)dx$$

::: {.theorem title="The Fourier series (period $T$)"}
If the function $f(x)$ is periodic with period $T$, it can be expressed as a trigonometric series as follows:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx,\qquad f(x+T)=f(x)$$
$$a_0=\frac1T\int_Tf(x)\,dx,\qquad a_n=\frac2T\int_Tf(x)\cos\frac{2\pi}Tnx\,dx,\qquad b_n=\frac2T\int_Tf(x)\sin\frac{2\pi}Tnx\,dx$$
:::

::: {.remark}
At points of discontinuity of the function, the value of the Fourier series equals the average of the upper and lower limits there; the value of the Fourier series at the point $x$ is
$$\frac{f(x^+)+f(x^-)}{2}$$
:::

## Dirichlet's Theorem

::: {.theorem title="Dirichlet's theorem"}
If the function $f(x)$ is periodic and **bounded**, has a **finite number of maxima and minima**, and also a **finite number of points of discontinuity** in each period, then this function has a Fourier series, and the value of the Fourier series at points of discontinuity equals the average of the right and left limits at those points.
:::

Examples of functions that do not satisfy Dirichlet's conditions:

$$f(x)=1/x,\quad 0<x\le1,\qquad f(x+1)=f(x)$$
$$f(x)=\sin(1/x),\quad 0<x\le1,\qquad f(x+1)=f(x)$$

```{.figure #m08-dirichlet caption="Functions that violate Dirichlet's conditions: $1/x$ (unbounded), $\\sin(1/x)$ (infinitely many maxima and minima) and a staircase function with infinitely many steps"}
```

## Solving Some Problems

::: {.example title="Problem 1"}
Find the Fourier series of the following function:
$$f(x)=\sin\alpha x,\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
Since this function is odd, $a_0=0$ and $a_n=0$.
$$\begin{aligned}
b_n&=\frac1\pi\int_{-\pi}^{\pi}\sin\alpha x\sin nx\,dx=\frac2\pi\int_0^\pi\sin\alpha x\sin nx\,dx=\frac1\pi\int_0^\pi\big[\cos(\alpha-n)x-\cos(\alpha+n)x\big]dx\\
&=\frac1\pi\left[\frac{\sin(\alpha-n)x}{\alpha-n}-\frac{\sin(\alpha+n)x}{\alpha+n}\right]_0^\pi=\cdots=\frac{2n(-1)^n\sin\alpha\pi}{\pi(\alpha^2-n^2)}
\end{aligned}$$
$$f(x)=\sum_{n=1}^{\infty}\frac{2n(-1)^n\sin\alpha\pi}{\pi(\alpha^2-n^2)}\sin nx$$

We examine the series when $\alpha=1$:
$$\lim_{\alpha\to1}b_1=\lim_{\alpha\to1}\frac{2(-1)^1\sin\alpha\pi}{\pi(\alpha^2-1^2)}=\lim_{\alpha\to1}\frac{-2(\pi\cos\alpha\pi)}{\pi(2\alpha)}=1,\qquad b_n\Big|_{n\neq1}=0$$
Hence the Fourier series is simply $f(x)=\sin x$.
:::
:::

::: {.exercise}
Examine the series when $\alpha=m$, $m\in\mathbb{N}$.
:::

::: {.example title="Problem 2"}
Find the Fourier series of the following function and deduce $\csc\alpha\pi$ from it.
$$f(x)=\cos\alpha x,\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
Since this function is even, $b_n=0$ and $f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx$.
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}\cos\alpha x\,dx=\frac1\pi\int_0^\pi\cos\alpha x\,dx=\frac1\pi\left[\frac{\sin\alpha x}{\alpha}\right]_0^\pi=\frac1{\alpha\pi}\sin\alpha\pi$$
$$a_n=\frac2\pi\int_0^\pi\cos\alpha x\cos nx\,dx=\frac1\pi\int_0^\pi\big[\cos(\alpha-n)x+\cos(\alpha+n)x\big]dx=\frac1\pi\left[\frac{\sin(\alpha-n)x}{\alpha-n}+\frac{\sin(\alpha+n)x}{\alpha+n}\right]_0^\pi=\cdots=\frac{(-1)^n2\alpha\sin\alpha\pi}{\pi(\alpha^2-n^2)}$$
$$f(x)=\frac1{\alpha\pi}\sin\alpha\pi+\frac{2\alpha\sin\alpha\pi}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}\cos nx$$
The periodic function is continuous at $x=0$, so
$$f(0)=1=\frac1{\alpha\pi}\sin\alpha\pi+\frac{2\alpha\sin\alpha\pi}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}\quad\Longrightarrow\quad\frac1{\sin\alpha\pi}=\csc\alpha\pi=\frac1{\alpha\pi}+\frac{2\alpha}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}$$
:::
:::

::: {.exercise}
Prove that if $\alpha=m$, $m\in\mathbb{N}$, then
$$a_0=0,\qquad a_n=\begin{cases}1&n=m\\ 0&n\neq m\end{cases}$$
:::

::: {.example title="Problem 3"}
Find the Fourier series of the following function and deduce $\coth\alpha\pi$ from it.
$$f(x)=e^{-\alpha x},\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
**Lemma 1:**
$$\int e^{\alpha x}\cos nx\,dx=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\cos nx+n\sin nx\big)$$
Proof: integrating by parts twice, with $I=\int e^{\alpha x}\cos nx\,dx$:
$$I=\frac1\alpha e^{\alpha x}\cos nx-\int\frac1\alpha e^{\alpha x}(-n\sin nx)\,dx=\frac1\alpha e^{\alpha x}\cos nx+\frac n\alpha\int e^{\alpha x}\sin nx\,dx$$
$$=\frac1\alpha e^{\alpha x}\cos nx+\frac n\alpha\left[\frac1\alpha e^{\alpha x}\sin nx-\int\frac1\alpha e^{\alpha x}(n\cos nx)\,dx\right]=\frac1\alpha e^{\alpha x}\cos nx+\frac n{\alpha^2}e^{\alpha x}\sin nx-\frac{n^2}{\alpha^2}I$$
$$\Longrightarrow\quad I=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\cos nx+n\sin nx\big)$$

**Lemma 2:**
$$\int e^{\alpha x}\sin nx\,dx=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\sin nx-n\cos nx\big)$$
(proof left as an exercise.)

The function is neither even nor odd, so all the Fourier coefficients must be computed.
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-\alpha x}\,dx=\frac1{-2\pi\alpha}\Big[e^{-\alpha x}\Big]_{-\pi}^{\pi}=\frac1{2\pi\alpha}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{\sinh\alpha\pi}{\alpha\pi}$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}e^{-\alpha x}\cos nx\,dx=\left\{\frac{e^{-\alpha x}}{\pi(\alpha^2+n^2)}\big(-\alpha\cos nx+n\sin nx\big)\right\}_{-\pi}^{\pi}=\frac{\alpha(-1)^n}{\pi(\alpha^2+n^2)}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}e^{-\alpha x}\sin nx\,dx=\left\{\frac{e^{-\alpha x}}{\pi(\alpha^2+n^2)}\big(-\alpha\sin nx-n\cos nx\big)\right\}_{-\pi}^{\pi}=\frac{n(-1)^n}{\pi(\alpha^2+n^2)}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi$$
$$\begin{aligned}
f(x)&=\frac{\sinh\alpha\pi}{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi\cos nx+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi\sin nx\right)\\
&=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\cos nx+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sin nx\right)\right)
\end{aligned}$$
Since $x=\pi$ is a point of discontinuity, the value of the Fourier series there equals the average of the upper and lower limits of the function at that point, i.e.
$$\frac{f(\pi^+)+f(\pi^-)}2=\frac{e^{\alpha\pi}+e^{-\alpha\pi}}2=\cosh\alpha\pi$$
$$\cosh\alpha\pi=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\cos n\pi+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sin n\pi\right)\right)=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\frac{2\alpha}{\pi(\alpha^2+n^2)}\right)$$
$$\coth\alpha\pi=\frac{\cosh\alpha\pi}{\sinh\alpha\pi}=\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\frac{2\alpha}{\pi(\alpha^2+n^2)}$$
:::
:::
