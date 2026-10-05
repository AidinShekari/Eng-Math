# Properties of Fourier Series, Parseval's Theorem and the Complex Form

## Approximating a Periodic Function by a Finite Trigonometric Series

::: {.theorem}
For an $N$-term approximation of a periodic function $f(x)$ by a series of sines and cosines, the best coefficients (in the MMSE sense) are the Fourier series coefficients.
:::

Consider a periodic function with period $2\pi$:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+b_n\sin nx,\qquad f(x)=f(x+2\pi)$$
The $N$-term trigonometric approximation:
$$f(x)\approx a_0+\sum_{n=1}^{N}a_n\cos nx+b_n\sin nx$$
Is the following trigonometric approximation not **better**?
$$F(x)\triangleq\alpha_0+\sum_{n=1}^{N}\alpha_n\cos nx+\beta_n\sin nx$$
What is the **criterion** for an approximation being better? One criterion: the error function:
$$E(x)=\big|f(x)-F(x)\big|=\left|f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right|$$
A good criterion: the mean squared error:
$$D\triangleq\int_{-\pi}^{\pi}E^2(x)\,dx=\int_{-\pi}^{\pi}\left|f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right|^2dx$$

::: {.proof}
For the best approximation we minimize the mean squared error. This is done by differentiating $D$ with respect to the coefficients of the trigonometric series and setting these derivatives equal to zero. In other words:
$$\frac{\partial D}{\partial\alpha_0}=-2\int_{-\pi}^{\pi}\left[f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right]dx=0$$
$$\int_{-\pi}^{\pi}f(x)\,dx=\int_{-\pi}^{\pi}\left[\alpha_0+\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right]dx=2\pi\alpha_0\quad\Longrightarrow\quad\alpha_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=a_0$$
$$\frac{\partial D}{\partial\alpha_m}=0\quad\Longrightarrow\quad\alpha_m=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos mx\,dx=a_m$$
$$\frac{\partial D}{\partial\beta_m}=0\quad\Longrightarrow\quad\beta_m=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin mx\,dx=b_m$$
The best finite trigonometric approximation of a periodic function is the finite Fourier series.
:::

## Differentiation and Integration of Fourier Series

::: {.theorem title="Differentiating a Fourier series"}
If $f(x)$ is periodic with period $T$, continuous and has a Fourier series, then its derivative is also periodic, and its Fourier series is obtained by differentiating the Fourier series of the function.
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$\Longrightarrow\quad f'(x)=\sum_{n=1}^{\infty}\left(\frac{2\pi}Tnb_n\right)\cos\frac{2\pi}Tnx+\left(-\frac{2\pi}Tna_n\right)\sin\frac{2\pi}Tnx$$
:::

::: {.theorem title="Integrating a Fourier series"}
If $f(x)$ is periodic with period $T$ and has a Fourier series, then the definite integral of this function can be computed by integrating the Fourier series of the function.
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$\Longrightarrow\quad\int_0^xf(t)\,dt=a_0x+\sum_{n=1}^{\infty}\left(\frac T{2\pi n}a_n\sin\frac{2\pi}Tnx-\frac T{2\pi n}b_n\cos\frac{2\pi}Tnx+\frac T{2\pi n}b_n\right)$$
:::

## Rayleigh's Theorem

::: {.theorem title="Rayleigh's theorem"}
If the functions $f(x)$ and $g(x)$ are periodic with period $T$ and their Fourier series exist as
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$g(x)=\alpha_0+\sum_{n=1}^{\infty}\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx$$
then
$$\frac2T\int_Tf(x)\,\overline{g(x)}\,dx=2a_0\overline{\alpha_0}+\sum_{n=1}^{\infty}a_n\overline{\alpha_n}+b_n\overline{\beta_n}$$
:::

::: {.proof}
Proof, assuming $g(x)$ is real:
$$\begin{aligned}
\frac2T\int_Tf(x)g(x)\,dx&=\frac2T\int_Tf(x)\left(\alpha_0+\sum_{n=1}^{\infty}\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx\right)dx\\
&=\frac2T\int_Tf(x)\alpha_0\,dx+\sum_{n=1}^{\infty}\frac2T\int_Tf(x)\left(\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx\right)dx\\
&=\underbrace{\frac2T\int_Tf(x)\,dx}_{2a_0}\,\alpha_0+\sum_{n=1}^{\infty}\underbrace{\frac2T\int_Tf(x)\cos\frac{2\pi}Tnx\,dx}_{a_n}\,\alpha_n+\underbrace{\frac2T\int_Tf(x)\sin\frac{2\pi}Tnx\,dx}_{b_n}\,\beta_n\\
&=2a_0\alpha_0+\sum_{n=1}^{\infty}a_n\alpha_n+b_n\beta_n
\end{aligned}$$
:::

## Parseval's Theorem

::: {.theorem title="Parseval's theorem"}
If the function $f(x)$ is periodic with period $T$ and its Fourier series exists as
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
then
$$\frac2T\int_T|f(x)|^2\,dx=2|a_0|^2+\sum_{n=1}^{\infty}\big(|a_n|^2+|b_n|^2\big)$$
:::

::: {.proof}
In Rayleigh's identity, replacing $g(x)$ by $f(x)$ gives Parseval's identity.
:::

By Parseval's identity, the power of the function $f(x)$ can be obtained from the Fourier coefficients. If the function is expressed by an $N$-term approximation of sines and cosines, then by the relation above the power of the approximating function is less than the power of $f(x)$, and we have:

::: {.important title="Bessel's inequality"}
$$\frac2T\int_T|f(x)|^2\,dx\ \ge\ 2|a_0|^2+\sum_{n=1}^{N}\big(|a_n|^2+|b_n|^2\big)$$
:::

::: {.example}
For the function $f(x)$ below, how many terms of the Fourier series are needed for at least 94 percent of the power to remain in the approximating function?

::: {.solution}
$$f(x)=\sum_{n=1}^{\infty}\frac{2k}{n\pi}(1-\cos n\pi)\sin nx$$
$$\frac2T\int_T|f(x)|^2\,dx=\frac1\pi\int_{-\pi}^{\pi}k^2\,dx=\frac2\pi\big[k^2x\big]_0^\pi=2k^2$$
$$\frac{\displaystyle\sum_{n=1}^{N}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\ge0.94$$
$$\frac{\displaystyle\sum_{n=1}^{7}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\cong0.9496,\qquad \frac{\displaystyle\sum_{n=1}^{5}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\cong0.9331\quad\Longrightarrow\quad N=7$$
:::
:::

```{.figure #m09-power-example caption="The square wave $\\pm k$ with period $2\\pi$ used in the power example"}
```

## The Complex Form of the Fourier Series

Suppose $f(x)$ is periodic and, merely for simplicity, has period $2\pi$. Then
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+b_n\sin nx$$
Using Euler's formula $e^{ix}=\cos x+i\sin x$:
$$\cos nx=\frac{e^{inx}+e^{-inx}}2,\qquad \sin nx=\frac{e^{inx}-e^{-inx}}{2i},\qquad \frac1i=-i$$
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\left(\frac{e^{inx}+e^{-inx}}2\right)+b_n\left(\frac{e^{inx}-e^{-inx}}{2i}\right)=\underbrace{a_0}_{c_0}+\sum_{n=1}^{\infty}\underbrace{\left(\frac{a_n-ib_n}2\right)}_{c_n}e^{inx}+\underbrace{\left(\frac{a_n+ib_n}2\right)}_{c_{-n}}e^{-inx}$$
$$c_n=\frac{a_n-ib_n}2=\frac12\left\{\frac1\pi\int_{2\pi}f(x)\cos nx\,dx-i\frac1\pi\int_{2\pi}f(x)\sin nx\,dx\right\}=\frac1{2\pi}\int_{2\pi}f(x)\big(\cos nx-i\sin nx\big)\,dx=\frac1{2\pi}\int_{2\pi}f(x)e^{-inx}\,dx$$
$$c_{-n}=\frac{a_n+ib_n}2=\frac1{2\pi}\int_{2\pi}f(x)\big(\cos nx+i\sin nx\big)\,dx=\frac1{2\pi}\int_{2\pi}f(x)e^{inx}\,dx$$

::: {.important title="The complex form of the Fourier series"}
$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{inx},\qquad c_n=\frac1{2\pi}\int_{2\pi}f(x)e^{-inx}\,dx$$
For an arbitrary period:
$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{i\frac{2\pi}Tnx},\qquad c_n=\frac1T\int_Tf(x)e^{-i\frac{2\pi}Tnx}\,dx$$
$$\frac1T\int_T|f(x)|^2\,dx=\sum_{n=-\infty}^{\infty}|c_n|^2$$
:::
