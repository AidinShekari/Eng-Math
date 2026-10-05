# d'Alembert's Method and the One-Dimensional Heat Equation

## d'Alembert's Method for the One-Dimensional Wave Equation

$$\begin{cases}\dfrac{\partial^2u}{\partial t^2}=c^2\dfrac{\partial^2u}{\partial x^2}\\[2mm] u(0,t)=u(L,t)=0\\ u(x,0)=f(x)\\ u_t(x,0)=g(x)\end{cases}$$
We rewrite and solve the equation using the following change of variables.
$$u(x,t)\Rightarrow u(\varphi,\psi),\qquad\begin{cases}\varphi=x+ct\\ \psi=x-ct\end{cases}$$
$$\frac{\partial u}{\partial x}=\frac{\partial u}{\partial\varphi}\frac{\partial\varphi}{\partial x}+\frac{\partial u}{\partial\psi}\frac{\partial\psi}{\partial x}=\frac{\partial u}{\partial\varphi}+\frac{\partial u}{\partial\psi}$$
$$\frac{\partial u}{\partial t}=\frac{\partial u}{\partial\varphi}\frac{\partial\varphi}{\partial t}+\frac{\partial u}{\partial\psi}\frac{\partial\psi}{\partial t}=c\frac{\partial u}{\partial\varphi}-c\frac{\partial u}{\partial\psi}$$
$$\frac{\partial^2u}{\partial x^2}=\frac\partial{\partial x}\left(\frac{\partial u}{\partial\varphi}+\frac{\partial u}{\partial\psi}\right)=\left(\frac{\partial^2u}{\partial\varphi^2}+\frac{\partial^2u}{\partial\varphi\partial\psi}\right)\cdot1+\left(\frac{\partial^2u}{\partial\psi\partial\varphi}+\frac{\partial^2u}{\partial\psi^2}\right)\cdot1=\frac{\partial^2u}{\partial\varphi^2}+2\frac{\partial^2u}{\partial\varphi\partial\psi}+\frac{\partial^2u}{\partial\psi^2}$$
(using $\dfrac{\partial^2u}{\partial\varphi\partial\psi}=\dfrac{\partial^2u}{\partial\psi\partial\varphi}$.)

::: {.exercise}
In the same way, prove the identity
$$\frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial\varphi^2}-2\frac{\partial^2u}{\partial\varphi\partial\psi}+\frac{\partial^2u}{\partial\psi^2}\right)$$
:::

Substituting the two relations above into the one-dimensional wave equation:
$$c^2\left(\frac{\partial^2u}{\partial\varphi^2}-2\frac{\partial^2u}{\partial\varphi\partial\psi}+\frac{\partial^2u}{\partial\psi^2}\right)=c^2\left(\frac{\partial^2u}{\partial\varphi^2}+2\frac{\partial^2u}{\partial\varphi\partial\psi}+\frac{\partial^2u}{\partial\psi^2}\right)\quad\Longrightarrow\quad\frac{\partial^2u}{\partial\varphi\partial\psi}=0$$

**The general solution:**
$$\frac{\partial u}{\partial\varphi}=\phi_1(\varphi)\ \Rightarrow\ u(\varphi,\psi)=\int\phi_1(\varphi)\,d\varphi+\Psi(\psi)=\Phi(\varphi)+\Psi(\psi)\quad\Longrightarrow\quad u(x,t)=\Phi(x+ct)+\Psi(x-ct)$$

**Applying the initial conditions:**
$$u(x,0)=\Phi(x)+\Psi(x)=f(x)$$
$$u_t(x,t)=\frac{\partial\Phi}{\partial\varphi}\frac{\partial\varphi}{\partial t}+\frac{\partial\Psi}{\partial\psi}\frac{\partial\psi}{\partial t}=c\Phi'(\varphi)-c\Psi'(\psi)=c\Phi'(x+ct)-c\Psi'(x-ct)$$
$$u_t(x,0)=c\Phi'(x)-c\Psi'(x)=c\big[\Phi'(x)-\Psi'(x)\big]=g(x)$$
$$\begin{cases}\Phi(x)+\Psi(x)=f(x)\\ \Phi'(x)-\Psi'(x)=\dfrac1cg(x)\end{cases}\Rightarrow\begin{cases}\Phi'(x)+\Psi'(x)=f'(x)\\ \Phi'(x)-\Psi'(x)=\dfrac1cg(x)\end{cases}\Rightarrow\begin{cases}\Phi'(x)=\dfrac12f'(x)+\dfrac1{2c}g(x)\\[2mm] \Psi'(x)=\dfrac12f'(x)-\dfrac1{2c}g(x)\end{cases}$$
$$\begin{cases}\Phi(x)=\dfrac12f(x)+\dfrac1{2c}\displaystyle\int_0^xg(s)\,ds+k_1\\[2mm] \Psi(x)=\dfrac12f(x)-\dfrac1{2c}\displaystyle\int_0^xg(s)\,ds+k_2\end{cases}$$
$$u(x,t)=\frac12\left(f(x+ct)+\frac1c\int_0^{x+ct}g(s)\,ds\right)+\frac12\left(f(x-ct)-\frac1c\int_0^{x-ct}g(s)\,ds\right)+k_1+k_2$$

::: {.important title="d'Alembert's formula"}
$$u(x,t)=\frac12\Big[f(x+ct)+f(x-ct)\Big]+\frac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds+K,\qquad u(0,0)=0\ \Rightarrow\ K=0$$
$$u(x,t)=\frac12\Big[f(x+ct)+f(x-ct)\Big]+\frac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds$$
:::

::: {.exercise}
Prove that if the boundary conditions are to hold, the functions $f(x)$ and $g(x)$ in the formula above must both be periodic with period $2L$ and odd.
:::

## The Heat Equation

$$\frac{\partial u}{\partial t}=c^2\frac{\partial^2u}{\partial x^2},\qquad \frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right),\qquad \frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}\right)$$

### The One-Dimensional Heat Equation

```{.figure #m05-rod caption="A one-dimensional rod $0\\le x\\le L$ with temperature distribution $u(x,t)$"}
```

For a unique solution we need boundary conditions and initial conditions:

- Boundary conditions: $u(0,t)=u(L,t)=0$
- Initial conditions: $u(x,0)=f(x)$

## Solving the One-Dimensional Heat Equation

$$\begin{cases}\dfrac{\partial u}{\partial t}=c^2\dfrac{\partial^2u}{\partial x^2}\\[2mm] u(0,t)=u(L,t)=0\\ u(x,0)=f(x)\end{cases}$$
Here we solve the equation by **separation of variables**. Assume $u(x,t)=X(x)\times T(t)$.
$$\frac{\partial^2u}{\partial x^2}=X''(x)T(t),\qquad \frac{\partial u}{\partial t}=X(x)T'(t)\quad\Longrightarrow\quad X(x)T'(t)=c^2X''(x)T(t)\quad\Longrightarrow\quad\frac{T'}{c^2T}=\frac{X''}X=k$$
$k$ must necessarily be negative (for $k=0$ and $k>0$ one gets $X(x)=0$ exactly as in the wave problem). With $k=-\lambda^2$:
$$\frac{T'}{c^2T}=\frac{X''}X=-\lambda^2\quad\Longrightarrow\quad\begin{cases}X''+\lambda^2X=0\\ T'+c^2\lambda^2T=0\end{cases}$$
$$X(x)=A\cos\lambda x+B\sin\lambda x,\quad X(0)=0\Rightarrow A=0,\qquad X(L)=0\Rightarrow B\sin\lambda L=0\Rightarrow\lambda=\frac{n\pi}L=\lambda_n$$
$$X_n(x)=B_n\sin\lambda_nx,\qquad T'+c^2\lambda_n^2T=0\ \Rightarrow\ T_n(t)=C_ne^{-(c\lambda_n)^2t}$$
$$u_n(x,t)=X_n(x)\times T_n(t)=B_n\sin\!\left(\frac{n\pi}Lx\right)\times C_ne^{-\left(\frac{cn\pi}L\right)^2t}$$
$$u(x,t)=\sum_{n=1}^{\infty}A_ne^{-(c\lambda_n)^2t}\sin(\lambda_nx),\qquad \lambda_n=\frac{n\pi}L$$
The initial condition $u(x,0)=f(x)$:
$$u(x,0)=\sum_{n=1}^{\infty}A_n\sin\lambda_nx=f(x)$$
$f(x)$ has been set equal to a periodic odd function, so to compute the unknown Fourier coefficients we must regard $f(x)$ as a periodic odd function (with period $2L$):
$$A_n=\frac2{2L}\int_{-L}^{L}f(x)\sin\!\left(\frac{2\pi}{2L}nx\right)dx=\frac1L\int_{-L}^{L}f(x)\sin\!\left(\frac{n\pi}Lx\right)dx=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx$$

::: {.important title="Solution of the one-dimensional heat equation (separation of variables)"}
$$u(x,t)=\sum_{n=1}^{\infty}A_ne^{-(c\lambda_n)^2t}\sin(\lambda_nx),\qquad \lambda_n=\frac{n\pi}L,\qquad A_n=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx$$
:::

::: {.example title="Example 1"}
Find the solution of the following one-dimensional heat equation.
$$\frac{\partial u}{\partial t}=\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=u(10,t)=0,\qquad u(x,0)=f(x)=\begin{cases}x&0\le x<5\\ 10-x&5\le x\le10\end{cases}$$

::: {.solution}
$$\begin{aligned}
A_n&=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx=0.2\int_0^5x\sin\!\left(\frac{n\pi}{10}x\right)dx+0.2\int_5^{10}(10-x)\sin\!\left(\frac{n\pi}{10}x\right)dx\\
&=0.2\left[(x)\left(\frac{-10}{n\pi}\cos\frac{n\pi}{10}x\right)-(1)\left(\frac{-100}{n^2\pi^2}\sin\frac{n\pi}{10}x\right)\right]_0^5\\
&\quad+0.2\left[(10-x)\left(\frac{-10}{n\pi}\cos\frac{n\pi}{10}x\right)-(-1)\left(\frac{-100}{n^2\pi^2}\sin\frac{n\pi}{10}x\right)\right]_5^{10}=\frac{40}{n^2\pi^2}\sin\frac{n\pi}2
\end{aligned}$$
$$u(x,t)=\sum_{n=1}^{\infty}\left(\frac{40}{n^2\pi^2}\sin\frac{n\pi}2\right)e^{-\left(\frac{cn\pi}{10}\right)^2t}\sin\!\left(\frac{n\pi}{10}x\right)$$
(with $c=1$.)
:::
:::

::: {.example title="Example 2 (nonzero boundary values)"}
Find the solution of the following one-dimensional heat equation.
$$\frac{\partial u}{\partial t}=c^2\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=T_0,\qquad u(L,t)=T_1,\qquad u(x,0)=f(x)$$

::: {.solution}
$$u(x,t)=w(x,t)+v(x)\quad\Longrightarrow\quad\begin{cases}w(0,t)+v(0)=T_0\\ w(L,t)+v(L)=T_1\end{cases}$$
$$\frac{\partial w}{\partial t}=c^2\left(\frac{\partial^2w}{\partial x^2}+\frac{\partial^2v}{\partial x^2}\right)$$
$$\begin{cases}\dfrac{\partial^2v}{\partial x^2}=0\\ v(0)=T_0\\ v(L)=T_1\end{cases}\Rightarrow\ v(x)=\left(\frac{T_1-T_0}L\right)x+T_0,\qquad\begin{cases}\dfrac{\partial w}{\partial t}=c^2\dfrac{\partial^2w}{\partial x^2}\\ w(0,t)=w(L,t)=0\end{cases}\Rightarrow\ w(x,t)=\sum_{n=1}^{\infty}A_ne^{-(c\lambda_n)^2t}\sin(\lambda_nx)$$
$$u(x,t)=\underbrace{\sum_{n=1}^{\infty}A_ne^{-(c\lambda_n)^2t}\sin(\lambda_nx)}_{w(x,t)}+\underbrace{\left(\frac{T_1-T_0}L\right)x+T_0}_{v(x)},\qquad \lambda_n=\frac{n\pi}L$$
The initial condition:
$$\sum_{n=1}^{\infty}A_n\sin\frac{n\pi}Lx=f(x)-\left(\frac{T_1-T_0}L\right)x-T_0\triangleq f_1(x)\ \Longrightarrow\ A_n=\frac2L\int_0^L\left[f(x)-\left(\frac{T_1-T_0}L\right)x-T_0\right]\sin\frac{n\pi}Lx\,dx$$
:::
:::

::: {.example title="Example 3 (insulated ends)"}
Find the solution of the following one-dimensional heat equation.
$$\frac{\partial u}{\partial t}=c^2\frac{\partial^2u}{\partial x^2},\qquad u_x(0,t)=u_x(L,t)=0,\qquad u(x,0)=f(x)$$

::: {.solution}
We solve this problem by **separation of variables**: $u(x,t)=X(x)\times T(t)$.
$$\frac{T'}{c^2T}=\frac{X''}X=-\lambda^2\ \Rightarrow\ \begin{cases}X''+\lambda^2X=0\ \Rightarrow\ X(x)=A\cos\lambda x+B\sin\lambda x\\ T'+c^2\lambda^2T=0\end{cases}$$
$$X'(x)=-A\lambda\sin\lambda x+B\lambda\cos\lambda x,\qquad X'(0)=0\Rightarrow B=0,\qquad X'(L)=0\Rightarrow-A\lambda\sin\lambda L=0\Rightarrow\lambda L=n\pi\Rightarrow\lambda_n=\frac{n\pi}L$$
$$X_n(x)=A_n\cos\lambda_nx,\qquad T_n(t)=C_ne^{-(c\lambda_n)^2t}$$
$$u(x,t)=\sum_{n=1}^{\infty}B_ne^{-(c\lambda_n)^2t}\cos(\lambda_nx),\qquad \lambda_n=\frac{n\pi}L$$
The initial condition $u(x,0)=\sum_{n=1}^{\infty}B_n\cos\!\left(\dfrac{n\pi}Lx\right)=f(x)$ gives
$$B_n=\frac2L\int_0^Lf(x)\cos\!\left(\frac{n\pi}Lx\right)dx$$
:::
:::

## The One-Dimensional Heat Equation on an Infinite Rod

$$\begin{cases}\dfrac{\partial u}{\partial t}=c^2\dfrac{\partial^2u}{\partial x^2}\\[2mm] u(\infty,t)=u(-\infty,t)=0\\ u(x,0)=f(x),\quad-\infty<x<\infty\end{cases}$$
Assuming $u(x,t)=X(x)\times T(t)$:
$$X(x)T'(t)=c^2X''(x)T(t)\ \Rightarrow\ \frac{T'}{c^2T}=\frac{X''}X=-\lambda^2\ \Rightarrow\ \begin{cases}X(x)=A_1(\lambda)\cos\lambda x+B_1(\lambda)\sin\lambda x=X_\lambda(x)\\ T(t)=C_1(\lambda)e^{-c^2\lambda^2t}=T_\lambda(t)\end{cases}$$
$$u_\lambda(x,t)=\big[A(\lambda)\cos\lambda x+B(\lambda)\sin\lambda x\big]e^{-c^2\lambda^2t}\quad\Longrightarrow\quad u(x,t)=\frac1\pi\int_0^\infty\big[A(\lambda)\cos\lambda x+B(\lambda)\sin\lambda x\big]e^{-c^2\lambda^2t}\,d\lambda$$
Checking the equation:
$$\frac{\partial^2u}{\partial x^2}=\frac1\pi\int_0^\infty-\lambda^2\big[A\cos\lambda x+B\sin\lambda x\big]e^{-c^2\lambda^2t}\,d\lambda,\qquad \frac{\partial u}{\partial t}=\frac1\pi\int_0^\infty-c^2\lambda^2\big[A\cos\lambda x+B\sin\lambda x\big]e^{-c^2\lambda^2t}\,d\lambda\ \Rightarrow\ \frac{\partial u}{\partial t}=c^2\frac{\partial^2u}{\partial x^2}\ \checkmark$$
**Applying the initial condition:** $u(x,0)=\dfrac1\pi\displaystyle\int_0^\infty\big[A(\lambda)\cos\lambda x+B(\lambda)\sin\lambda x\big]d\lambda=f(x)$, i.e. the Fourier integral (Chapter 3):
$$A(\lambda)=\mathfrak{I}_C\{f(x)\}=\int_{-\infty}^{\infty}f(x)\cos\lambda x\,dx,\qquad B(\lambda)=\mathfrak{I}_S\{f(x)\}=\int_{-\infty}^{\infty}f(x)\sin\lambda x\,dx$$
$$\begin{aligned}
u(x,t)&=\frac1\pi\int_0^\infty\left[\left(\int_{-\infty}^{\infty}f(\nu)\cos\lambda\nu\,d\nu\right)\cos\lambda x+\left(\int_{-\infty}^{\infty}f(\nu)\sin\lambda\nu\,d\nu\right)\sin\lambda x\right]e^{-c^2\lambda^2t}\,d\lambda\\
&=\frac1\pi\int_0^\infty\left\{\int_{-\infty}^{\infty}f(\nu)\big[\cos\lambda\nu\cos\lambda x+\sin\lambda\nu\sin\lambda x\big]d\nu\right\}e^{-c^2\lambda^2t}\,d\lambda\\
&=\frac1\pi\int_0^\infty\left\{\int_{-\infty}^{\infty}f(\nu)\cos\lambda(x-\nu)\,d\nu\right\}e^{-c^2\lambda^2t}\,d\lambda
\end{aligned}$$

::: {.important title="First form of the solution"}
$$u(x,t)=\frac1\pi\int_{-\infty}^{\infty}f(\nu)\left\{\int_0^\infty e^{-c^2\lambda^2t}\cos\lambda(x-\nu)\,d\lambda\right\}d\nu$$
:::

### Mathematical Lemmas

::: {.theorem title="Lemma (a)"}
$$I=\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt\pi}2$$
:::

::: {.proof}
$$I^2=\int_0^\infty e^{-x^2}dx\times\int_0^\infty e^{-y^2}dy=\int_0^\infty\!\!\int_0^\infty e^{-(x^2+y^2)}\,dx\,dy\ \overset{\rho^2=x^2+y^2}{=}\ \int_0^{\pi/2}\!\!\int_0^\infty\rho\,e^{-\rho^2}\,d\rho\,d\theta=\int_0^{\pi/2}\left[\frac{-1}2e^{-\rho^2}\right]_0^\infty d\theta=\frac\pi4$$
:::

::: {.theorem title="Lemma (b)"}
$$\int_0^\infty e^{-s^2}\cos(2bs)\,ds=\frac{\sqrt\pi}2e^{-b^2}$$
:::

::: {.proof}
$$I(b)=\int_0^\infty e^{-s^2}\cos(2bs)\,ds\ \Rightarrow\ \frac{dI(b)}{db}=-\int_0^\infty2se^{-s^2}\sin(2bs)\,ds$$
Integrating by parts ($du=-2se^{-s^2}ds$, $v=\sin2bs$):
$$\frac{dI(b)}{db}=e^{-s^2}\sin2bs\Big|_0^\infty-2b\int_0^\infty e^{-s^2}\cos2bs\,ds=-2b\,I(b)\ \Rightarrow\ I(b)=ke^{-b^2},\qquad I(0)=k=\int_0^\infty e^{-s^2}ds=\frac{\sqrt\pi}2$$
:::

With the substitution $c\lambda\sqrt t=s$:
$$\int_0^\infty e^{-c^2\lambda^2t}\cos\lambda(x-\nu)\,d\lambda=\frac1{c\sqrt t}\int_0^\infty e^{-s^2}\cos\!\left[2\frac{(x-\nu)}{2c\sqrt t}s\right]ds=\frac1{c\sqrt t}\frac{\sqrt\pi}2e^{-\left(\frac{x-\nu}{2c\sqrt t}\right)^2}$$

::: {.important title="Second form of the solution"}
$$u(x,t)=\frac1{2c\sqrt{\pi t}}\int_{-\infty}^{\infty}f(\nu)\,e^{-\frac{(x-\nu)^2}{4c^2t}}\,d\nu$$
:::

With the substitution $z=\dfrac{\nu-x}{2c\sqrt t}$ (i.e. $\nu=x+2c\sqrt t\,z$ and $d\nu=2c\sqrt t\,dz$):

::: {.important title="Third form of the solution"}
$$u(x,t)=\frac1{\sqrt\pi}\int_{-\infty}^{\infty}f\big(x+2c\sqrt t\,z\big)\,e^{-z^2}\,dz$$
:::

## The Error Function

In mathematics the error function is most often defined as
$$\operatorname{erf}(x)\triangleq\frac2{\sqrt\pi}\int_0^xe^{-t^2}\,dt$$
Properties of the error function:

- odd symmetry: $\operatorname{erf}(-x)=-\operatorname{erf}(x)$
- asymptotic property: $\operatorname{erf}(\infty)=1$
- its Maclaurin expansion is given below (start from the expansion of $e^x$ and prove this identity):
$$\operatorname{erf}(x)=\frac2{\sqrt\pi}\left[x-\frac{x^3}{1!\times3}+\frac{x^5}{2!\times5}-\frac{x^7}{3!\times7}+-\cdots\right]=\frac2{\sqrt\pi}\sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^{2n-1}}{(n-1)!\,(2n-1)}$$

```{.figure #m05-erf caption="The graph of the error function $\\operatorname{erf}(x)$ for $-2\\le x\\le2$"}
```

::: {.example title="Example 1"}
Find the solution of the equation above for the following initial condition.
$$f(x)=\begin{cases}U_0&|x|<1\\ 0&|x|\ge1\end{cases}$$

::: {.solution}
We use the second form of the solution:
$$u(x,t)=\frac{U_0}{2c\sqrt{\pi t}}\int_{-1}^{1}e^{-\frac{(x-\nu)^2}{4c^2t}}\,d\nu\ \overset{z=\frac{\nu-x}{2c\sqrt t}}{=}\ \frac{U_0}{\sqrt\pi}\int_{-\frac{1+x}{2c\sqrt t}}^{\frac{1-x}{2c\sqrt t}}e^{-z^2}\,dz$$
$$=\frac{U_0}{\sqrt\pi}\left\{\int_{-\frac{1+x}{2c\sqrt t}}^{0}e^{-z^2}dz+\int_0^{\frac{1-x}{2c\sqrt t}}e^{-z^2}dz\right\}=\frac{U_0}{\sqrt\pi}\frac{\sqrt\pi}2\left\{\frac2{\sqrt\pi}\int_0^{\frac{1+x}{2c\sqrt t}}e^{-z^2}dz+\frac2{\sqrt\pi}\int_0^{\frac{1-x}{2c\sqrt t}}e^{-z^2}dz\right\}$$
$$u(x,t)=\frac{U_0}2\left[\operatorname{erf}\!\left(\frac{1+x}{2c\sqrt t}\right)+\operatorname{erf}\!\left(\frac{1-x}{2c\sqrt t}\right)\right]$$
:::
:::

```{.figure #m05-heat-pulse caption="The temperature distribution $u(x,t)$ at $t=0$, $\\frac18$, $\\frac12$, $1$, $2$ and $8$ for the initial pulse $U_0=100$ and $c=1$"}
```

::: {.example title="Example 2"}
Find the solution of the equation above for the following initial condition.
$$f(x)=\begin{cases}1&x>0\\ 0&x\le0\end{cases}$$

::: {.solution}
We use the second form of the solution:
$$u(x,t)=\frac1{2c\sqrt{\pi t}}\int_0^\infty e^{-\frac{(x-\nu)^2}{4c^2t}}\,d\nu\ \overset{z=\frac{\nu-x}{2c\sqrt t}}{=}\ \frac1{\sqrt\pi}\int_{-\frac x{2c\sqrt t}}^{\infty}e^{-z^2}\,dz=\frac1{\sqrt\pi}\left\{\int_{-\frac x{2c\sqrt t}}^{0}e^{-z^2}dz+\int_0^\infty e^{-z^2}dz\right\}$$
$$u(x,t)=\frac12\left[\operatorname{erf}\!\left(\frac x{2c\sqrt t}\right)+1\right]$$
:::
:::
