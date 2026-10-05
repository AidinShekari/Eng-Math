# Complex Functions, the Derivative and the Cauchy–Riemann Conditions

## Complex Functions

```{.figure #m02-mapping caption="A complex function $w=f(z)$ maps points of the domain in the $z$-plane to points of the range in the $w$-plane"}
```

$$z=x+iy,\qquad w=u+iv$$
$$f:\mathbb{C}\to\mathbb{C},\qquad f:\begin{cases}u=u(x,y)\\ v=v(x,y)\end{cases}$$

::: {.example}
Consider the function $w=z^2$:
$$u+iv=(x+iy)^2=(x^2-y^2)+i(2xy)\quad\Longrightarrow\quad\begin{cases}u=x^2-y^2\\ v=2xy\end{cases}$$
:::

## Some Important Loci

```{.figure #m02-loci caption="Important loci: a circle, the $\\rho$-neighbourhood of a point $a$, and an annular region"}
```

$$|z|=1,\qquad |z-a|=\rho,\qquad |z-a|<\rho,\qquad \rho_1<|z-a|<\rho_2$$

The set $|z-a|<\rho$ is called the $\rho$-neighbourhood of $a$.

## Limits of Complex Functions

::: {.definition title="Limit"}
If for every $\varepsilon>0$ one can find $\delta>0$ such that $|z-z_0|<\delta$ implies $|f(z)-l|<\varepsilon$, then
$$\lim_{z\to z_0}f(z)=l$$
Hence for all points inside the circle of centre $z_0$ and radius $\delta$, $f(z)$ must lie inside the circle of centre $l$ and radius $\varepsilon$. Here $\varepsilon$ is given and $\delta(\varepsilon)$ has to be found. Clearly the concept of limit here is broader than that for real functions.
:::

```{.figure #m02-limit caption="The definition of the limit: the $\\delta$-neighbourhood of $z_0$ in the $z$-plane and the $\\varepsilon$-neighbourhood of $l$ in the $w$-plane"}
```

## Continuity of Complex Functions

::: {.definition title="Continuity at a point"}
The function $w=f(z)$ is continuous at the point $z=z_0$ if the following three conditions hold:

1. $f(z)$ is defined at $z=z_0$.
2. $\displaystyle\lim_{z\to z_0}f(z)$ exists.
3. $\displaystyle\lim_{z\to z_0}f(z)=f(z_0)$.
:::

::: {.example}
Is the function $f(z)=\sin(1/z)$ continuous at $z=0$?
:::

::: {.example}
Is the function
$$f(z)=\begin{cases}\sin(1/z)&z\neq0\\ 5+4i&z=0\end{cases}$$
continuous at $z=0$?
:::

::: {.example}
Is the function
$$f(z)=\begin{cases}3z^3+4&z\neq0\\ 17&z=0\end{cases}$$
continuous at $z=0$?
:::

### Properties of Continuous Complex Functions

::: {.theorem title="Theorems"}
1. If $f(z),g(z)$ are continuous at $z_0$, then $f(z)\pm g(z)$ is continuous at $z_0$.
2. If $f(z),g(z)$ are continuous at $z_0$, then $f(z)\times g(z)$ is continuous at $z_0$.
3. If $f(z),g(z)$ are continuous at $z_0$ and $g(z_0)\neq0$, then $\dfrac{f(z)}{g(z)}$ is continuous at $z_0$.
:::

::: {.definition title="Continuity on a domain"}
The function $w=f(z)$ is continuous on the domain $D$ if $f$ is continuous at every point of $D$.

Domain: all the points inside a closed curve.
:::

```{.figure #m02-domain caption="A domain $D$ in the complex plane"}
```

## The Derivative of Complex Functions

::: {.definition title="Derivative"}
The function $w=f(z)$ is differentiable at the point $z=z_0$ if the following limit exists:
$$f'(z_0)=\lim_{|\Delta z|\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}$$
:::

::: {.remark}
The existence of the derivative of a complex function requires stricter conditions than for real functions: since $z_0$ can be approached from *all* directions in the $z$-plane, this limit must exist and must not depend on the chosen path towards $z_0$.
:::

```{.figure #m02-approach caption="Approaching the point $z_0$ from all directions"}
```

## The Cauchy–Riemann Conditions

::: {.theorem title="Necessary condition for differentiability"}
A necessary condition for the complex function $w=f(z)$ to be differentiable is that the Cauchy–Riemann conditions hold:
$$\begin{cases}\dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}\\[2mm] \dfrac{\partial u}{\partial y}=-\dfrac{\partial v}{\partial x}\end{cases}\qquad w=u+iv=f(x+iy)=f(z)$$
:::

::: {.proof}
$$f'(z)=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z},\qquad z=x+iy,\qquad \Delta z=\Delta x+i\Delta y$$
$$\begin{aligned}
f(z+\Delta z)-f(z)&=\big[u(x+\Delta x,y+\Delta y)+iv(x+\Delta x,y+\Delta y)\big]-\big[u(x,y)+iv(x,y)\big]\\
&=\big[u(x+\Delta x,y+\Delta y)-u(x,y)\big]+i\big[v(x+\Delta x,y+\Delta y)-v(x,y)\big]
\end{aligned}$$
$$\frac{f(z+\Delta z)-f(z)}{\Delta z}=\frac{u(x+\Delta x,y+\Delta y)-u(x,y)}{\Delta x+i\Delta y}+i\,\frac{v(x+\Delta x,y+\Delta y)-v(x,y)}{\Delta x+i\Delta y}$$
A necessary condition for the existence of the derivative of $w=f(z)$ is that the value of the limit defining $f'(z)$ does not change if we approach $z$ from any direction (in particular along the horizontal or the vertical direction).

**Path 1: the vertical direction.** $\Delta z=\Delta x+i\Delta y$ with $\Delta x=0$, i.e. $\Delta z=i\Delta y$:
$$\begin{aligned}
f'(z)&=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}\\
&=\lim_{\Delta y\to0}\left[\frac{u(x,y+\Delta y)-u(x,y)}{i\Delta y}+i\,\frac{v(x,y+\Delta y)-v(x,y)}{i\Delta y}\right]\\
&=\frac1i\,\frac{\partial u}{\partial y}+\frac{\partial v}{\partial y}=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}
\end{aligned}$$

**Path 2: the horizontal direction.** $\Delta z=\Delta x+i\Delta y$ with $\Delta y=0$, i.e. $\Delta z=\Delta x$:
$$\begin{aligned}
f'(z)&=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}\\
&=\lim_{\Delta x\to0}\left[\frac{u(x+\Delta x,y)-u(x,y)}{\Delta x}+i\,\frac{v(x+\Delta x,y)-v(x,y)}{\Delta x}\right]\\
&=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}
\end{aligned}$$

Therefore
$$f'(z)=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}$$
and equating real and imaginary parts:
:::

```{.figure #m02-cr-paths caption="Two paths towards $z$: the vertical direction ($\\Delta z=i\\Delta y$) and the horizontal direction ($\\Delta z=\\Delta x$)"}
```

::: {.important title="The Cauchy–Riemann conditions"}
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$
:::

::: {.remark title="Consequence"}
1. If these conditions do not hold, the derivative does not exist at the point $z$.
2. The following ways of computing the derivative are suggested:
$$f'(z)=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\frac{\partial u}{\partial x}-i\,\frac{\partial u}{\partial y}=\frac{\partial v}{\partial y}+i\,\frac{\partial v}{\partial x}$$
:::

::: {.theorem title="Sufficient condition for differentiability"}
A sufficient condition for the complex function $w=f(z)$ to be differentiable is that the Cauchy–Riemann conditions hold.

The proof is beyond the scope of this class.
:::

::: {.theorem title="The Cauchy–Riemann theorem"}
A necessary and sufficient condition for the complex function $w=f(z)$ to be differentiable is that the Cauchy–Riemann conditions hold.
$$\begin{cases}\dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}\\[2mm] \dfrac{\partial u}{\partial y}=-\dfrac{\partial v}{\partial x}\end{cases}\qquad w=u+iv=f(x+iy)=f(z)$$
:::

### A Consequence of the Cauchy–Riemann Conditions (Analyticity of a Function)

Differentiating the Cauchy–Riemann conditions with respect to $x$ and $y$:

$$\left.\begin{aligned}\frac{\partial^2u}{\partial x^2}&=\frac{\partial^2v}{\partial x\partial y}\\[1mm] \frac{\partial^2u}{\partial y^2}&=-\frac{\partial^2v}{\partial x\partial y}\end{aligned}\right\}\ \xrightarrow{\ \text{add}\ }\ \frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0$$

$$\left.\begin{aligned}\frac{\partial^2u}{\partial x\partial y}&=\frac{\partial^2v}{\partial y^2}\\[1mm] \frac{\partial^2u}{\partial x\partial y}&=-\frac{\partial^2v}{\partial x^2}\end{aligned}\right\}\ \xrightarrow{\ \text{subtract}\ }\ \frac{\partial^2v}{\partial x^2}+\frac{\partial^2v}{\partial y^2}=0$$

::: {.remark title="Consequence"}
The real and imaginary parts of an analytic function satisfy the two-dimensional Laplace equation.
:::

## Differentiability of Complex Functions: Examples

::: {.example}
Consider the function $w=z^2$; is it analytic?

::: {.solution}
$$w=f(z)=z^2=(x+iy)^2=(x^2-y^2)+i\,2xy,\qquad u(x,y)=x^2-y^2,\qquad v(x,y)=2xy$$
$$\frac{\partial u}{\partial x}=2x=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=-2y=-\frac{\partial v}{\partial x}\ \checkmark$$
$$f'(z)=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=2x+i\,2y=2(x+iy)=2z$$
$$\nabla^2u=2-2=0,\qquad \nabla^2v=0+0=0$$
:::
:::

::: {.example}
Consider the function $w=|z|^2$; is it analytic?

::: {.solution}
$$w=f(z)=|z|^2=(x+iy)(x-iy)=x^2+y^2,\qquad u(x,y)=x^2+y^2,\qquad v(x,y)=0$$
$$\frac{\partial u}{\partial x}=2x,\quad \frac{\partial v}{\partial y}=0,\qquad \frac{\partial u}{\partial y}=2y,\quad -\frac{\partial v}{\partial x}=0$$
$$\nabla^2u=2+2=4,\qquad \nabla^2v=0+0=0$$
Analytic nowhere except at the origin.
:::
:::

::: {.exercise}
Determine whether each of the following functions is analytic. When it is, find its derivative.

1. $f(z)=\bar z$
2. $f(z)=\operatorname{Re}\{z\}$
3. $f(z)=z^3+2z^2+3i$
:::

## Analytic Complex Functions

::: {.example}
$u=x^2-y^2$ is the real part of an analytic function $f(z)$. Find $f(z)$.

::: {.solution}
Since $f(z)$ is analytic, its real and imaginary parts satisfy the Cauchy–Riemann conditions, and consequently they must also satisfy the two-dimensional Laplace equation.

1) First check whether the real part satisfies the two-dimensional Laplace equation:
$$\nabla^2u=\frac{\partial^2}{\partial x^2}(x^2-y^2)+\frac{\partial^2}{\partial y^2}(x^2-y^2)=2-2=0\ \checkmark$$

2) We use the Cauchy–Riemann relations:
$$\frac{\partial u}{\partial x}=2x=\frac{\partial v}{\partial y}\quad\Longrightarrow\quad v(x,y)=2xy+\varphi(x)$$
$$-\frac{\partial v}{\partial x}=-2y-\varphi'(x)=\frac{\partial u}{\partial y}=-2y\quad\Longrightarrow\quad\varphi'(x)=0\quad\Longrightarrow\quad\varphi(x)=c,\ \ c\in\mathbb{R}$$
$$f(z)=(x^2-y^2)+i(2xy+c)=z^2+C$$
:::
:::

::: {.example}
Let $u=\cos x\cosh y$.
(a) Show that this function is harmonic in the plane ($\nabla^2u=0$).
(b) Find $v(x,y)$ such that $u+iv$ is analytic.

::: {.solution}
(a) Check whether the real part satisfies the two-dimensional Laplace equation:
$$\nabla^2u=\frac{\partial^2}{\partial x^2}(\cos x\cosh y)+\frac{\partial^2}{\partial y^2}(\cos x\cosh y)=-\cos x\cosh y+\cos x\cosh y=0\ \checkmark$$

(b) We use the Cauchy–Riemann relations:
$$\frac{\partial u}{\partial x}=-\sin x\cosh y=\frac{\partial v}{\partial y}\quad\Longrightarrow\quad v(x,y)=-\sin x\sinh y+\varphi(x)$$
$$-\frac{\partial v}{\partial x}=\cos x\sinh y-\varphi'(x)=\frac{\partial u}{\partial y}=\cos x\sinh y\quad\Longrightarrow\quad\varphi'(x)=0$$
$$\varphi(x)=c,\ \ c\in\mathbb{R}\quad\Longrightarrow\quad v(x,y)=-\sin x\sinh y+c$$
:::
:::

## The Cauchy–Riemann Conditions in Polar Coordinates

$$\begin{cases}x=r\cos\theta\\ y=r\sin\theta\end{cases}\qquad\begin{cases}r=\sqrt{x^2+y^2}\\ \theta=\tan^{-1}\dfrac{y}{x}\end{cases}\qquad r_x=\frac{x}{r},\quad\theta_x=\frac{-y}{r^2},\quad r_y=\frac{y}{r},\quad\theta_y=\frac{x}{r^2}$$

$$\frac{\partial u}{\partial x}=\frac{\partial u}{\partial r}\frac{\partial r}{\partial x}+\frac{\partial u}{\partial\theta}\frac{\partial\theta}{\partial x}=\frac xr\frac{\partial u}{\partial r}-\frac{y}{r^2}\frac{\partial u}{\partial\theta}=\cos\theta\frac{\partial u}{\partial r}-\frac1r\sin\theta\frac{\partial u}{\partial\theta}$$

$$\frac{\partial v}{\partial y}=\frac{\partial v}{\partial r}\frac{\partial r}{\partial y}+\frac{\partial v}{\partial\theta}\frac{\partial\theta}{\partial y}=\frac yr\frac{\partial v}{\partial r}+\frac{x}{r^2}\frac{\partial v}{\partial\theta}=\sin\theta\frac{\partial v}{\partial r}+\frac1r\cos\theta\frac{\partial v}{\partial\theta}$$

$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}\;\Longrightarrow\;\cos\theta\frac{\partial u}{\partial r}-\frac1r\sin\theta\frac{\partial u}{\partial\theta}=\sin\theta\frac{\partial v}{\partial r}+\frac1r\cos\theta\frac{\partial v}{\partial\theta}$$

Similarly

$$\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}\;\Longrightarrow\;\sin\theta\frac{\partial u}{\partial r}+\frac1r\cos\theta\frac{\partial u}{\partial\theta}=-\cos\theta\frac{\partial v}{\partial r}+\frac1r\sin\theta\frac{\partial v}{\partial\theta}$$

::: {.important title="The Cauchy–Riemann conditions in polar form"}
$$\frac{\partial u}{\partial r}=\frac1r\frac{\partial v}{\partial\theta},\qquad -\frac1r\frac{\partial u}{\partial\theta}=\frac{\partial v}{\partial r}$$
:::

::: {.exercise}
Using the Cauchy–Riemann conditions in polar form, prove that $u$ and $v$ satisfy Laplace's equation in polar form, i.e.
$$\nabla^2u=u_{rr}+\frac1{r^2}u_{\theta\theta}+\frac1ru_r=0,\qquad \nabla^2v=v_{rr}+\frac1{r^2}v_{\theta\theta}+\frac1rv_r=0$$
:::
