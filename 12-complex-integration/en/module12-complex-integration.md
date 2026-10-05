# Integration of Complex Functions

## The Definite Integral and the Path of Integration

The integral of complex functions, like that of real functions, appears in two forms:

- the indefinite integral, which amounts to finding an antiderivative;
- the definite integral, known as the integral along a path.

In the setting of complex functions the definite integral is also called the path integral or *line integral*, and is written
$$\int_C f(z)\,dz$$
$C$ is called the path of integration.

```{.figure #m12-path caption="A path of integration $C$ from the point $A$ to the point $B$ in the $z$-plane"}
```

### The Path of Integration

A path of integration in the complex plane consists of a starting point, an intermediate route and an end point. In many cases the best way to describe a path is to use an auxiliary variable which, as it increases, traverses the path from start to end in the desired direction.

$$z(t)=x(t)+iy(t),\qquad a\le t\le b,\qquad t,a,b\in\mathbb{R}$$
$$z(a)=A,\qquad z(b)=B,\qquad z,A,B\in\mathbb{C}$$

```{.figure #m12-path-param caption="The path $C$, directed from $A=z(a)$ to $B=z(b)$"}
```

::: {.example}
$$z(t)=t+i2t,\qquad 1\le t\le2$$
This path is the line segment from the point $1+2i$ to the point $2+4i$.
:::

```{.figure #m12-line-path caption="The path $z(t)=t+i2t$, $1\\le t\\le2$"}
```

::: {.example}
$$z(t)=\cos t+i\sin t,\qquad 0\le t\le2\pi$$
$$z(t)=e^{it},\qquad 0\le t\le2\pi$$
This path is the unit circle, traversed counterclockwise.
:::

```{.figure #m12-circle-path caption="The path $z(t)=e^{it}$, $0\\le t\\le2\\pi$ (the unit circle)"}
```

### The Derivative of the Path

$$\dot z(t)=\frac{d}{dt}z(t)=\lim_{\Delta t\to0}\frac{z(t+\Delta t)-z(t)}{\Delta t}=\frac{d}{dt}x(t)+i\frac{d}{dt}y(t)=\dot x(t)+i\dot y(t)$$

```{.figure #m12-tangent caption="The derivative of the path $\\dot z(t)$ as the limit of $\\frac{z(t+\\Delta t)-z(t)}{\\Delta t}$"}
```

## The Definite Integral of Complex Functions

$$\int_Cf(z)\,dz=\int_C(u+iv)(dx+i\,dy)=\int_C(u\,dx-v\,dy)+i\int_C(v\,dx+u\,dy)$$
$$\int_Cf(z)\,dz=\int_tf\big(z(t)\big)\,\dot z(t)\,dt$$

::: {.definition title="Steps for computing a complex definite integral along a path"}
1. Describe the path parametrically: $z(t)=x(t)+iy(t)$, $a\le t\le b$.
2. Compute the derivative of $z(t)$ with respect to $t$: $\dot z(t)=\dot x(t)+i\,\dot y(t)$.
3. Substitute $z(t)$ into $f(z)$.
4. Integrate $f\big(z(t)\big)\dot z(t)$ with respect to $t$ for $a\le t\le b$.
:::

::: {.example}
Compute the integral of the function $f(z)=\bar z$ along the path shown.

::: {.solution}
$$z(t)=t+it^2,\quad -1\le t\le1,\qquad \dot z(t)=1+i2t$$
$$f(z)=\bar z=x-iy,\qquad f\big(z(t)\big)=\bar z(t)=t-it^2$$
$$\begin{aligned}
\int_{-1+i}^{1+i}\bar z\,dz&=\int_{t=-1}^{1}(t-it^2)(1+i2t)\,dt\\
&=\int_{t=-1}^{1}\Big[(t+2t^3)+i(2t^2-t^2)\Big]dt=\int_{t=-1}^{1}\Big[(t+2t^3)+it^2\Big]dt\\
&=\left.\left(\frac12t^2+\frac24t^4\right)+i\times\frac13t^3\right|_{-1}^{1}=0+i\,\frac23
\end{aligned}$$
:::
:::

```{.figure #m12-parabola-path caption="The path $z(t)=t+it^2$, $-1\\le t\\le1$, from $-1+i$ to $1+i$"}
```

::: {.example}
Compute the integral of the function $f(z)=\bar z$ along the path shown.

::: {.solution}
$$z(t)=t+i,\quad -1\le t\le1,\qquad \dot z(t)=1$$
$$f(z)=\bar z=x-iy,\qquad f\big(z(t)\big)=\bar z(t)=t-i$$
$$\int_{-1+i}^{1+i}\bar z\,dz=\int_{t=-1}^{1}(t-i)(1)\,dt=\left.\left(\frac{t^2}{2}-it\right)\right|_{-1}^{1}=0-i2$$
So for this complex function the value of the integral depends on the chosen path.
:::
:::

```{.figure #m12-line-path-2 caption="The path $z(t)=t+i$, $-1\\le t\\le1$, from $-1+i$ to $1+i$"}
```

### Some Properties of the Definite Integral

$$\int_C\big[k_1f_1(z)+k_2f_2(z)\big]dz=k_1\int_Cf_1(z)\,dz+k_2\int_Cf_2(z)\,dz\qquad\text{(linearity)}$$
$$\int_{z_0}^{Z}f(z)\,dz=-\int_{Z}^{z_0}f(z)\,dz\qquad\text{(reversing the direction of integration)}$$
$$\int_Cf(z)\,dz=\int_{C_1}f(z)\,dz+\int_{C_2}f(z)\,dz\qquad\text{(splitting the path of integration)}$$

```{.figure #m12-split-path caption="A path $C$ from $z_0$ to $Z$ split into two pieces $C_1$ and $C_2$"}
```

## Simple Closed Curves and Simply Connected Domains

::: {.definition title="Simple closed curve"}
A simple closed curve is a closed curve that does not intersect itself.
:::

```{.figure #m12-curve-types caption="Simple closed curves and closed curves that are not simple"}
```

::: {.definition title="Simply connected domain"}
A domain $D$ is simply connected if, whenever a simple closed curve lies entirely in it, all the points inside the curve belong to this domain.
:::

```{.figure #m12-connected-types caption="Simply connected and not simply connected domains"}
```

## Integration by Antiderivative

::: {.theorem}
Let the complex function $f(z)$ be analytic in the simply connected domain $D$. If $F(z)$ is an antiderivative of $f(z)$, i.e. $F'(z)=f(z)$, then
$$\int_{z_0}^{z_1}f(z)\,dz=F(z_1)-F(z_0)$$
:::

::: {.example}
$$\int_0^{1+i}z^2\,dz=\left.\frac13z^3\right|_0^{1+i}=\frac13(1+i)^3=\frac23(-1+i)$$
:::

::: {.example}
$$\int_{-\pi i}^{\pi i}\cos z\,dz=\sin z\Big|_{-\pi i}^{\pi i}=2\sin(\pi i)=2i\sinh\pi=23.097\,i$$
:::

::: {.example}
$$\int_{8+\pi i}^{8-3\pi i}e^{z/2}\,dz=2e^{z/2}\Big|_{8+\pi i}^{8-3\pi i}=2\left(e^{4-3\pi i/2}-e^{4+\pi i/2}\right)=0$$
:::

::: {.example}
$$\int_{-i}^{i}\frac{dz}{z}=\ln i-\ln(-i)=\frac{i\pi}{2}-\left(-\frac{i\pi}{2}\right)=i\pi$$
:::

## Integrals of Complex Functions Along Closed Paths

The integral along a simple closed path $C$, written
$$\oint_Cf(z)\,dz$$
is of great importance.

::: {.theorem title="Cauchy's integral theorem"}
If the function $f(z)$ is analytic in the simply connected domain $D$, then for every simple closed path $C$ in this domain,
$$\oint_Cf(z)\,dz=0$$
:::

```{.figure #m12-cauchy-region caption="A simple closed path $C$ in the simply connected domain $D$"}
```

::: {.proof}
As we saw earlier, since the complex function is analytic, we have
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$
$$\oint_Cf(z)\,dz=\oint_C(u+iv)(dx+i\,dy)=\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy)$$
By Green's theorem (which you learned in Mathematics II),
$$\oint_C(L\,dx+M\,dy)=\iint_R\left(\frac{\partial M}{\partial x}-\frac{\partial L}{\partial y}\right)dx\,dy$$
Hence
$$\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy)=\iint_R\underbrace{\left(-\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)}_{0}dx\,dy+i\iint_R\underbrace{\left(\frac{\partial u}{\partial x}-\frac{\partial v}{\partial y}\right)}_{0}dx\,dy=0$$
where the first term vanishes because of the second Cauchy–Riemann condition and the second because of the first.
:::

::: {.example}
If the function is analytic in the whole complex plane, the integral along any closed path is zero:
$$\oint_C\cos z\,dz=0,\qquad \oint_Ce^z\,dz=0,\qquad \oint_Cz^n\,dz=0,\quad n=1,2,3,\dots$$
:::

::: {.example}
If the function has non-analytic points that lie neither on the path nor inside $C$, the integral is still zero:
$$\oint_{|z|=1}\sec z\,dz,\qquad \oint_{|z|=1}\frac{dz}{z^2+4}$$
(the path is the unit circle.)
:::

::: {.example}
If the function is not analytic, the integral along a closed path **may** be nonzero:
$$\oint_{|z|=1}\bar z\,dz,\qquad z(t)=\cos t+i\sin t=e^{it},\quad\dot z(t)=ie^{it}$$
$$\oint_{|z|=1}\bar z\,dz=\int_0^{2\pi}e^{-it}\,ie^{it}\,dt=2\pi i$$
:::

::: {.example}
If the function is not analytic on the path or inside it, the integral along a closed path **may** be zero:
$$\oint_C\frac1{z^2}\,dz=0$$
:::

::: {.exercise}
Prove that $\displaystyle\oint_C\frac1{z^2}\,dz=0$.
:::

::: {.remark title="Consequence 1"}
The connectedness of the domain is essential in Cauchy's integral theorem.
:::

::: {.remark title="Consequence 2"}
If $f(z)$ is analytic in the simply connected domain $D$, the definite integral does not depend on the choice of path.
:::

$$\int_{C_1}f(z)\,dz+\int_{C_2^*}f(z)\,dz=0\;\Longrightarrow\;\int_{C_1}f(z)\,dz=-\int_{C_2^*}f(z)\,dz\;\Longrightarrow\;\int_{C_1}f(z)\,dz=\int_{C_2}f(z)\,dz$$

Hence the integral from the starting point to the end point does not depend on the chosen path.

```{.figure #m12-path-independence caption="The paths $C_1$, $C_2$ and $C_2^*$ ($C_2$ with reversed direction) between $z_1$ and $z_2$"}
```

### A Very Important Example

$$\oint_C\frac{dz}{z-z_0}=\;?\qquad C:\ z(t)=z_0+re^{it}$$

```{.figure #m12-circle-integral caption="A circle $C$ with centre $z_0$ and radius $r$"}
```

$$z(t)=z_0+re^{it},\qquad \dot z(t)=rie^{it}$$
$$\oint_C\frac{dz}{z-z_0}=\int_0^{2\pi}\frac{rie^{it}}{re^{it}}\,dt=\int_0^{2\pi}i\,dt=2\pi i$$

::: {.important}
$$\oint_C\frac{dz}{z-z_0}=2\pi i$$
:::

## Cauchy's Integral Formula

::: {.theorem title="Cauchy's integral formula"}
If the function $f(z)$ is analytic in the simply connected domain $D$ and $z_0$ is a point inside $C$, then
$$\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz=f(z_0)$$
:::

::: {.proof}
As we saw earlier, since the function $\dfrac{f(z)}{z-z_0}$ is analytic inside the connected domain $\Gamma$, we have
$$\oint_\Gamma\frac{f(z)}{z-z_0}\,dz=0=\int_{ACA'}\frac{f(z)}{z-z_0}\,dz+\int_{A'B'}\frac{f(z)}{z-z_0}\,dz+\int_{B'C'B}\frac{f(z)}{z-z_0}\,dz+\int_{BA}\frac{f(z)}{z-z_0}\,dz$$
$$\lim_{\substack{A\to A'\\ B\to B'}}\int_{BA}\frac{f(z)}{z-z_0}\,dz=-\int_{A'B'}\frac{f(z)}{z-z_0}\,dz$$
Consequently (the two integrals along the connecting segments cancel)
$$\lim_{\substack{A\to A'\\ B\to B'}}\int_{ACA'}\frac{f(z)}{z-z_0}\,dz+\int_{B'C'B}\frac{f(z)}{z-z_0}\,dz=0\;\Longrightarrow\;\oint_C\frac{f(z)}{z-z_0}\,dz=\oint_{C'}\frac{f(z)}{z-z_0}\,dz$$
(here $C'$ is traversed counterclockwise). Continuing:
$$\begin{aligned}
\oint_C\frac{f(z)}{z-z_0}\,dz&=\oint_{C'}\frac{f(z)}{z-z_0}\,dz=\oint_{C'}\frac{f(z)-f(z_0)+f(z_0)}{z-z_0}\,dz\\
&=\oint_{C'}\frac{f(z)-f(z_0)}{z-z_0}\,dz+\oint_{C'}\frac{f(z_0)}{z-z_0}\,dz\\
&=\oint_{C'}g(z)\,dz+f(z_0)\oint_{C'}\frac1{z-z_0}\,dz=0+2\pi i\,f(z_0)=2\pi i\,f(z_0)
\end{aligned}$$
where
$$g(z)\triangleq\begin{cases}\dfrac{f(z)-f(z_0)}{z-z_0}&z\neq z_0\\[2mm] f'(z_0)&z=z_0\end{cases}$$
is analytic inside $C'$. Therefore
$$\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz=f(z_0)$$
:::

```{.figure #m12-cauchy-proof caption="The path $\\Gamma$ in the proof of Cauchy's integral formula: the curve $C$, the small circle $C'$ centred at $z_0$, and the two connecting segments $AA'$ and $BB'$"}
```

## Application: Evaluating Real Integrals

::: {.example}
Evaluate the integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ using Cauchy's integral formula.

::: {.solution}
Consider the function $g(z)=\dfrac{1}{1+z^2}$. Using the path shown in the figure we find the integral along the closed path.
$$\oint_C\frac{dz}{1+z^2}=\oint_C\frac{\left[\dfrac1{z+i}\right]}{z-i}\,dz=2\pi i\,\frac1{i+i}=\pi,\qquad f(z)=\frac1{z+i},\quad z_0=i$$
On the other hand
$$\oint_C\frac{dz}{1+z^2}=\int_{-R}^{R}\frac{dx}{1+x^2}+\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}$$
In the expression above, the first term as $R\to\infty$ is the required value.
$$\oint_C\frac{dz}{1+z^2}=\pi=\int_{-\infty}^{\infty}\frac{dx}{1+x^2}+I,\qquad I=\lim_{R\to\infty}\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}=0$$
Therefore
$$\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi$$
:::
:::

```{.figure #m12-semicircle-1 caption="The semicircular path in the upper half-plane; the poles are at $z=\\pm i$"}
```

::: {.example}
Evaluate the integral $\displaystyle\int_{-\infty}^{\infty}\frac{\cos\omega x}{1+x^2}\,dx$ using Cauchy's integral formula ($\omega>0$).

::: {.solution}
Consider the function $g(z)=\dfrac{e^{i\omega z}}{1+z^2}$. Using the path shown in the figure (the same semicircle as before) we find the integral along the closed path.
$$\oint_C\frac{e^{i\omega z}}{1+z^2}\,dz=\oint_C\frac{\left[\dfrac{e^{i\omega z}}{z+i}\right]}{z-i}\,dz=2\pi i\,\frac{e^{i\omega i}}{i+i}=\pi e^{-\omega},\qquad f(z)=\frac{e^{i\omega z}}{z+i},\quad z_0=i$$
On the other hand
$$\oint_C\frac{e^{i\omega z}\,dz}{1+z^2}=\int_{-R}^{R}\frac{e^{i\omega x}\,dx}{1+x^2}+\int_0^\pi\frac{e^{i\omega Re^{it}}\,iRe^{it}\,dt}{1+R^2e^{i2t}}$$
But:
$$I_1=\lim_{R\to\infty}\int_0^\pi\frac{e^{i\omega Re^{it}}\,iRe^{it}\,dt}{1+R^2e^{i2t}}\to0$$
**Proof:**
$$e^{i\omega Re^{it}}=e^{i\omega R(\cos t+i\sin t)}=e^{i\omega R\cos t}\,e^{-\omega R\sin t}$$
$$\lim_{R\to\infty}\left|e^{i\omega Re^{it}}\right|=\lim_{R\to\infty}\left|e^{i\omega R\cos t}\right|\times\left|e^{-\omega R\sin t}\right|=1\times0=0,\qquad t\in[0,\pi]$$
On the other hand, in the integral $I_1$ the remaining factor of the integrand tends to zero as $R$ tends to infinity. So the limit of $I_1$ as $R\to\infty$ is zero.

Therefore
$$\pi e^{-\omega}=\oint_C\frac{e^{i\omega z}\,dz}{1+z^2}=\int_{-R}^{R}\frac{e^{i\omega x}\,dx}{1+x^2}=\int_{-R}^{R}\frac{(\cos x+i\sin x)\,dx}{1+x^2}=\int_{-R}^{R}\frac{\cos x\,dx}{1+x^2}+i\int_{-R}^{R}\frac{\sin x\,dx}{1+x^2}$$
The second integral is zero. Why?
$$\int_{-\infty}^{\infty}\frac{\cos\omega x}{1+x^2}\,dx=\pi e^{-\omega}$$
:::
:::

::: {.example}
Evaluate the integral $\displaystyle I=\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)(x^2+4)}$ using Cauchy's integral formula.

::: {.solution}
$$\frac{1}{(x^2+1)(x^2+4)}=\frac{A}{x^2+1}+\frac{B}{x^2+4}=\frac{\frac13}{x^2+1}+\frac{-\frac13}{x^2+4}$$
$$\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)(x^2+4)}=\frac13\int_{-\infty}^{\infty}\frac{dx}{x^2+1}-\frac13\int_{-\infty}^{\infty}\frac{dx}{x^2+4}$$

**First integral:** $I_1=\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+1}$ and $g_1(z)=\dfrac1{z^2+1}$:
$$\oint_Cg_1(z)\,dz=\oint_C\frac1{z^2+1}\,dz=\oint_C\frac{\left[\dfrac1{z+i}\right]}{z-i}\,dz=2\pi i\,\frac1{i+i}=\pi$$
$$\oint_C\frac1{z^2+1}\,dz=\pi=\int_{-R}^{R}\frac{dx}{1+x^2}+\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^2+1}\,dz=\int_{-R}^{R}\frac{dx}{1+x^2}+0=\pi\;\Longrightarrow\;I_1=\pi$$

**Second integral:** $I_2=\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+4}$ and $g_2(z)=\dfrac1{z^2+4}$:
$$\oint_Cg_2(z)\,dz=\oint_C\frac1{z^2+4}\,dz=\oint_C\frac{\left[\dfrac1{z+2i}\right]}{z-2i}\,dz=2\pi i\,\frac1{2i+2i}=\frac\pi2$$
$$\oint_C\frac1{z^2+4}\,dz=\frac\pi2=\int_{-R}^{R}\frac{dx}{x^2+4}+\int_0^\pi\frac{iRe^{it}\,dt}{R^2e^{i2t}+4}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^2+4}\,dz=\int_{-R}^{R}\frac{dx}{x^2+4}+0=\frac\pi2\;\Longrightarrow\;I_2=\frac\pi2$$

As a result
$$I=\frac13I_1-\frac13I_2=\frac13\pi-\frac13\times\frac\pi2=\frac\pi6$$
:::
:::

```{.figure #m12-semicircle-2 caption="The semicircular path; the poles are at $z=\\pm i$ and $z=\\pm2i$"}
```

::: {.example}
Evaluate the integral $\displaystyle I=\int_0^\infty\frac{dx}{x^4+1}$ using Cauchy's integral formula.

::: {.solution}
$$g(z)=\frac1{z^4+1},\qquad z^4+1=0\;\Longrightarrow\;z_1=e^{i\pi/4},\quad z_2=e^{i3\pi/4},\quad z_3=e^{i5\pi/4},\quad z_4=e^{i7\pi/4}$$
Only the two poles $z_1$ and $z_2$ lie inside the path $C$:
$$\begin{aligned}
\oint_Cg(z)\,dz&=\oint_C\frac1{z^4+1}\,dz=\oint_{C_1}\frac1{z^4+1}\,dz+\oint_{C_2}\frac1{z^4+1}\,dz\\
&=\oint_{C_1}\frac{\dfrac1{(z-z_2)(z-z_3)(z-z_4)}}{z-z_1}\,dz+\oint_{C_2}\frac{\dfrac1{(z-z_1)(z-z_3)(z-z_4)}}{z-z_2}\,dz\\
&=2\pi i\left.\frac1{(z-z_2)(z-z_3)(z-z_4)}\right|_{z=z_1}+2\pi i\left.\frac1{(z-z_1)(z-z_3)(z-z_4)}\right|_{z=z_2}\\
&=2\pi i\,\frac1{\underbrace{(e^{i\pi/4}-e^{i3\pi/4})}_{\sqrt2}\underbrace{(e^{i\pi/4}-e^{i5\pi/4})}_{\sqrt2+i\sqrt2}\underbrace{(e^{i\pi/4}-e^{i7\pi/4})}_{i\sqrt2}}\\
&\quad+2\pi i\,\frac1{\underbrace{(e^{i3\pi/4}-e^{i\pi/4})}_{-\sqrt2}\underbrace{(e^{i3\pi/4}-e^{i5\pi/4})}_{i\sqrt2}\underbrace{(e^{i3\pi/4}-e^{i7\pi/4})}_{-\sqrt2+i\sqrt2}}=\frac\pi{\sqrt2}
\end{aligned}$$
On the other hand
$$\oint_C\frac1{z^4+1}\,dz=\frac\pi{\sqrt2}=\int_{-R}^{R}\frac{dx}{x^4+1}+\int_0^\pi\frac{iRe^{it}\,dt}{R^4e^{i4t}+1}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^4+1}\,dz=\int_{-\infty}^{\infty}\frac{dx}{x^4+1}+\underbrace{\lim_{R\to\infty}\int_0^\pi\frac{iRe^{it}\,dt}{R^4e^{i4t}+1}}_{0}=\frac\pi{\sqrt2}$$
$$\int_{-\infty}^{\infty}\frac{dx}{x^4+1}=\frac\pi{\sqrt2}\;\Longrightarrow\;\int_0^\infty\frac{dx}{x^4+1}=\frac\pi{2\sqrt2}$$
:::
:::

```{.figure #m12-semicircle-3 caption="The semicircular path and the circles $C_1$ and $C_2$ around the poles $z_1$ and $z_2$; the poles $z_3$ and $z_4$ lie in the lower half-plane"}
```

## Cauchy's Theorem with Several Non-Analytic Points

::: {.theorem}
If the function $f(z)$ is analytic at all points of the domain $D$ except the points $z_1,z_2,z_3,\dots,z_n$ inside $C$, then
$$\oint_Cf(z)\,dz=\oint_{C_1}f(z)\,dz+\oint_{C_2}f(z)\,dz+\cdots+\oint_{C_n}f(z)\,dz$$
where $C_k$ is a circle centred at $z_k$ that lies inside $C$ and does not contain any of the other points $z_1,\dots,z_n$.
:::

```{.figure #m12-multi-points caption="A path $C$ and the non-analytic points $z_1,\\dots,z_n$ inside it"}
```

::: {.proof}
Build the path $\Gamma$ from $C$ (counterclockwise), the small circles $C_1,\dots,C_n$ (clockwise) and the segments connecting them to $C$; the integral along each connecting segment is traversed twice in opposite directions and cancels. The function is analytic inside $\Gamma$, so
$$\oint_\Gamma f(z)\,dz=0\;\Longrightarrow\;\oint_Cf(z)\,dz+\oint_{C_1^{\circlearrowright}}f(z)\,dz+\cdots+\oint_{C_n^{\circlearrowright}}f(z)\,dz=0$$
$$\oint_Cf(z)\,dz=-\oint_{C_1^{\circlearrowright}}f(z)\,dz-\cdots-\oint_{C_n^{\circlearrowright}}f(z)\,dz=\oint_{C_1}f(z)\,dz+\cdots+\oint_{C_n}f(z)\,dz$$
where $C_k^{\circlearrowright}$ is the circle $C_k$ traversed clockwise and $C_k$ the same circle traversed counterclockwise.
:::

```{.figure #m12-multi-proof caption="The path $\\Gamma$ for the proof: $C$, the circles $C_1,\\dots,C_n$ and the connecting segments"}
```

## Derivatives of an Analytic Function

::: {.theorem title="Cauchy's integral formula for the derivative"}
If the function $f(z)$ is analytic in the simply connected domain $D$ and $z_0$ is a point inside $C$, then
$$\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz=f'(z_0)$$
:::

::: {.proof}
$$f'(z_0)=\lim_{\Delta t\to0}\frac{f(z_0+\Delta t)-f(z_0)}{\Delta t},\qquad f(z_0)=\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz,\qquad f(z_0+\Delta t)=\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0-\Delta t}\,dz$$
$$\begin{aligned}
\frac{f(z_0+\Delta t)-f(z_0)}{\Delta t}&=\frac1{2\pi i\,\Delta t}\left\{\oint_C\frac{f(z)}{z-z_0-\Delta t}\,dz-\oint_C\frac{f(z)}{z-z_0}\,dz\right\}\\
&=\frac1{2\pi i\,\Delta t}\oint_Cf(z)\left[\frac1{z-z_0-\Delta t}-\frac1{z-z_0}\right]dz\\
&=\frac1{2\pi i\,\Delta t}\oint_Cf(z)\left[\frac{\Delta t}{(z-z_0-\Delta t)(z-z_0)}\right]dz\\
&=\frac1{2\pi i}\oint_Cf(z)\left[\frac1{(z-z_0-\Delta t)(z-z_0)}\right]dz
\end{aligned}$$
$$f'(z_0)=\lim_{\Delta t\to0}\frac{f(z_0+\Delta t)-f(z_0)}{\Delta t}=\lim_{\Delta t\to0}\frac1{2\pi i}\oint_Cf(z)\left[\frac1{(z-z_0-\Delta t)(z-z_0)}\right]dz=\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz$$
:::

::: {.theorem title="Generalization of Cauchy's integral formula"}
If the function $f(z)$ is analytic in the simply connected domain $D$ and $z_0$ is a point inside $C$, then
$$\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz=f^{(n)}(z_0)$$
:::

::: {.exercise}
Prove it by mathematical induction.
:::

::: {.example}
Evaluate the following integral. ($C$ is the unit circle.)
$$I=\oint_C\frac{z^2}{(2z-1)^2}\,dz$$

::: {.solution}
$$I=\oint_C\frac{z^2}{4\left(z-\frac12\right)^2}\,dz=\frac14\oint_C\frac{z^2}{\left(z-\frac12\right)^2}\,dz=\frac14\times2\pi i\times\left.\frac{d}{dz}\big(z^2\big)\right|_{z=1/2}=\frac14\times2\pi i\times(2z)\Big|_{z=1/2}=\frac\pi2\,i$$
($z=\frac12$ lies inside the unit circle.)
:::
:::

::: {.example}
Evaluate the following integral. ($C$ is the unit circle.)
$$I=\oint_C\frac{e^{-z}\sin z}{z^2}\,dz$$

::: {.solution}
$$f(z)=e^{-z}\sin z,\quad z_0=0,\qquad f'(z)=-e^{-z}\sin z+e^{-z}\cos z,\qquad f'(z_0)=f'(0)=1$$
$$I=2\pi i\,f'(z_0)=2\pi i$$
:::
:::

::: {.exercise title="Problem"}
If $f(z)$ is analytic in the whole $z$-plane and bounded in the whole plane, i.e. $|f(z)|<M$, prove that $f(z)=k$, $k\in\mathbb{C}$.

::: {.solution}
Choose the path $C$ to be a circle of radius $R$ centred at $z_0$, and let $R$ tend to infinity.
$$f'(z_0)=\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz$$
$$|f'(z_0)|=\left|\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz\right|\le\frac1{2\pi}\oint_C\frac{|f(z)|}{|z-z_0|^2}\,|dz|\le\frac1{2\pi}\,\frac{M}{R^2}\oint_C|dz|=\frac1{2\pi}\,\frac{M}{R^2}\cdot2\pi R=\frac MR\to0\quad(R\to\infty)$$
$$\Longrightarrow\;|f'(z_0)|=0\;\Longrightarrow\;f'(z)=0\;\Longrightarrow\;f(z)=k$$
:::
:::

```{.figure #m12-liouville-circle caption="A circle $C$ with centre $z_0$ and radius $R$"}
```

::: {.exercise}
Evaluate the following integrals:

1. $\displaystyle\oint_C\frac{z^2}{(2z-1)^4}\,dz$, $C$: the unit circle
2. $\displaystyle\int_{1+i}^{1+3i}e^z\sin z\,dz$
3. $\displaystyle\int_{1+i}^{2+2i}\operatorname{Re}\{z^2\}\,dz$ along a straight-line path
4. $\displaystyle\oint_C\frac{e^{\cos z}\sin z}{1+z^6}\,dz$ along the path below
:::

```{.figure #m12-exercise-circle caption="The path of exercise 4: a circle with centre $3+3i$ and radius $r=1$"}
```
