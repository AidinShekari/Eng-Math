# Evaluating Definite Integrals by Residues

::: {.theorem title="The residue theorem"}
If the function $f(z)$ is analytic everywhere inside the path $C$ except at the points $z_1,z_2,\dots,z_n$, and the residues of the function at these points are $A_1^1,A_1^2,\dots,A_1^n$ respectively, then
$$\oint_Cf(z)\,dz=2\pi i\sum_{k=1}^{n}A_1^k$$
:::

Many different kinds of integrals can be solved by the method of residues. Two classes of them are mentioned here:

::: {.definition title="Integrals of the first class"}
In these integrals the denominator of the integrand is a polynomial, and the numerator is a polynomial, an exponential, or a sine or cosine function (which can also be expressed exponentially).
:::

::: {.definition title="Integrals of the second class"}
In these integrals the integrand is a function of sine or cosine.
:::

## Integrals of the First Class

::: {.example}
Evaluate the integral $\displaystyle\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx$ ($\omega>0$).

::: {.solution}
Consider the function $f(z)=e^{i\omega z}\big/(1+z^2)^2$. It is not analytic at $z=i$ and $z=-i$. The path $C$ is the upper semicircle of radius $R$.
$$\begin{aligned}
\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz&=2\pi i\times\operatorname{Res}\left\{\frac{e^{i\omega z}}{(1+z^2)^2}\right\}\Bigg|_{z=i}\\
&=2\pi i\times\left[\frac d{dz}\left\{(z-i)^2\,\frac{e^{i\omega z}}{(z-i)^2(z+i)^2}\right\}\right]_{z=i}\\
&=2\pi i\times\left[\frac{i\omega e^{i\omega z}(z+i)-2e^{i\omega z}}{(z+i)^3}\right]_{z=i}\\
&=2\pi i\times e^{-\omega}\left(\frac{i\omega(2i)-2}{(2i)^3}\right)\\
&=2\pi i\times e^{-\omega}\,\frac{\omega+1}{4i}=\frac\pi2(\omega+1)e^{-\omega}
\end{aligned}$$
On the other hand
$$\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz=\int_{-R}^{R}\frac{e^{i\omega x}}{(1+x^2)^2}\,dx+\int_0^\pi\frac{e^{i\omega Re^{it}}\,Rie^{it}}{(1+R^2e^{i2t})^2}\,dt$$
and as $R\to\infty$ the integral along the semicircle vanishes, while the imaginary part of the integral along the real axis (the odd function $\sin\omega x/(1+x^2)^2$) is zero:
$$\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz\ \xrightarrow{\ R\to\infty\ }\ 2\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx$$
$$\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx=\frac\pi4(\omega+1)e^{-\omega}$$
:::
:::

```{.figure #m14-semicircle caption="The upper semicircular path; the double pole $z=i$ lies inside the path and $z=-i$ outside it"}
```

## Integrals of the Second Class

$$\int_0^{2\pi}f(a\cos t,\,b\sin t)\,dt$$
To solve such integrals we put $z=e^{it}$. Then
$$dz=ie^{it}\,dt\;\Longrightarrow\;dt=\frac{dz}{ie^{it}}=\frac{dz}{iz}$$
$$\sin t=\frac{e^{it}-e^{-it}}{2i}=\frac{z-z^{-1}}{2i},\qquad \cos t=\frac{e^{it}+e^{-it}}2=\frac{z+z^{-1}}2$$

::: {.important}
$$\int_0^{2\pi}f(a\cos t,\,b\sin t)\,dt=\oint_Cf\!\left(a\,\frac{z+z^{-1}}{2},\;b\,\frac{z-z^{-1}}{2i}\right)\frac{dz}{iz}$$
:::

Here $C$ is the unit circle, and the integral is easily solved with the method of residues.

```{.figure #m14-unit-circle caption="The unit circle $z=e^{it}$, $0\\le t\\le2\\pi$"}
```

::: {.example}
Evaluate the integral $\displaystyle\int_0^{2\pi}\frac1{2+\cos x}\,dx$.

::: {.solution}
$$z=e^{ix},\qquad dz=ie^{ix}dx,\qquad dx=\frac{dz}{iz},\qquad \cos x=\frac{z+z^{-1}}2=\frac{z^2+1}{2z}$$
$$2+\cos x=2+\frac{z^2+1}{2z}=\frac{z^2+4z+1}{2z}$$
$$\int_0^{2\pi}\frac1{2+\cos x}\,dx=\oint_C\frac{2z}{z^2+4z+1}\,\frac{dz}{iz}=\frac2i\oint_C\frac1{z^2+4z+1}\,dz=\frac2i\times2\pi i\times\sum_k\operatorname{Res}\left\{\frac1{z^2+4z+1}\right\}\Bigg|_{z=z_k}$$
$$z^2+4z+1=0\;\Longrightarrow\;z_1=-2+\sqrt3\approx-0.27,\qquad z_2=-2-\sqrt3\approx-3.73$$
Only $z_1$ lies inside the unit circle.
$$\int_0^{2\pi}\frac1{2+\cos x}\,dx=4\pi\times\operatorname{Res}\left\{\frac1{z^2+4z+1}\right\}\Bigg|_{z=z_1}=4\pi\left[\big(z+2-\sqrt3\big)\frac1{\big(z+2-\sqrt3\big)\big(z+2+\sqrt3\big)}\right]_{z_1=-2+\sqrt3}=\frac{2\pi}{\sqrt3}$$
:::
:::

```{.figure #m14-poles-cos caption="The unit circle and the poles $z_1\\approx-0.27$ (inside) and $z_2\\approx-3.73$ (outside)"}
```

::: {.exercise title="Applying the residue theorem to integrals"}
Using the residue theorem, evaluate the following definite integrals:
$$I_1=\int_0^{2\pi}\frac{dt}{1-2p\cos t+p^2},\qquad I_2=\int_{-\infty}^{\infty}\frac{\sin2x}{x^2+x+1}\,dx$$
$$I_3=\int_{-\infty}^{\infty}\frac{x}{(x^2-2x+2)^2}\,dx,\qquad I_4=\int_{-\infty}^{\infty}\frac{\cos^4x}{(x^2+1)(x^2+4)}\,dx$$
:::
