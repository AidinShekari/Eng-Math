# Elementary Complex Functions

The elementary complex functions generalize the elementary real functions.

## The Exponential Function

The real exponential function $f(x)=e^x$ has the following properties:

$$\begin{aligned}
&1)\quad f(x_1+x_2)=f(x_1)f(x_2)\qquad &&e^{x_1}e^{x_2}=e^{x_1+x_2}\\
&2)\quad \frac{d}{dx}f(x)=f(x)\qquad &&\frac{d}{dx}e^x=e^x\\
&3)\quad e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+\cdots
\end{aligned}$$

We define the complex exponential function inspired by the third property, and then verify the other properties for it.

::: {.definition title="The complex exponential function"}
$$w=e^z\triangleq1+z+\frac{z^2}{2!}+\cdots+\frac{z^n}{n!}+\cdots$$
:::

If in the definition of the complex exponential we substitute $z=iy$:

$$\begin{aligned}
e^{iy}&=1+iy+\frac1{2!}(iy)^2+\frac1{3!}(iy)^3+\cdots\\
&=1+iy-\frac1{2!}y^2-\frac{i}{3!}y^3+\frac1{4!}y^4+\frac{i}{5!}y^5+\cdots\\
&=\underbrace{\left(1-\frac1{2!}y^2+\frac1{4!}y^4+\cdots\right)}_{\cos y}+i\underbrace{\left(y-\frac1{3!}y^3+\frac1{5!}y^5+\cdots\right)}_{\sin y}=\cos y+i\sin y
\end{aligned}$$

::: {.important}
$$w=e^z=e^{x+iy}=e^xe^{iy}=e^x(\cos y+i\sin y)$$
:::

::: {.example}
Is the function $w=e^z$ analytic?

::: {.solution}
$$u(x,y)=e^x\cos y,\qquad v(x,y)=e^x\sin y$$
$$\frac{\partial u}{\partial x}=e^x\cos y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=-e^x\sin y=-\frac{\partial v}{\partial x}\ \checkmark$$
Since the Cauchy–Riemann conditions hold in the whole complex plane, the function $w=e^z$ is differentiable in the whole complex plane.
:::
:::

::: {.example}
Find the derivative of $w=e^z$.

::: {.solution}
$$\frac{d}{dz}e^z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^z$$
:::
:::

::: {.important title="Important remark"}
From now on we can write every complex number in exponential form:
$$z=x+iy=|z|(\cos\theta+i\sin\theta)=|z|\,e^{i\theta}$$
:::

Observe that
$$e^{z+i2k\pi}=e^ze^{i2k\pi}=e^z\big[\cos(2k\pi)+i\sin(2k\pi)\big]=e^z$$
so $w=e^z$ is a periodic function in the complex plane with period $i2\pi$.

```{.figure #m03-exp-strip caption="The fundamental strip of the exponential function: $-\\pi<y\\le\\pi$"}
```

## Trigonometric Functions

$$e^{i\theta}=\cos\theta+i\sin\theta\quad\Longrightarrow\quad e^{-i\theta}=\cos\theta-i\sin\theta$$
$$\Longrightarrow\quad\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\qquad \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}$$

::: {.definition title="Complex cosine and sine"}
$$\cos z\triangleq\frac{e^{iz}+e^{-iz}}{2},\qquad \sin z\triangleq\frac{e^{iz}-e^{-iz}}{2i}$$
:::

$$\begin{aligned}
\cos z&=\frac12\Big[e^{i(x+iy)}+e^{-i(x+iy)}\Big]=\frac12\Big[e^{ix}e^{-y}+e^{-ix}e^{y}\Big]\\
&=\frac12\Big[e^{-y}(\cos x+i\sin x)+e^{y}(\cos x-i\sin x)\Big]\\
&=\cos x\left(\frac{e^y+e^{-y}}{2}\right)-i\sin x\left(\frac{e^y-e^{-y}}{2}\right)\\
&=\cos x\cosh y-i\sin x\sinh y
\end{aligned}$$

$$\begin{aligned}
\sin z&=\frac1{2i}\Big[e^{i(x+iy)}-e^{-i(x+iy)}\Big]=\frac1{2i}\Big[e^{ix}e^{-y}-e^{-ix}e^{y}\Big]\\
&=\frac1{2i}\Big[e^{-y}(\cos x+i\sin x)-e^{y}(\cos x-i\sin x)\Big]\\
&=\sin x\left(\frac{e^y+e^{-y}}{2}\right)+i\cos x\left(\frac{e^y-e^{-y}}{2}\right)\\
&=\sin x\cosh y+i\cos x\sinh y
\end{aligned}$$

### Analyticity and Differentiability of $\cos z$

$$\cos z=u(x,y)+iv(x,y)=\cos x\cosh y-i\sin x\sinh y,\qquad u=\cos x\cosh y,\quad v=-\sin x\sinh y$$
$$\frac{\partial u}{\partial x}=-\sin x\cosh y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\cos x\sinh y=-\frac{\partial v}{\partial x}\ \checkmark$$
So this function is analytic in the whole complex plane. We obtain its derivative with one of the methods described earlier:
$$f'(z)=\frac{d}{dz}\cos z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=-\sin x\cosh y-i\cos x\sinh y=-\sin z$$

### Analyticity and Differentiability of $\sin z$

$$\sin z=u(x,y)+iv(x,y)=\sin x\cosh y+i\cos x\sinh y,\qquad u=\sin x\cosh y,\quad v=\cos x\sinh y$$
$$\frac{\partial u}{\partial x}=\cos x\cosh y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\sin x\sinh y=-\frac{\partial v}{\partial x}\ \checkmark$$
So this function is analytic in the whole complex plane and
$$f'(z)=\frac{d}{dz}\sin z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\cos x\cosh y-i\sin x\sinh y=\cos z$$

::: {.important}
$$(\sin z)'=\cos z,\qquad (\cos z)'=-\sin z$$
:::

### Unboundedness of $\sin z$ and $\cos z$

$$|\cos z|=\sqrt{\cos^2x\cosh^2y+\sin^2x\sinh^2y}=\sqrt{\cos^2x+\sinh^2y},\qquad(\cosh^2y=1+\sinh^2y,\ \ \sin^2x=1-\cos^2x)$$
$$|\sin z|=\sqrt{\sin^2x\cosh^2y+\cos^2x\sinh^2y}=\sqrt{\sin^2x+\sinh^2y},\qquad(\cosh^2y=1+\sinh^2y,\ \ \cos^2x=1-\sin^2x)$$

Since $\sinh y$ is an unbounded function, the functions $\cos z$ and $\sin z$ are **unbounded**.

### Periodicity

$$\begin{aligned}
\cos(z+2\pi)&=\cos(x+iy+2\pi)=\cos(x+2\pi)\cosh y-i\sin(x+2\pi)\sinh y\\
&=\cos x\cosh y-i\sin x\sinh y=\cos z
\end{aligned}$$
In the same way $\sin(z+2\pi)=\sin z$.

```{.figure #m03-trig-strip caption="The fundamental strip of $\\sin z$ and $\\cos z$: $-\\pi<x\\le\\pi$"}
```

### Remark

$$\cos(iy)=\cosh y,\qquad \sin(iy)=i\sinh y$$
$$\cos(x+iy)=\cos x\cos(iy)-\sin x\sin(iy)=\cos x\cosh y-i\sin x\sinh y$$
$$\sin(x+iy)=\sin x\cos(iy)+\cos x\sin(iy)=\sin x\cosh y+i\cos x\sinh y$$

The other trigonometric functions:
$$\tan z\triangleq\frac{\sin z}{\cos z},\qquad \cot z\triangleq\frac{\cos z}{\sin z},\qquad \sec z\triangleq\frac1{\cos z},\qquad \csc z\triangleq\frac1{\sin z}$$
$$(\tan z)'=\sec^2z,\quad\dots$$

## Hyperbolic Functions

$$\cosh z\triangleq\frac{e^z+e^{-z}}{2},\qquad \sinh z\triangleq\frac{e^z-e^{-z}}{2},\qquad e^z=e^x(\cos y+i\sin y)$$

::: {.exercise}
Verify that
$$\cosh z=\cosh x\cos y+i\sinh x\sin y,\qquad \sinh z=\sinh x\cos y+i\cosh x\sin y$$
:::

::: {.exercise}
Verify that $\cosh z$ and $\sinh z$ are analytic in the whole complex plane and that their derivatives are given by
$$(\cosh z)'=\sinh z,\qquad (\sinh z)'=\cosh z$$
:::

$$\tanh z=\frac{\sinh z}{\cosh z},\quad \coth z=\frac{\cosh z}{\sinh z},\quad \operatorname{sech}z=\frac1{\cosh z},\quad \operatorname{csch}z=\frac1{\sinh z}$$

$$\cosh(z+i2\pi)=\cosh(z),\qquad \sinh(z+i2\pi)=\sinh(z)$$

```{.figure #m03-hyp-strip caption="The fundamental strip of the hyperbolic functions: $-\\pi<y\\le\\pi$"}
```

## The Logarithm Function

$$w=\ln z,\qquad z=|z|e^{i\arg z}=e^w=e^{\ln|z|}e^{i\arg z}$$
$$w=\ln z=\ln|z|+i\arg z=\ln\!\big(x^2+y^2\big)^{1/2}+i\tan^{-1}\frac yx$$
$$u(x,y)=\frac12\ln\!\big(x^2+y^2\big),\qquad v(x,y)=\tan^{-1}\frac yx$$
$$\frac{\partial u}{\partial x}=\frac{x}{x^2+y^2}=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\frac{y}{x^2+y^2}=-\frac{\partial v}{\partial x}\ \checkmark$$

Hence the logarithm function is analytic in the whole complex plane except at the origin.

$$\frac{d}{dz}\ln z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\frac{x}{x^2+y^2}+i\,\frac{-y}{x^2+y^2}=\frac{\bar z}{z\bar z}=\frac1z$$

$$z=re^{i\theta}=re^{i(\theta+2k\pi)}$$

So that the definition of a function is not violated, the range of this function is the region shown in the figure.

```{.figure #m03-log-range caption="The range of the logarithm function: the strip $-\\pi<\\operatorname{Im}w\\le\\pi$"}
```

The following properties hold for the logarithm function:
$$\ln(z_1\times z_2)=\ln z_1+\ln z_2,\qquad \ln\!\left(\frac{z_1}{z_2}\right)=\ln z_1-\ln z_2,\qquad \ln(z^c)=c\ln z$$
