# Laurent Series, Singularities and Residues

## The Laurent Series

::: {.theorem title="Laurent series"}
If the function $f(z)$ is analytic in the domain $D$, its Laurent series about the point $z_0$ is written
$$f(z)=\sum_{n=-\infty}^{\infty}a_n\,(z-z_0)^n,\qquad a_n=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{n+1}}\,dv$$
where $C$ is a circle centred at $z_0$ and the function is analytic at all points inside and on this circle, except possibly at $z_0$.

The radius of convergence is the distance from $z_0$ to the nearest non-analytic point of $f(z)$.
:::

For non-negative $n$ we have
$$a_n=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{n+1}}\,dv=\frac{f^{(n)}(z_0)}{n!},\qquad n=0,1,2,\dots$$
Therefore
$$\begin{aligned}
f(z)&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=-\infty}^{-1}a_n(z-z_0)^n\\
&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=1}^{\infty}a_{-n}(z-z_0)^{-n}\\
&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n},\qquad A_n=a_{-n}
\end{aligned}$$
$$A_n=a_{-n}=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{-n+1}}\,dv=\frac1{2\pi i}\oint_C(v-z_0)^{n-1}f(v)\,dv,\qquad n=1,2,\dots$$

::: {.important title="The Laurent series: Taylor part and principal part"}
$$f(z)=\underbrace{\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n}_{\text{Taylor series part}}+\underbrace{\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n}}_{\text{principal part}},\qquad A_n=\frac1{2\pi i}\oint_C(v-z_0)^{n-1}f(v)\,dv$$
:::

If $z_0$ is an irregular (singular) point, in other words if the function is not analytic there, the Taylor part alone is not sufficient to describe the function.

### The Different Cases for the Point $z_0$

1. If all the $A_n$ are zero, the point $z_0$ is called a **regular** point. In this case the Laurent series is just the Taylor series.
2. If $A_p\neq0$ but $(A_n=0\ \ \forall n>p)$, then $z_0$ is called a **pole of order $p$**.
3. If $z_0$ is not a regular point and is also not a pole (in other words, no $p$ can be found such that $A_p\neq0$ and $(A_n=0\ \ \forall n>p)$), then $z_0$ is called an **essential singularity**.

## The Residue

::: {.definition title="Residue"}
The residue of $f(z)$ at the point $z_0$ is $A_1$.
$$\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=A_1=\frac1{2\pi i}\oint_Cf(v)\,dv$$
:::

::: {.theorem}
If the function $f(z)$ has a pole of order $p$ at $z_0$, then
$$A_k=\frac1{(p-k)!}\left.\frac{d^{\,p-k}}{dz^{\,p-k}}\Big[(z-z_0)^p\,f(z)\Big]\right|_{z=z_0},\qquad k=1,2,\dots,p$$
:::

::: {.proof}
$$f(z)=\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$
If $f(z)$ has a pole of order $p$ at $z_0$ we have
$$f(z)=\frac{A_p}{(z-z_0)^p}+\frac{A_{p-1}}{(z-z_0)^{p-1}}+\cdots+\frac{A_2}{(z-z_0)^2}+\frac{A_1}{z-z_0}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$
Multiplying both sides by $(z-z_0)^p$ gives
$$(z-z_0)^pf(z)=A_p+A_{p-1}(z-z_0)+\cdots+A_2(z-z_0)^{p-2}+A_1(z-z_0)^{p-1}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p}$$
Now if we set $z=z_0$ we get
$$(z-z_0)^pf(z)\Big|_{z=z_0}=A_p$$
If we differentiate $(z-z_0)^pf(z)$ once and then set $z=z_0$:
$$\begin{aligned}
\frac{d}{dz}\Big[(z-z_0)^pf(z)\Big]\Big|_{z=z_0}&=\Bigg\{A_{p-1}+\cdots+A_2(p-2)(z-z_0)^{p-3}+A_1(p-1)(z-z_0)^{p-2}\\
&\qquad+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p-1}(n+p)\Bigg\}\Bigg|_{z=z_0}=A_{p-1}
\end{aligned}$$
If we differentiate $(z-z_0)^pf(z)$ twice and then set $z=z_0$:
$$\begin{aligned}
\frac{d^2}{dz^2}\Big[(z-z_0)^pf(z)\Big]\Big|_{z=z_0}&=\Bigg\{2A_{p-2}+\cdots+A_2(p-2)(p-3)(z-z_0)^{p-4}+A_1(p-1)(p-2)(z-z_0)^{p-3}\\
&\qquad+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p-2}(n+p)(n+p-1)\Bigg\}\Bigg|_{z=z_0}=2A_{p-2}
\end{aligned}$$
$$\Longrightarrow\quad A_{p-2}=\frac1{2!}\left.\frac{d^2}{dz^2}\Big[(z-z_0)^pf(z)\Big]\right|_{z=z_0}$$
:::

::: {.exercise}
Continue the differentiation in the same way and complete the proof of the theorem.
:::

::: {.remark title="Consequence"}
In particular, when $f(z)$ has a pole of order $p$ at $z_0$, the residue is given by
$$\operatorname{Res}\{f(z)\}=A_1=\frac1{(p-1)!}\left.\frac{d^{\,p-1}}{dz^{\,p-1}}\Big[(z-z_0)^p\,f(z)\Big]\right|_{z=z_0}$$
:::

## The Residue Theorem

::: {.theorem title="The residue theorem"}
If the function $f(z)$ is analytic everywhere inside the path $C$ except at the points $z_1,z_2,\dots,z_n$, and the residues of the function at these points are $A_1^1,A_1^2,\dots,A_1^n$ respectively, then
$$\oint_Cf(z)\,dz=2\pi i\sum_{k=1}^{n}A_1^k$$
:::

```{.figure #m06-residue-theorem caption="A path $C$ and the singular points $z_1,\\dots,z_n$ inside it; a small circle is drawn around each point"}
```

The proof is left to the reader as an exercise.

## Examples of Taylor and Laurent Expansions

::: {.example}
Find the Laurent series of $f(z)=\dfrac1{z^4+1}$ in a neighbourhood of $z_0=0$.

::: {.solution}
We see that $f(z)$ is analytic at $z_0=0$, so this is a regular point and the Laurent series is the Taylor (Maclaurin) series. Hence
$$f(z)=f(0)+\frac1{1!}f^{(1)}(0)z+\frac1{2!}f^{(2)}(0)z^2+\frac1{3!}f^{(3)}(0)z^3+\cdots$$
Geometric series:
$$1+q+q^2+q^3+q^4+\cdots=\frac1{1-q},\qquad |q|<1$$
$$\frac1{1+z^4}=1-z^4+z^8-z^{12}+-\cdots,\qquad |z^4|<1\ \Longrightarrow\ |z|<1$$
(Taylor/Maclaurin series; region of convergence of radius 1.)
$$z^4+1=0\;\Longrightarrow\;z_1=e^{i\pi/4},\quad z_2=e^{i3\pi/4},\quad z_3=e^{i5\pi/4},\quad z_4=e^{i7\pi/4}$$
We see that the distance from $z_0=0$ to the nearest non-analytic point of the function (the radius of convergence) is $1$.
:::
:::

```{.figure #m06-radius-1 caption="The four poles of $z^4+1=0$ on the unit circle; the radius of convergence of the series about the origin is $1$"}
```

::: {.example}
Find the Laurent series of $f(z)=\dfrac{4z^2+30z+68}{(z+4)^2(z-2)}$ in a neighbourhood of $z_0=0$.

::: {.solution}
We see that $f(z)$ is analytic at $z_0=0$, so this is a regular point and the Laurent series is the Taylor (Maclaurin) series. Hence
$$f(z)=f(0)+\frac1{1!}f^{(1)}(0)z+\frac1{2!}f^{(2)}(0)z^2+\frac1{3!}f^{(3)}(0)z^3+\cdots$$
$$\frac1{z-2}=\frac{-1}{2-z}=\frac{-1}2\,\frac1{1-z/2}=\frac{-1}2\left(1+\frac z2+\frac{z^2}4+\frac{z^3}8+\cdots\right),\qquad \left|\frac z2\right|<1\ \Longrightarrow\ |z|<2$$
$$\frac1{4+z}=\frac14\,\frac1{1+z/4}=\frac14\left(1-\frac z4+\frac{z^2}{16}-\frac{z^3}{64}+\cdots\right),\qquad \left|-\frac z4\right|<1\ \Longrightarrow\ |z|<4$$
$$\frac d{dz}\left(\frac1{4+z}\right)=\frac{-1}{(4+z)^2}=\frac14\left(-\frac14+\frac{2z}{16}-\frac{3z^2}{64}+\cdots\right)\;\Longrightarrow\;\frac1{(4+z)^2}=\frac14\left(\frac14-\frac{2z}{16}+\frac{3z^2}{64}-\cdots\right)$$
$$f(z)=(4z^2+30z+68)\times\frac1{(z+4)^2}\times\frac1{z-2}$$
$$f(z)=(4z^2+30z+68)\times\left(\frac{-1}2\right)\left(1+\frac z2+\frac{z^2}4+\frac{z^3}8+\cdots\right)\times\frac14\left(\frac14-\frac z8+\frac{3z^2}{64}-\cdots\right)$$
$$f(z)=\frac{-1}{16}\left(34+15z+\frac{67}8z^2+\cdots\right),\qquad |z|<2$$
(region of convergence of radius 2.)
:::
:::

```{.figure #m06-radius-2 caption="The poles $z=-4$ and $z=2$; the circle of convergence about the origin has radius $2$"}
```

::: {.example}
Find the Laurent series of $f(z)=\cos z^2$ in a neighbourhood of $z_0=0$.

::: {.solution}
From the definition of the cosine function,
$$\cos z=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots$$
$$f(z)=\cos z^2=1-\frac{z^4}{2!}+\frac{z^8}{4!}-\frac{z^{12}}{6!}+-\cdots$$
The region of convergence is the whole complex plane, with infinite radius of convergence.
:::
:::

::: {.example}
Find the Laurent series of $f(z)=\dfrac{\cos z}{1-z^2}$ in a neighbourhood of $z_0=0$.

::: {.solution}
$$\left\{\begin{aligned}
\frac1{1-z^2}&=1+z^2+z^4+z^6+\cdots&&|z^2|<1\ \ \ |z|<1\\
\cos z&=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots&&|z|<\infty
\end{aligned}\right.$$
$$\begin{aligned}
f(z)=\frac{\cos z}{1-z^2}&=\big(1+z^2+z^4+z^6+\cdots\big)\left(1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots\right)\\
&=1+\left(1-\frac1{2!}\right)z^2+\left(1+\frac1{4!}-\frac1{2!}\right)z^4+\cdots,\qquad |z|<1
\end{aligned}$$
:::
:::

::: {.example}
Find the Laurent series of $f(z)=\dfrac1{z^4}$ in a neighbourhood of $z_0=1$.

::: {.solution}
$$g(z)=\frac1z=\frac1{z-1+1}=\frac1{1+(z-1)}=1-(z-1)+(z-1)^2-(z-1)^3+-\cdots,\qquad |z-1|<1$$
$$\frac d{dz}g(z)=\frac{-1}{z^2}=-1+2(z-1)-3(z-1)^2+4(z-1)^3-+\cdots,\qquad |z-1|<1$$
$$\frac{d^2}{dz^2}g(z)=\frac2{z^3}=2-6(z-1)+12(z-1)^2-20(z-1)^3+-\cdots,\qquad |z-1|<1$$
$$\frac{d^3}{dz^3}g(z)=\frac{-6}{z^4}=-6+24(z-1)-60(z-1)^2-+\cdots,\qquad |z-1|<1$$
$$f(z)=\frac1{z^4}=1-4(z-1)+10(z-1)^2-+\cdots$$
:::
:::

```{.figure #m06-radius-3 caption="The region of convergence of the series about $z_0=1$ is a disc of radius $1$ (up to the pole $z=0$)"}
```

::: {.exercise}
Find the Laurent expansions of the following functions in a neighbourhood of $z_0=0$:

1. $f_1(z)=\dfrac1{\sqrt{1-z^2}}$
2. $f_2(z)=\sin^{-1}z$
3. $f_3(z)=\dfrac{e^z}{z^2(z^2+1)}$
4. Expand $\sinh z$ in powers of $(z-\pi i)$ and prove that $\displaystyle\lim_{z\to\pi i}\frac{\sinh z}{z-\pi i}=-1$
5. Prove that $\displaystyle z\cosh z^2=z+\sum_{n=1}^{\infty}\frac1{(2n)!}\,z^{4n+1}$
:::

## Examples of Singular Points and Residues

::: {.example}
Find the Laurent series of $f(z)=\dfrac{z}{(z+1)(z+4)^3}$ in the neighbourhoods of its non-analytic points, and find the residue at those points.

::: {.solution}
The function is not analytic at $z=-1$ and $z=-4$.

**(a)** In a neighbourhood of $z=-1$, a circle centred at this point with radius less than $3$ ($|z+1|<3$) does not contain the isolated singular point $z=-4$.
$$\frac{z}{(z+4)^3}=\frac{z+4-4}{(z+4)^3}=\frac{z+4}{(z+4)^3}+\frac{-4}{(z+4)^3}=\frac1{(z+4)^2}-\frac4{(z+4)^3}$$
$$\frac1{z+4}=\frac1{(z+1)+3}=\frac13\,\frac1{1+\frac{z+1}3}=\frac13\left[1-\frac{z+1}3+\left(\frac{z+1}3\right)^2-\left(\frac{z+1}3\right)^3+-\cdots\right]$$
$$\frac{-1}{(z+4)^2}=\frac13\left[-\frac13+\frac2{3^2}(z+1)-\frac3{3^3}(z+1)^2+-\cdots\right]\;\Longrightarrow\;\frac1{(z+4)^2}=\frac19-\frac2{27}(z+1)+\frac1{27}(z+1)^2-+\cdots$$
$$\frac1{(z+4)^3}=\frac16\left[\frac2{3^2}-\frac{2\times3}{3^3}(z+1)+\frac{3\times4}{3^4}(z+1)^2-\frac{4\times5}{3^5}(z+1)^3+-\cdots\right]=\frac1{27}-\frac1{27}(z+1)+\frac2{81}(z+1)^2-+\cdots$$
$$\frac z{(z+4)^3}=\frac1{(z+4)^2}-\frac4{(z+4)^3}=-\frac1{27}+\frac2{27}(z+1)-\frac5{81}(z+1)^2+\cdots$$
$$f(z)=\frac1{z+1}\,\frac z{(z+4)^3}=-\frac1{27}\,\frac1{z+1}+\frac2{27}-\frac5{81}(z+1)+\cdots$$
Type of singular point: a simple pole (of order $1$). Residue: $\operatorname{Res}\{f(z)\}\big|_{z=-1}=-\dfrac1{27}$.

**(b)** In a neighbourhood of $z=-4$, a circle centred at this point with radius less than $3$ ($|z+4|<3$) does not contain the isolated singular point $z=-1$.
$$\frac z{z+1}=\frac{z+1-1}{z+1}=\frac{z+1}{z+1}-\frac1{z+1}=1-\frac1{z+1}$$
$$\frac1{z+1}=\frac1{z+4-3}=\frac1{-3+(z+4)}=\frac{-1}3\,\frac1{1-\frac{z+4}3}=\frac{-1}3\left[1+\frac{z+4}3+\frac{(z+4)^2}{3^2}+\cdots\right],\qquad |z+4|<3$$
$$\frac z{z+1}=1+\frac13+\frac1{3^2}(z+4)+\frac1{3^3}(z+4)^2+\frac1{3^4}(z+4)^3+\cdots$$
$$f(z)=\frac z{(z+1)(z+4)^3}=\frac1{(z+4)^3}\,\frac z{z+1}=\frac{4/3}{(z+4)^3}+\frac1{3^2}\frac1{(z+4)^2}+\frac1{3^3}\frac1{z+4}+\frac1{3^4}+\frac1{3^5}(z+4)+\frac1{3^6}(z+4)^2+\cdots$$
Type of singular point: a pole of order $3$. Residue: $\operatorname{Res}\{f(z)\}\big|_{z=-4}=\dfrac1{27}$.
:::
:::

```{.figure #m06-poles-1 caption="The poles $z=-1$ and $z=-4$ of $f(z)=\\frac{z}{(z+1)(z+4)^3}$"}
```

::: {.example}
Find the Laurent series of $f(z)=e^{1/z}$ in a neighbourhood of its non-analytic point, and find the residue at that point.

::: {.solution}
$$e^z=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots\;\Longrightarrow\;e^{1/z}=1+\frac1z+\frac1{2!\,z^2}+\frac1{3!\,z^3}+\cdots$$
Type of singular point: an essential singularity (infinitely many negative powers). Residue: $\operatorname{Res}\{f(z)\}\big|_{z=0}=1$.
:::
:::

::: {.example}
Find the Laurent series of $f(z)=\cos\!\left(\dfrac z{z-1}\right)$ in a neighbourhood of its non-analytic point, and find the residue at that point.

::: {.solution}
$$\frac z{z-1}=1+\frac1{z-1}\;\Longrightarrow\;\cos\!\left(\frac z{z-1}\right)=\cos\!\left(1+\frac1{z-1}\right)=\cos1\cos\!\left(\frac1{z-1}\right)-\sin1\sin\!\left(\frac1{z-1}\right)$$
$$\cos z=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots,\qquad \sin z=z-\frac{z^3}{3!}+\frac{z^5}{5!}-+\cdots$$
$$\begin{aligned}
\cos\!\left(\frac z{z-1}\right)&=\cos1\left(1-\frac1{2!}\frac1{(z-1)^2}+\frac1{4!}\frac1{(z-1)^4}-+\cdots\right)\\
&\quad-\sin1\left(\frac1{z-1}-\frac1{3!}\frac1{(z-1)^3}+\frac1{5!}\frac1{(z-1)^5}-+\cdots\right)\\
&=\cos1-\sin1\,\frac1{z-1}-\cos1\,\frac1{2!}\frac1{(z-1)^2}+\sin1\,\frac1{3!}\frac1{(z-1)^3}+\cdots
\end{aligned}$$
Type of singular point: an essential singularity. Residue: $\operatorname{Res}\{f(z)\}\big|_{z=1}=-\sin1$.
:::
:::

::: {.theorem title="Residue at a simple pole"}
Prove that if $f(z)=q(z)/g(z)$ and $g(z)$ has a simple root at $z_0$, then
$$\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=\frac{q(z_0)}{g'(z_0)}$$
:::

::: {.proof}
Since $z_0$ is a pole of order $1$ we have ($p=1$):
$$\begin{aligned}
\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=A_1&=\frac1{(p-1)!}\left.\frac{d^{\,p-1}}{dz^{\,p-1}}\Big[(z-z_0)^pf(z)\Big]\right|_{z=z_0}=(z-z_0)\frac{q(z)}{g(z)}\Bigg|_{z=z_0}\\
&=(z-z_0)\frac{q(z)}{g(z)-g(z_0)}\Bigg|_{z=z_0}=\frac{q(z)}{\dfrac{g(z)-g(z_0)}{z-z_0}}\Bigg|_{z=z_0}=\frac{q(z_0)}{g'(z_0)}
\end{aligned}$$
:::

::: {.exercise}
Find the Laurent series of the following functions about $z=0$ and determine the type of this point.
$$f_1(z)=\frac z{e^z-1},\qquad f_2(z)=\frac{e^{-z}}{z^3},\qquad f_3(z)=\frac1{z^2(1-z^2)},\qquad f_4(z)=\frac{\sin z^2}{z^3}$$
:::
