# The Laplace Transform

## The One-Sided Laplace Transform

::: {.definition title="The one-sided Laplace transform"}
$$F(s)=\mathcal{L}\{f(t)\}\triangleq\int_0^\infty f(t)\,e^{-st}\,dt\qquad\Longleftrightarrow\qquad f(t)=\mathcal{L}^{-1}\{F(s)\}$$
:::

The Laplace transform is one of the important tools in various engineering and mathematical applications. One of its applications is solving differential equations (read Chapter 6 of the course textbook).

The Laplace transform is a linear operator:
$$\mathcal{L}\{af(t)+bg(t)\}=a\,\mathcal{L}\{f(t)\}+b\,\mathcal{L}\{g(t)\}$$

::: {.example title="Example 1"}
$$f(t)=\begin{cases}1&t\ge0\\ 0&t<0\end{cases}\ \Longrightarrow\ \mathcal{L}\{f(t)\}=F(s)=\;?$$

::: {.solution}
$$\mathcal{L}\{f(t)\}=\int_0^\infty1\times e^{-st}\,dt=-\frac1se^{-st}\Big|_0^\infty=\frac1s$$
:::
:::

::: {.example title="Example 2"}
$$f(t)=\begin{cases}e^{at}&t\ge0\\ 0&t<0\end{cases}\ \Longrightarrow\ \mathcal{L}\{f(t)\}=F(s)=\;?$$

::: {.solution}
$$\mathcal{L}\{f(t)\}=\int_0^\infty e^{at}\times e^{-st}\,dt=\int_0^\infty e^{-(s-a)t}\,dt=-\frac1{s-a}e^{-(s-a)t}\Big|_0^\infty=\frac1{s-a}$$
:::
:::

::: {.example title="Example 3"}
::: {.solution}
$$\mathcal{L}\{\cosh(at)\}=\mathcal{L}\left\{\tfrac12e^{at}+\tfrac12e^{-at}\right\}=\tfrac12\mathcal{L}\{e^{at}\}+\tfrac12\mathcal{L}\{e^{-at}\}=\frac12\frac1{s-a}+\frac12\frac1{s+a}=\frac s{s^2-a^2}$$
:::
:::

::: {.example title="Example 4"}
::: {.solution}
$$\mathcal{L}\{\sinh(at)\}=\mathcal{L}\left\{\tfrac12e^{at}-\tfrac12e^{-at}\right\}=\tfrac12\mathcal{L}\{e^{at}\}-\tfrac12\mathcal{L}\{e^{-at}\}=\frac12\frac1{s-a}-\frac12\frac1{s+a}=\frac a{s^2-a^2}$$
:::
:::

::: {.example title="Example 5"}
::: {.solution}
Using $\displaystyle\int e^{ax}\cos nx\,dx=\frac{e^{ax}}{a^2+n^2}\big(a\cos nx+n\sin nx\big)$:
$$\mathcal{L}\{\cos\omega t\}=\int_0^\infty\cos\omega t\,e^{-st}\,dt=\frac{e^{-st}}{s^2+\omega^2}\big(-s\cos\omega t+\omega\sin\omega t\big)\Big|_0^\infty=\frac s{s^2+\omega^2}$$
:::
:::

::: {.example title="Example 6"}
::: {.solution}
Using $\displaystyle\int e^{ax}\sin nx\,dx=\frac{e^{ax}}{a^2+n^2}\big(a\sin nx-n\cos nx\big)$:
$$\mathcal{L}\{\sin\omega t\}=\int_0^\infty\sin\omega t\,e^{-st}\,dt=\frac{e^{-st}}{s^2+\omega^2}\big(-s\sin\omega t-\omega\cos\omega t\big)\Big|_0^\infty=\frac\omega{s^2+\omega^2}$$
:::
:::

### Table of Laplace Transforms (Table 6.1 of the textbook; a longer table is in Section 6.9)

| | $f(t)$ | $\mathcal{L}(f)$ | | | $f(t)$ | $\mathcal{L}(f)$ |
|:---:|:---:|:---:|---|:---:|:---:|:---:|
| 1 | $1$ | $\dfrac1s$ | | 7 | $\cos\omega t$ | $\dfrac{s}{s^2+\omega^2}$ |
| 2 | $t$ | $\dfrac1{s^2}$ | | 8 | $\sin\omega t$ | $\dfrac{\omega}{s^2+\omega^2}$ |
| 3 | $t^2$ | $\dfrac{2!}{s^3}$ | | 9 | $\cosh at$ | $\dfrac{s}{s^2-a^2}$ |
| 4 | $t^n$ $(n=0,1,\dots)$ | $\dfrac{n!}{s^{n+1}}$ | | 10 | $\sinh at$ | $\dfrac{a}{s^2-a^2}$ |
| 5 | $t^a$ ($a$ positive) | $\dfrac{\Gamma(a+1)}{s^{a+1}}$ | | 11 | $e^{at}\cos\omega t$ | $\dfrac{s-a}{(s-a)^2+\omega^2}$ |
| 6 | $e^{at}$ | $\dfrac1{s-a}$ | | 12 | $e^{at}\sin\omega t$ | $\dfrac{\omega}{(s-a)^2+\omega^2}$ |

$$\Gamma(x)=\int_0^\infty e^{-t}t^{x-1}\,dt$$

### Properties of the One-Sided Laplace Transform (the table of Section 6.8 of the textbook)

With the unit step function
$$u(t)\triangleq\begin{cases}1&t\ge0\\ 0&t<0\end{cases}$$

| Property | Formula |
|:---|:---:|
| Definition of the Laplace transform | $F(s)=\mathcal{L}\{f(t)\}\triangleq\displaystyle\int_0^\infty f(t)e^{-st}\,dt$ |
| Inverse Laplace transform | $f(t)=\mathcal{L}^{-1}\{F(s)\}$ |
| Linearity | $\mathcal{L}\{af(t)+bg(t)\}=a\mathcal{L}\{f(t)\}+b\mathcal{L}\{g(t)\}$ |
| Time shift | $\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$ |
| Shift in the $s$ domain | $\mathcal{L}\{e^{at}f(t)\}=F(s-a)$ |
| Time scaling | $\mathcal{L}\{f(at)\}=\dfrac1aF\!\left(\frac sa\right)$ |
| Time derivative | $\mathcal{L}\{f^{(n)}(t)\}=s^nF(s)-s^{n-1}f(0)-s^{n-2}f^{(1)}(0)-\cdots-f^{(n-1)}(0)$ |
| Time integral | $\mathcal{L}\left\{\displaystyle\int_0^tf(\tau)\,d\tau\right\}=\dfrac1sF(s)$ |
| Derivative in the $s$ domain | $\mathcal{L}\{tf(t)\}=-F'(s)$ |
| Integral in the $s$ domain | $\mathcal{L}\left\{\dfrac{f(t)}t\right\}=\displaystyle\int_s^\infty F(\nu)\,d\nu$ |

## Using the Laplace Transform to Solve Differential Equations

The steps for solving a differential equation with initial conditions using the Laplace transform:

1. convert the initial-value problem into an algebraic problem;
2. compute the solution of the algebraic problem;
3. solve the initial-value problem (return the solution to the time domain).

```{.figure #m07-solve-scheme caption="The steps of solving an initial-value problem with the Laplace transform: initial-value problem $\\xrightarrow{1}$ algebraic problem $\\xrightarrow{2}$ solution of the algebraic problem $\\xrightarrow{3}$ solution of the initial-value problem"}
```

### Ordinary Differential Equations

::: {.example}
Solve the differential equation $y''-y=t$, $y(0)=1$, $y'(0)=1$ using the Laplace transform.

::: {.solution}
$$s^2Y-sy(0)-y'(0)-Y=\frac1{s^2}\ \Longrightarrow\ (s^2-1)Y(s)=s+1+\frac1{s^2}$$
$$Y(s)=\frac{s+1}{s^2-1}+\frac1{s^2(s^2-1)}=\frac1{s-1}+\left(\frac1{s^2-1}-\frac1{s^2}\right)$$
$$y(t)=\mathcal{L}^{-1}\{Y(s)\}=\mathcal{L}^{-1}\left\{\frac1{s-1}\right\}+\mathcal{L}^{-1}\left\{\frac1{s^2-1}\right\}-\mathcal{L}^{-1}\left\{\frac1{s^2}\right\}=e^tu(t)+\sinh t\,u(t)-t\,u(t)$$
:::
:::

### Partial Differential Equations

::: {.example}
Solve the following partial differential equation using the Laplace transform.
$$\frac{\partial w}{\partial x}+x\frac{\partial w}{\partial t}=0,\qquad w(x,0)=0,\qquad w(0,t)=t\,u(t)$$

::: {.solution}
We take the Laplace transform of both sides with respect to $t$:
$$\mathcal{L}_t\left\{\frac{\partial w}{\partial x}+x\frac{\partial w}{\partial t}\right\}=\mathcal{L}_t\left\{\frac{\partial w}{\partial x}\right\}+x\,\mathcal{L}_t\left\{\frac{\partial w}{\partial t}\right\}=0$$
$$\frac\partial{\partial x}w(x,s)+x\big[s\,w(x,s)-w(x,0)\big]=0,\qquad w(x,0)=0$$
$$\frac\partial{\partial x}w(x,s)+xs\,w(x,s)=0\ \Rightarrow\ \frac{dw}w=-sx\,dx\ \Rightarrow\ \ln w=-s\frac{x^2}2+\ln C\ \Rightarrow\ w(x,s)=Ce^{-\frac{x^2}2s}$$
From $w(0,t)=t\,u(t)$ we have $w(0,s)=\mathcal{L}\{w(0,t)\}=\frac1{s^2}=C$:
$$w(x,s)=\frac1{s^2}e^{-\frac{x^2}2s}$$
Using the time-shift property $\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$:
$$w(x,t)=\left(t-\frac{x^2}2\right)\times u\!\left(t-\frac{x^2}2\right)$$
:::
:::
