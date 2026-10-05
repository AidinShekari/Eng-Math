# Two-Dimensional Wave and Heat Equations: Rectangle and Disc

## The Two-Dimensional Wave Equation

Modelling a vibrating membrane (deriving the equation governing $u(x,y,t)$).

**Physical assumptions:**

- The mass is distributed uniformly over the membrane (a homogeneous membrane), and the membrane is perfectly flexible.
- The membrane is stretched so tightly that the force of gravity on it is negligible.
- The deflection of the membrane from equilibrium is very small.

```{.figure #m06-membrane caption="An element $\\Delta x\\times\\Delta y$ of the vibrating membrane and the tensile forces $T\\Delta x$ and $T\\Delta y$ acting on it"}
```

By a modelling process analogous to the one-dimensional case, the equation of the vibrating two-dimensional membrane is obtained:
$$\frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)=c^2\nabla^2u$$
For a unique solution we need boundary conditions and initial conditions:

- Boundary conditions: $u(x,y,t)=0$ on the boundary of the membrane
- Initial conditions: $u(x,y,0)=f(x,y)$ and $u_t(x,y,0)=g(x,y)$, where $u_t\triangleq\dfrac{\partial u}{\partial t}$

## The Two-Dimensional Wave Equation with a Rectangular Boundary

```{.figure #m06-rectangle caption="The rectangular region $0\\le x\\le a$, $0\\le y\\le b$"}
```

$$\frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)$$

- Boundary conditions: $u(0,y,t)=u(a,y,t)=0$ and $u(x,0,t)=u(x,b,t)=0$
- Initial conditions: $u(x,y,0)=f(x,y)$ and $u_t(x,y,0)=g(x,y)$

### Solving the Equation

Here we solve the equation by **separation of variables**. Assume $u(x,y,t)=X(x)\times Y(y)\times T(t)$.
$$\frac{\partial^2u}{\partial x^2}=X''YT,\qquad\frac{\partial^2u}{\partial y^2}=XY''T,\qquad\frac{\partial^2u}{\partial t^2}=XYT''\quad\Longrightarrow\quad XYT''=c^2\big(X''YT+XY''T\big)$$
$$\frac{T''}{c^2T}=\frac{X''}X+\frac{Y''}Y=-\lambda^2\ \Rightarrow\ \frac{Y''}Y=-\lambda^2-\frac{X''}X=-\rho^2\ \Rightarrow\ \frac{X''}X=-\lambda^2+\rho^2=-\mu^2$$
$$\begin{cases}X''+\mu^2X=0\\ Y''+\rho^2Y=0\\ T''+c^2\lambda^2T=0\end{cases}\qquad\lambda^2=\mu^2+\rho^2$$
**The solution in the $x$ direction:**
$$X(x)=A_1\cos\mu x+A_2\sin\mu x,\quad X(0)=0\Rightarrow A_1=0,\quad X(a)=0\Rightarrow A_2\sin\mu a=0\Rightarrow\mu a=n\pi\Rightarrow\mu_n=\frac{n\pi}a$$
$$X_n(x)=A_n\sin\mu_nx,\qquad \mu_n=\frac{n\pi}a$$
**The solution in the $y$ direction:**
$$Y(y)=B_1\cos\rho y+B_2\sin\rho y,\quad Y(0)=0\Rightarrow B_1=0,\quad Y(b)=0\Rightarrow B_2\sin\rho b=0\Rightarrow\rho b=m\pi\Rightarrow\rho_m=\frac{m\pi}b$$
$$Y_m(y)=B_m\sin\rho_my,\qquad \rho_m=\frac{m\pi}b$$
**The solution in time:**
$$\lambda_{nm}^2=\mu_n^2+\rho_m^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2,\qquad T_{nm}(t)=C_1\cos(c\lambda_{nm}t)+C_2\sin(c\lambda_{nm}t)$$
$$u_{nm}(x,y,t)=\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right),\qquad n,m=1,2,\dots$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)$$

**Applying the initial condition $u(x,y,0)=f(x,y)$:**
$$f(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)=\sum_{n=1}^{\infty}K_n(y)\sin\frac{n\pi}ax,\qquad K_n(y)\triangleq\sum_{m=1}^{\infty}A_{nm}\sin\frac{m\pi}by$$
$$K_n(y)=\frac2a\int_0^af(x,y)\sin\frac{n\pi}ax\,dx,\qquad A_{nm}=\frac2b\int_0^bK_n(y)\sin\frac{m\pi}by\,dy$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$

::: {.exercise}
Prove that
$$B_{nm}=\frac4{abc\lambda_{nm}}\int_0^b\left\{\int_0^ag(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$
:::

::: {.important title="Solution of the two-dimensional wave equation on a rectangle"}
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right),\qquad\lambda_{nm}^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy,\qquad B_{nm}=\frac4{abc\lambda_{nm}}\int_0^b\left\{\int_0^ag(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$
:::

::: {.example}
Find the solution of the two-dimensional motion equation above for $g(x,y)=0$ and $f(x,y)=xy$.

::: {.solution}
$$g(x,y)=0\ \Rightarrow\ B_{nm}=0$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^axy\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy=\frac4{ab}\left\{\left[\int_0^by\sin\frac{m\pi}by\,dy\right]\times\left[\int_0^ax\sin\frac{n\pi}ax\,dx\right]\right\}$$
$$=\frac4{ab}\left[y\left(\frac{-b}{m\pi}\cos\frac{m\pi}by\right)-(1)\left(\frac{-b^2}{m^2\pi^2}\sin\frac{m\pi}by\right)\right]_0^b\times\left[x\left(\frac{-a}{n\pi}\cos\frac{n\pi}ax\right)-(1)\left(\frac{-a^2}{n^2\pi^2}\sin\frac{n\pi}ax\right)\right]_0^a$$
$$=\frac4{ab}\cdot\frac{-b^2}{m\pi}(-1)^m\cdot\frac{-a^2}{n\pi}(-1)^n=\frac{4ab}{nm\pi^2}(-1)^{n+m}$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\frac{4ab}{nm\pi^2}(-1)^{n+m}\cos(c\lambda_{nm}t)\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)$$
:::
:::

## The Two-Dimensional Heat Equation with a Rectangular Boundary

$$\frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)=c^2\nabla^2u$$

- Boundary condition: $u(x,y,t)=0$ on the boundary of the plate
- Initial condition: $u(x,y,0)=f(x,y)$

### Solving the Equation

Assume $u(x,y,t)=X(x)\times Y(y)\times T(t)$.
$$\frac{\partial^2u}{\partial x^2}=X''YT,\qquad\frac{\partial^2u}{\partial y^2}=XY''T,\qquad\frac{\partial u}{\partial t}=XYT'\quad\Longrightarrow\quad XYT'=c^2\big(X''YT+XY''T\big)$$
$$\frac{T'}{c^2T}=\frac{X''}X+\frac{Y''}Y=-\lambda^2,\qquad \frac{Y''}Y=-\lambda^2-\frac{X''}X=-\rho^2,\qquad\frac{X''}X=-\lambda^2+\rho^2=-\mu^2$$
$$\begin{cases}X''+\mu^2X=0\\ Y''+\rho^2Y=0\\ T'+c^2\lambda^2T=0\end{cases}\qquad\lambda^2=\mu^2+\rho^2$$
As in the wave case ($X_n(x)=A_n\sin\mu_nx$ with $\mu_n=\frac{n\pi}a$ and $Y_m(y)=B_m\sin\rho_my$ with $\rho_m=\frac{m\pi}b$), and with
$$T_{nm}(t)=C_1e^{-c^2\lambda_{nm}^2t},\qquad\lambda_{nm}^2=\mu_n^2+\rho_m^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2$$
$$u_{nm}(x,y,t)=A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)e^{-c^2\lambda_{nm}^2t},\qquad n=1,2,\dots,\ m=1,2,\dots$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)e^{-c^2\lambda_{nm}^2t}$$
**Applying the initial condition:** exactly as in the wave case,
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$

## The Laplacian in Polar Coordinates

The aim is to write $\nabla^2u=u_{xx}+u_{yy}$ in polar coordinates in terms of $r,\theta$.

```{.figure #m06-polar caption="Polar coordinates: $x=r\\cos\\theta$, $y=r\\sin\\theta$"}
```

$$r=\sqrt{x^2+y^2},\quad x=r\cos\theta,\qquad\theta=\tan^{-1}\!\left(\frac yx\right),\quad y=r\sin\theta$$
$$u_x=u_rr_x+u_\theta\theta_x\ \Rightarrow\ u_{xx}=\big(u_rr_x+u_\theta\theta_x\big)_x=u_{rr}r_x^2+u_{\theta\theta}\theta_x^2+2r_x\theta_xu_{r\theta}+r_{xx}u_r+\theta_{xx}u_\theta$$
$$u_y=u_rr_y+u_\theta\theta_y\ \Rightarrow\ u_{yy}=u_{rr}r_y^2+u_{\theta\theta}\theta_y^2+2r_y\theta_yu_{r\theta}+r_{yy}u_r+\theta_{yy}u_\theta$$
$$r_x=\frac xr,\quad r_{xx}=\frac{y^2}{r^3},\quad\theta_x=\frac{-y}{r^2},\quad\theta_{xx}=\frac{2xy}{r^4},\qquad r_y=\frac yr,\quad r_{yy}=\frac{x^2}{r^3},\quad\theta_y=\frac x{r^2},\quad\theta_{yy}=\frac{-2xy}{r^4}$$
$$u_{xx}=\frac{x^2}{r^2}u_{rr}+\frac{y^2}{r^4}u_{\theta\theta}+\frac{-2xy}{r^3}u_{r\theta}+\frac{y^2}{r^3}u_r+\frac{2xy}{r^4}u_\theta$$
$$u_{yy}=\frac{y^2}{r^2}u_{rr}+\frac{x^2}{r^4}u_{\theta\theta}+\frac{2xy}{r^3}u_{r\theta}+\frac{x^2}{r^3}u_r+\frac{-2xy}{r^4}u_\theta$$
Adding these two relations:

::: {.important title="The Laplacian in polar coordinates"}
$$\nabla^2u=u_{rr}+\frac1{r^2}u_{\theta\theta}+\frac1ru_r$$
:::

## The Two-Dimensional Wave Equation with a Circular Boundary

```{.figure #m06-disc caption="A circular membrane of radius $R$"}
```

$$\frac{\partial^2u}{\partial t^2}=c^2\nabla^2u,\qquad u(R,t)=0\ \ \text{(boundary condition)},\qquad u(r,0)=f(r),\ \ u_t(r,0)=g(r)\ \ \text{(initial conditions)}$$

### Solving the Equation

Because of the circular symmetry of this problem it is better to solve it in polar coordinates. On a circular membrane the vibration is not a function of $\theta$, so
$$\begin{cases}\dfrac{\partial^2u}{\partial t^2}=c^2\left(u_{rr}+\dfrac1ru_r\right)\\[2mm] u(R,t)=0,\quad u(r,0)=f(r),\quad u_t(r,0)=g(r)\end{cases}$$
Now, assuming separable variables $u(r,t)=P(r)\times T(t)$:
$$PT''=c^2\left(P''T+\frac1rP'T\right)\ \Rightarrow\ \frac{T''}{c^2T}=\frac{P''}P+\frac1r\frac{P'}P=-\lambda^2\ \Rightarrow\ \begin{cases}P''+\dfrac1rP'+\lambda^2P=0\\[1mm] T''+c^2\lambda^2T=0\end{cases}$$

### Bessel's Differential Equation of Order $n$

$$y''+\frac1xy'+\left(1-\frac{n^2}{x^2}\right)y=0\quad\Longrightarrow\quad y(x)=AJ_n(x)+BY_n(x)$$
where $J_n$ are the Bessel functions of the first kind of order $n$ and $Y_n$ the Bessel functions of the second kind of order $n$.

```{.figure #m06-bessel caption="The Bessel functions of the first kind $J_0,\\dots,J_4$ and of the second kind $Y_0,\\dots,Y_4$ for $0<x\\le10$"}
```

With the substitution $s=\lambda r$:
$$P'=\frac{dP}{dr}=\frac{dP}{ds}\frac{ds}{dr}=\lambda\frac{dP}{ds},\qquad P''=\lambda^2\frac{d^2P}{ds^2},\qquad\frac1r\lambda=\frac{\lambda^2}s$$
$$\lambda^2\frac{d^2P}{ds^2}+\frac1r\lambda\frac{dP}{ds}+\lambda^2P=0\ \Rightarrow\ \frac{d^2P}{ds^2}+\frac1s\frac{dP}{ds}+P=0$$
This is Bessel's equation of order zero ($n=0$), so
$$P(r)=AJ_0(\lambda r)+BY_0(\lambda r)$$
**Applying the boundary conditions:**

- Since $P(0)\neq\infty$ and $Y_0$ is unbounded at the origin, the coefficient of $Y_0$ is zero ($D=0$) and $P(r)=CJ_0(\lambda r)$.
- $P(R)=0$ gives $J_0(\lambda R)=0$, i.e. $\lambda R=\alpha_m$, where $\alpha_m$ are the roots of $J_0$:
$$\lambda=\lambda_m=\frac{\alpha_m}R,\quad m=1,2,\dots\quad\Longrightarrow\quad P_m(r)=C_mJ_0\!\left(\frac{\alpha_m}Rr\right)$$

```{.figure #m06-j0-zeros caption="The function $J_0(x)$ and its roots $\\alpha_1,\\alpha_2,\\alpha_3$"}
```

$$T''+c^2\lambda_m^2T=0\ \Rightarrow\ T_m(t)=A_m\cos(c\lambda_mt)+B_m\sin(c\lambda_mt)$$

::: {.important title="Solution of the two-dimensional wave equation on a disc"}
$$u(r,t)=\sum_{m=1}^{\infty}\big(A_m\cos(c\lambda_mt)+B_m\sin(c\lambda_mt)\big)J_0\!\left(\frac{\alpha_m}Rr\right),\qquad\lambda_m=\frac{\alpha_m}R$$
:::

::: {.remark title="Research task (up to 1 bonus point)"}
Prepare a complete report on Bessel's differential equation of order $n$, the Bessel functions of the first and second kind and their properties, as well as the complete solution of the two-dimensional wave equation with a circular boundary (the report must be typed, in Word format).
:::
