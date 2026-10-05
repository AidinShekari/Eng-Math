# The Fourier Integral

## Fourier Analysis of Non-Periodic Functions

To be able to use Fourier analysis for non-periodic functions, we first regard the function as periodic and then let the period tend to infinity.

```{.figure #m03-periodic-extension caption="A non-periodic function $f(x)$ and its periodic extension $\\tilde f(x)$ with period $T$"}
```

$$\tilde f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$a_0=\frac1T\int_{-T/2}^{T/2}f(x)\,dx,\qquad a_n=\frac2T\int_{-T/2}^{T/2}f(x)\cos\frac{2\pi}Tnx\,dx,\qquad b_n=\frac2T\int_{-T/2}^{T/2}f(x)\sin\frac{2\pi}Tnx\,dx$$
$$\begin{aligned}
\tilde f(x)&=\left(\frac1T\int_{-T/2}^{T/2}f(t)\,dt\right)+\sum_{n=1}^{\infty}\Bigg\{\left(\frac2T\int_{-T/2}^{T/2}f(t)\cos\frac{2\pi}Tnt\,dt\right)\cos\frac{2\pi}Tnx\\
&\qquad+\left(\frac2T\int_{-T/2}^{T/2}f(t)\sin\frac{2\pi}Tnt\,dt\right)\sin\frac{2\pi}Tnx\Bigg\}
\end{aligned}$$
$$\tilde f(x)=\left(\frac1T\int_{-T/2}^{T/2}f(t)\,dt\right)+\frac2T\sum_{n=1}^{\infty}\left\{\int_{-T/2}^{T/2}f(t)\left(\cos\frac{2\pi}Tnt\cos\frac{2\pi}Tnx+\sin\frac{2\pi}Tnt\sin\frac{2\pi}Tnx\right)dt\right\}$$
$$\tilde f(x)=\left(\frac1T\int_{-T/2}^{T/2}f(t)\,dt\right)+\frac2T\sum_{n=1}^{\infty}\left\{\int_{-T/2}^{T/2}f(t)\cos\frac{2\pi}Tn(t-x)\,dt\right\}$$

- To obtain the Fourier analysis of the function $f(x)$ we must let $T$ tend to **infinity**.
- Suppose $f(x)$ is an integrable function, so that
$$\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}f(t)\,dt=0$$

Then
$$f(x)=\lim_{T\to\infty}\frac2T\sum_{n=1}^{\infty}\left\{\int_{-T/2}^{T/2}f(t)\cos\frac{2\pi}Tn(t-x)\,dt\right\}$$
$$\omega_n\triangleq\frac{2\pi}Tn\quad\Longrightarrow\quad\Delta\omega\triangleq\omega_n-\omega_{n-1}=\frac{2\pi}Tn-\frac{2\pi}T(n-1)=\frac{2\pi}T\quad\Longrightarrow\quad\frac2T=\frac{\Delta\omega}\pi$$
$$f(x)=\lim_{T\to\infty}\frac1\pi\sum_{n=1}^{\infty}\left\{\int_{-T/2}^{T/2}f(t)\cos\omega_n(t-x)\,dt\right\}\Delta\omega$$
If $T\to\infty$, then $\sum_{n=1}^{\infty}\to\int_0^\infty$, $\Delta\omega\to d\omega$ and $\omega_n\to\omega$:
$$\begin{aligned}
f(x)&=\frac1\pi\int_0^\infty\left\{\int_{-\infty}^{\infty}f(t)\cos\omega(t-x)\,dt\right\}d\omega\\
&=\frac1\pi\int_0^\infty\left\{\int_{-\infty}^{\infty}f(t)\big(\cos\omega t\cos\omega x+\sin\omega t\sin\omega x\big)\,dt\right\}d\omega\\
&=\frac1\pi\int_0^\infty\left\{\cos\omega x\int_{-\infty}^{\infty}\big(f(t)\cos\omega t\big)\,dt+\sin\omega x\int_{-\infty}^{\infty}\big(f(t)\sin\omega t\big)\,dt\right\}d\omega
\end{aligned}$$
$$A(\omega)\triangleq\int_{-\infty}^{\infty}f(t)\cos\omega t\,dt,\qquad B(\omega)\triangleq\int_{-\infty}^{\infty}f(t)\sin\omega t\,dt\quad\Longrightarrow\quad f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega$$

## The Fourier Integral

::: {.important title="The Fourier integral and the sine and cosine transforms"}
$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega\qquad\text{(the Fourier integral; synthesis equation)}$$
$$A(\omega)\triangleq\int_{-\infty}^{\infty}f(t)\cos\omega t\,dt\qquad\text{(the Fourier cosine transform)}$$
$$B(\omega)\triangleq\int_{-\infty}^{\infty}f(t)\sin\omega t\,dt\qquad\text{(the Fourier sine transform)}$$
(the analysis equations)
:::

::: {.theorem}
A sufficient condition for the existence of the Fourier integral of a function $f(x)$ is that the function be piecewise continuous, have right and left derivatives at every point, and be absolutely integrable, i.e.
$$\int_{-\infty}^{\infty}|f(x)|\,dx<\infty$$
At points of discontinuity, the value of the Fourier integral equals the average of the left and right limits of $f(x)$ at those points.
:::

## The Complex Form of the Fourier Integral (the Fourier Transform)

$$f(x)=\frac1\pi\int_0^\infty\left\{\int_{-\infty}^{\infty}f(t)\cos\omega(t-x)\,dt\right\}d\omega$$
The expression $\displaystyle\int_{-\infty}^{\infty}f(t)\cos\omega(t-x)\,dt$ is an even function of $\omega$, hence
$$f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)\cos\omega(t-x)\,dt\right\}d\omega$$
and the expression $\displaystyle\int_{-\infty}^{\infty}f(t)\sin\omega(t-x)\,dt$ is an odd function of $\omega$, hence
$$\frac{-i}{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)\sin\omega(t-x)\,dt\right\}d\omega=0$$
$$f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)\cos\omega(t-x)\,dt\right\}d\omega-\frac i{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)\sin\omega(t-x)\,dt\right\}d\omega$$
$$f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)\big(\cos\omega(t-x)-i\sin\omega(t-x)\big)\,dt\right\}d\omega$$
$$f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)e^{-i\omega(t-x)}\,dt\right\}d\omega=\frac1{2\pi}\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt\right\}e^{i\omega x}\,d\omega$$

::: {.important title="The Fourier transform"}
$$f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{i\omega x}\,d\omega\qquad\text{(the Fourier integral; synthesis equation)}$$
$$F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt\qquad\text{(the Fourier transform; analysis equation)}$$
:::

The complex form of the Fourier series (review):
$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{i\frac{2\pi}Tnx}\quad\text{(Fourier series; synthesis equation)},\qquad c_n=\frac1T\int_Tf(x)e^{-i\frac{2\pi}Tnx}\,dx\quad\text{(Fourier coefficients; analysis equation)}$$

## The Function $\operatorname{Si}(u)$

$$\operatorname{Si}(x)\triangleq\int_0^x\frac{\sin w}{w}\,dw$$

- odd;
- has finite asymptotic values at infinity.

```{.figure #m03-si caption="The function $\\operatorname{Si}(u)$ (solid) and the function $\\sin u/u$ (dashed)"}
```

::: {.theorem title="Lemma"}
$$\int_0^\infty\frac{\sin\alpha w}{w}\,dw=\begin{cases}\dfrac\pi2&\alpha>0\\[1mm] 0&\alpha=0\\[1mm] -\dfrac\pi2&\alpha<0\end{cases}$$
:::

::: {.proof}
For $\alpha=0$ the lemma is obvious. With the substitution $\tau=\alpha w$:
$$\int_0^x\frac{\sin\alpha w}{w}\,dw=\int_0^{\alpha x}\frac{\sin\tau}{\tau/\alpha}\,\frac{d\tau}{\alpha}=\int_0^{\alpha x}\frac{\sin\tau}{\tau}\,d\tau=\operatorname{Si}(\alpha x),\qquad \operatorname{Si}(\alpha x)=-\operatorname{Si}(-\alpha x)$$
So it suffices to prove the lemma for positive values of $\alpha$.
$$F(\alpha)\triangleq\int_0^\infty e^{-\alpha t}\frac{\sin t}{t}\,dt,\qquad F(0)=\operatorname{Si}(+\infty)=\;?$$
$$F'(\alpha)=\int_0^\infty-t\,e^{-\alpha t}\frac{\sin t}t\,dt=-\int_0^\infty e^{-\alpha t}\sin t\,dt=-\left[\frac{e^{-\alpha t}}{1+\alpha^2}\big(-\alpha\sin t-\cos t\big)\right]_0^\infty=\frac{-1}{1+\alpha^2}$$
$$\alpha>0:\quad F(\alpha)=-\tan^{-1}\alpha+C,\qquad F(\alpha\to\infty)=0\quad\Longrightarrow\quad C=F(\infty)+\tan^{-1}\infty=\frac\pi2$$
$$F(\alpha)=-\tan^{-1}\alpha+\frac\pi2\quad\Longrightarrow\quad F(0)=\operatorname{Si}(+\infty)=\frac\pi2$$
:::

## Examples of the Fourier Integral

::: {.example}
Express the rectangular pulse below as a Fourier integral.
$$f(x)=\begin{cases}1&|x|<1\\ 0&|x|>1\end{cases}$$

::: {.solution}
Since $f(x)$ is even, the Fourier sine transform vanishes: $B(\omega)=0$.
$$A(\omega)=\int_{-\infty}^{\infty}f(t)\cos\omega t\,dt=\int_{-1}^{1}\cos\omega t\,dt=\frac2\omega\sin\omega$$
$$f(x)=\frac1\pi\int_0^\infty\frac2\omega\sin\omega\cos\omega x\,d\omega=\frac1\pi\int_0^\infty\frac1\omega\big[\sin(1-x)\omega+\sin(1+x)\omega\big]\,d\omega$$
$$=\frac1\pi\left[\int_0^\infty\frac{\sin(1-x)\omega}\omega\,d\omega+\int_0^\infty\frac{\sin(1+x)\omega}\omega\,d\omega\right]=\begin{cases}0&x<-1\\ 1/2&x=-1\\ 1&-1<x<1\\ 1/2&x=1\\ 0&x>1\end{cases}$$
Note: the value of the Fourier integral at the points of discontinuity (using the lemma above).
:::
:::

```{.figure #m03-pulse caption="The rectangular pulse $f(x)=1$ for $|x|<1$"}
```

::: {.example}
Express the exponential function below as a Fourier integral.
$$f(x)=\begin{cases}0&x<0\\ e^{-x}&x>0\end{cases}$$

::: {.solution}
$$A(\omega)=\int_{-\infty}^{\infty}f(x)\cos\omega x\,dx=\int_0^\infty e^{-x}\cos\omega x\,dx=\frac{e^{-x}}{1+\omega^2}\big(-\cos\omega x+\omega\sin\omega x\big)\Big|_0^\infty=\frac1{1+\omega^2}$$
$$B(\omega)=\int_{-\infty}^{\infty}f(x)\sin\omega x\,dx=\int_0^\infty e^{-x}\sin\omega x\,dx=\frac{e^{-x}}{1+\omega^2}\big(-\sin\omega x-\omega\cos\omega x\big)\Big|_0^\infty=\frac\omega{1+\omega^2}$$
$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega=\frac1\pi\int_0^\infty\frac{\cos\omega x+\omega\sin\omega x}{1+\omega^2}\,d\omega$$
$$f(x=0)=\frac1\pi\int_0^\infty\frac1{1+\omega^2}\,d\omega=\frac1\pi\Big[\tan^{-1}\omega\Big]_0^\infty=\frac1\pi\times\frac\pi2=\frac12$$
:::
:::

::: {.example}
Express the function below as a Fourier integral.
$$f(x)=e^{-|x|}$$

::: {.solution}
Since $f(x)$ is even, the Fourier sine transform vanishes.
$$A(\omega)=\int_{-\infty}^{\infty}f(x)\cos\omega x\,dx=2\int_0^\infty e^{-x}\cos\omega x\,dx=\frac{2e^{-x}}{1+\omega^2}\big(-\cos\omega x+\omega\sin\omega x\big)\Big|_0^\infty=\frac2{1+\omega^2}$$
$$B(\omega)=\int_{-\infty}^{\infty}e^{-|x|}\sin\omega x\,dx=0$$
$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega=\frac2\pi\int_0^\infty\frac{\cos\omega x}{1+\omega^2}\,d\omega$$
$$f(x=0)=\frac2\pi\int_0^\infty\frac1{1+\omega^2}\,d\omega=\frac2\pi\Big[\tan^{-1}\omega\Big]_0^\infty=\frac2\pi\times\frac\pi2=1$$
:::
:::

```{.figure #m03-exp-abs caption="The function $f(x)=e^{-|x|}$"}
```

::: {.example}
Express the function below as a Fourier integral.
$$f(x)=\begin{cases}\sin x&|x|\le\pi\\ 0&|x|>\pi\end{cases}$$

::: {.solution}
Since $f(x)$ is odd, the Fourier cosine transform vanishes.
$$A(\omega)=\int_{-\pi}^{\pi}\sin x\cos\omega x\,dx=0$$
$$B(\omega)=\int_{-\pi}^{\pi}\sin x\sin\omega x\,dx=2\int_0^\pi\sin x\sin\omega x\,dx=\int_0^\pi\big[\cos(1-\omega)x-\cos(1+\omega)x\big]dx=\left[\frac{\sin(1-\omega)x}{1-\omega}-\frac{\sin(1+\omega)x}{1+\omega}\right]_0^\pi=\frac{2\sin(\omega\pi)}{1-\omega^2}$$
$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega=\frac2\pi\int_0^\infty\frac{\sin(\omega\pi)\sin\omega x}{1-\omega^2}\,d\omega$$
:::
:::

```{.figure #m03-sine-pulse caption="The function $f(x)=\\sin x$ for $|x|\\le\\pi$ and zero outside"}
```

::: {.example}
Express the function below as a Fourier integral.
$$f(x)=\begin{cases}x^2&|x|\le a\\ 0&|x|>a\end{cases}$$

::: {.solution}
Since $f(x)$ is even, the Fourier sine transform vanishes.
$$B(\omega)=\int_{-a}^{a}x^2\sin\omega x\,dx=0$$
$$A(\omega)=\int_{-\infty}^{\infty}f(x)\cos\omega x\,dx=2\int_0^ax^2\cos\omega x\,dx=2\left[\frac{x^2}\omega\sin\omega x+\frac{2x}{\omega^2}\cos\omega x-\frac2{\omega^3}\sin\omega x\right]_0^a=2\left[\left(\frac{a^2}\omega-\frac2{\omega^3}\right)\sin\omega a+\frac{2a}{\omega^2}\cos\omega a\right]$$
$$f(x)=\frac2\pi\int_0^\infty\left[\left(\frac{a^2}\omega-\frac2{\omega^3}\right)\sin\omega a+\frac{2a}{\omega^2}\cos\omega a\right]\cos\omega x\,d\omega$$
:::
:::

## Some Properties of the Fourier Integral

All the properties follow from the synthesis and analysis equations:
$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega,\qquad A(\omega)\triangleq\int_{-\infty}^{\infty}f(x)\cos\omega x\,dx,\qquad B(\omega)\triangleq\int_{-\infty}^{\infty}f(x)\sin\omega x\,dx$$

### Time Scaling

$$f(x)\to f(ax),\quad a\in\mathbb{R}\quad\Longrightarrow\quad\begin{cases}A(\omega)\to\dfrac1{|a|}A\!\left(\dfrac\omega a\right)\\[2mm] B(\omega)\to\dfrac1{|a|}B\!\left(\dfrac\omega a\right)\end{cases}$$

::: {.proof}
$$A_1(\omega)=\int_{-\infty}^{\infty}f(ax)\cos\omega x\,dx\ \ \begin{cases}\underset{u=ax}{\overset{a>0}{=}}\ \displaystyle\int_{-\infty}^{\infty}f(u)\cos\frac\omega au\,\frac{du}a=\frac1aA\!\left(\frac\omega a\right)\\[3mm]\underset{u=ax}{\overset{a<0}{=}}\ \displaystyle\int_{+\infty}^{-\infty}f(u)\cos\frac\omega au\,\frac{du}a=-\frac1a\int_{-\infty}^{\infty}f(u)\cos\frac\omega au\,du=-\frac1aA\!\left(\frac\omega a\right)\end{cases}\ \Longrightarrow\ A_1(\omega)=\frac1{|a|}A\!\left(\frac\omega a\right)$$
:::

### Parseval's Identity

$$\int_{-\infty}^{\infty}f^2(x)\,dx=\frac1\pi\int_0^\infty\big\{A^2(\omega)+B^2(\omega)\big\}\,d\omega$$

::: {.proof}
$$\begin{aligned}
\int_{-\infty}^{\infty}f^2(x)\,dx&=\int_{-\infty}^{\infty}f(x)\left(\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega\right)dx\\
&=\frac1\pi\int_0^\infty\left\{A(\omega)\left[\int_{-\infty}^{\infty}f(x)\cos\omega x\,dx\right]+B(\omega)\left[\int_{-\infty}^{\infty}f(x)\sin\omega x\,dx\right]\right\}d\omega\\
&=\frac1\pi\int_0^\infty\big\{A^2(\omega)+B^2(\omega)\big\}\,d\omega
\end{aligned}$$
:::

### The Time Derivative

$$f(x)=\frac1\pi\int_0^\infty\big\{A(\omega)\cos\omega x+B(\omega)\sin\omega x\big\}\,d\omega\quad\Longrightarrow\quad f'(x)=\frac1\pi\int_0^\infty\big\{\omega B(\omega)\cos\omega x-\omega A(\omega)\sin\omega x\big\}\,d\omega$$
(using the rule for differentiating an integral:)
$$\frac\partial{\partial z}\int_{a(z)}^{b(z)}f(x,z)\,dx=\int_{a(z)}^{b(z)}\frac{\partial f(x,z)}{\partial z}\,dx+f\big(b(z),z\big)\frac{db(z)}{dz}-f\big(a(z),z\big)\frac{da(z)}{dz}$$

### The Frequency Derivative

$$\frac{dA(\omega)}{d\omega}=A'(\omega)=\int_{-\infty}^{\infty}-xf(x)\sin\omega x\,dx\quad\Longrightarrow\quad\int_{-\infty}^{\infty}\big(xf(x)\big)\sin\omega x\,dx=-A'(\omega)$$
$$\frac{dB(\omega)}{d\omega}=B'(\omega)=\int_{-\infty}^{\infty}xf(x)\cos\omega x\,dx\quad\Longrightarrow\quad\int_{-\infty}^{\infty}\big(xf(x)\big)\cos\omega x\,dx=B'(\omega)$$
$$xf(x)=\frac1\pi\int_0^\infty\big\{B'(\omega)\cos\omega x-A'(\omega)\sin\omega x\big\}\,d\omega$$

::: {.exercise}
Prove the following identities:

1. $\displaystyle\int_0^\infty\frac{\cos xw+w\sin xw}{1+w^2}\,dw=\begin{cases}0&x<0\\ \pi/2&x=0\\ \pi e^{-x}&x>0\end{cases}$
2. $\displaystyle\int_0^\infty\frac{\sin\pi w\,\sin xw}{1-w^2}\,dw=\begin{cases}\dfrac\pi2\sin x&0\le x\le\pi\\[1mm] 0&x>\pi\end{cases}$
3. $\displaystyle\int_0^\infty\frac{1-\cos\pi w}{w}\sin xw\,dw=\begin{cases}\dfrac12\pi&0<x<\pi\\[1mm] 0&x>\pi\end{cases}$
4. $\displaystyle\int_0^\infty\frac{\cos\frac12\pi w}{1-w^2}\cos xw\,dw=\begin{cases}\dfrac12\pi\cos x&0<|x|<\frac12\pi\\[1mm] 0&|x|\ge\frac12\pi\end{cases}$
5. $\displaystyle\int_0^\infty\frac{\sin w-w\cos w}{w^2}\sin xw\,dw=\begin{cases}\dfrac12\pi x&0<x<1\\[1mm] \dfrac14\pi&x=1\\[1mm] 0&x>1\end{cases}$
:::
