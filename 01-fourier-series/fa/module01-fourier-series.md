# سری فوریه

## توابع متناوب

$$f(x+p)=f(x)\quad\Longrightarrow\quad f(x+np)=f(x)$$

```{.figure #m01-periodic caption="تابعی متناوب با دورهٔ تناوب $p$"}
```

- کوچک‌ترین مقدار مثبت $p$ به قسمی که تابع با آن تناوبی باشد، دورهٔ تناوب اصلی تابع نامیده می‌شود.
- اگر تابع با دورهٔ تناوب $p$ تناوبی باشد آنگاه با دورهٔ $np$، که $n$ یک عدد طبیعی است، نیز متناوب است.

### توابع متناوب سینوس و کسینوس

::: {.example}
تابع $\sin x$ تابعی با دورهٔ تناوب $2\pi$ تناوبی است و $\sin2x$ با دورهٔ تناوب اصلی $\pi$ تناوبی است هر چند $2\pi$ نیز دورهٔ تناوب آن هست. همینطور تابع $\sin3x$ با دورهٔ تناوب $2\pi/3$ تناوبی است، هر چند $2\pi$ نیز دورهٔ تناوب آن هست.
:::

```{.figure #m01-sincos caption="توابع $\\sin nx$ و $\\cos nx$ برای $n=1,2,3$ در بازهٔ $[0,2\\pi]$"}
```

## یادآوری از مبحث مثلثات

$$\begin{gathered}
\sin^2\alpha+\cos^2\alpha=1\\
\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta\\
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta\\
\cos2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha=\cos^2\alpha-\sin^2\alpha\\
\sin2\alpha=2\sin\alpha\cos\alpha\\
\sin^2\alpha=\frac{1-\cos2\alpha}{2}\qquad\cos^2\alpha=\frac{1+\cos2\alpha}{2}\\
\sin\alpha\sin\beta=\tfrac12\big[\cos(\alpha-\beta)-\cos(\alpha+\beta)\big]\\
\cos\alpha\cos\beta=\tfrac12\big[\cos(\alpha-\beta)+\cos(\alpha+\beta)\big]\\
\sin\alpha\cos\beta=\tfrac12\big[\sin(\alpha-\beta)+\sin(\alpha+\beta)\big]
\end{gathered}$$

## یادآوری: انتگرال‌ها و تعامد

$$\int_{-\pi}^{\pi}\sin nt\,dt=0,\qquad n\in\mathbb{Z}$$
$$\int_{-\pi}^{\pi}\cos nt\,dt=0,\qquad n\in\mathbb{Z}\setminus\{0\}$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin nt\,dt=-\frac1n\cos nt\Big|_{-\pi}^{\pi}=0,\qquad \int_{-\pi}^{\pi}\cos nt\,dt=\frac1n\sin nt\Big|_{-\pi}^{\pi}=0\qquad(n\neq0)$$
:::

### تعامد

$$\int_{-\pi}^{\pi}\sin nt\sin mt\,dt=0,\qquad n,m\in\mathbb{Z},\ n\neq m$$
$$\int_{-\pi}^{\pi}\cos nt\cos mt\,dt=0,\qquad n,m\in\mathbb{Z},\ n\neq m$$
$$\int_{-\pi}^{\pi}\sin nt\cos mt\,dt=0,\qquad n,m\in\mathbb{Z}\ \ (n\neq m\ \text{یا}\ n=m)$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin nx\sin mx\,dx=\frac12\int_{-\pi}^{\pi}\cos(n-m)x\,dx-\frac12\int_{-\pi}^{\pi}\cos(n+m)x\,dx$$
$$\int_{-\pi}^{\pi}\cos nx\cos mx\,dx=\frac12\int_{-\pi}^{\pi}\cos(n+m)x\,dx+\frac12\int_{-\pi}^{\pi}\cos(n-m)x\,dx$$
$$\int_{-\pi}^{\pi}\sin nx\cos mx\,dx=\frac12\int_{-\pi}^{\pi}\sin(n+m)x\,dx+\frac12\int_{-\pi}^{\pi}\sin(n-m)x\,dx$$
:::

$$\int_{-\pi}^{\pi}\sin^2nt\,dt=\pi,\qquad \int_{-\pi}^{\pi}\cos^2nt\,dt=\pi,\qquad n\in\mathbb{Z}\setminus\{0\}$$

::: {.proof}
$$\int_{-\pi}^{\pi}\sin^2nt\,dt=\int_{-\pi}^{\pi}\frac{1-\cos2nt}{2}\,dt=\pi,\qquad \int_{-\pi}^{\pi}\cos^2nt\,dt=\int_{-\pi}^{\pi}\frac{1+\cos2nt}{2}\,dt=\pi$$
:::

## سری فوریه

::: {.remark title="تاریخچه"}
ژوزف فوریه (۱۷۶۸–۱۸۳۰) ایدهٔ بیان توابع متناوب به صورت یک سری از توابع سینوسی را ارائه کرد. در زمان ارائهٔ این ایدهٔ انقلابی، بعضی از ریاضیدانان، از جمله لاگرانژ با عمومیت این ایده مخالفت کردند تا زمانی که دریشله شرایط همگرایی سری فوریه را بیان کرد.
:::

::: {.theorem title="سری فوریه"}
اگر تابع $f(x)$ با دورهٔ تناوب $2\pi$ متناوب باشد، آنگاه می‌توان آن را بر حسب یک سری مثلثاتی به صورت زیر بیان کرد:
$$f(x)=a_0+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big)$$
که در آن
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx,\qquad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx,\qquad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx$$
:::

::: {.proof}
فرض کنید تابع متناوب را به صورت سری مثلثاتی بالا نوشته‌ایم؛ کافی است ضرایب $a_0$، $a_n$ و $b_n$ را پیدا کنیم.

**محاسبهٔ $a_0$.** اگر از طرفین تساوی بالا روی بازه‌ای به طول $2\pi$ انتگرال بگیریم، خواهیم داشت:
$$\int_{-\pi}^{\pi}f(x)\,dx=\int_{-\pi}^{\pi}\left[a_0+\sum_{n=1}^{\infty}(a_n\cos nx+b_n\sin nx)\right]dx=a_0\int_{-\pi}^{\pi}dx+\sum_{n=1}^{\infty}\left(a_n\underbrace{\int_{-\pi}^{\pi}\cos nx\,dx}_{0}+b_n\underbrace{\int_{-\pi}^{\pi}\sin nx\,dx}_{0}\right)=2\pi a_0$$
$$\Longrightarrow\quad a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx$$
$a_0$ مقدار متوسط یا سطح DC تابع است.

**محاسبهٔ $a_n$.** اگر از طرفین تساوی بالا در $\cos mx$ ضرب کنیم و روی بازه‌ای به طول $2\pi$ انتگرال بگیریم، خواهیم داشت:
$$\int_{-\pi}^{\pi}f(x)\cos mx\,dx=\int_{-\pi}^{\pi}a_0\cos mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}a_n\cos nx\cos mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}b_n\sin nx\cos mx\,dx=\pi a_m$$
$$\Longrightarrow\quad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx$$

**محاسبهٔ $b_n$.** اگر از طرفین تساوی بالا در $\sin mx$ ضرب کنیم و روی بازه‌ای به طول $2\pi$ انتگرال بگیریم، خواهیم داشت:
$$\int_{-\pi}^{\pi}f(x)\sin mx\,dx=\int_{-\pi}^{\pi}a_0\sin mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}a_n\cos nx\sin mx\,dx+\sum_{n=1}^{\infty}\int_{-\pi}^{\pi}b_n\sin nx\sin mx\,dx=\pi b_m$$
$$\Longrightarrow\quad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx$$
:::

::: {.important title="سری فوریه و روابط اویلر"}
$$f(x)=a_0+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big),\qquad f(x+2\pi)=f(x)$$
$$a_0=\frac1{2\pi}\int_{2\pi}f(x)\,dx,\qquad a_n=\frac1\pi\int_{2\pi}f(x)\cos nx\,dx,\qquad b_n=\frac1\pi\int_{2\pi}f(x)\sin nx\,dx$$
(انتگرال روی یک دورهٔ تناوب $2\pi$ گرفته می‌شود.)
:::

::: {.remark}
مقدار سری فوریه در نقاط ناپیوستگی تابع برابر است با متوسط حد بالا و پایین در آن نقطه.
:::

## یادآوری: انتگرال معین حاصل‌ضرب دو تابع

با استفاده از روش جزء به جزء:
$$\int_\alpha^\beta f(x)g(x)\,dx=\Big[f(x)G_1(x)-f^{(1)}(x)G_2(x)+f^{(2)}(x)G_3(x)-+\cdots\Big]_\alpha^\beta$$
که در آن $f^{(k)}$ مشتق $k$-ام $f$ و $G_k$ انتگرال $k$-ام $g$ است:

| مشتق $f$ | | انتگرال $g$ |
|:---:|:---:|:---:|
| $f(x)$ | $\searrow$ | $g(x)$ |
| $f^{(1)}(x)$ | $\searrow$ | $G_1(x)$ |
| $f^{(2)}(x)$ | $\searrow$ | $G_2(x)$ |
| $f^{(3)}(x)$ | $\searrow$ | $G_3(x)$ |
| $\vdots$ | | $\vdots$ |

## مثال‌های سری فوریه

::: {.example}
سری فوریهٔ تابع زیر را به دست آورید:
$$f(x)=\begin{cases}-k&-\pi<x<0\\ \ \ k&0<x<\pi\end{cases}\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=0$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx=\frac1\pi\left[\int_{-\pi}^{0}(-k)\cos nx\,dx+\int_0^\pi k\cos nx\,dx\right]=\frac1\pi\left[-k\,\frac{\sin nx}{n}\Big|_{-\pi}^{0}+k\,\frac{\sin nx}{n}\Big|_0^\pi\right]=0$$
$$\begin{aligned}
b_n&=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx=\frac1\pi\left[\int_{-\pi}^{0}(-k)\sin nx\,dx+\int_0^\pi k\sin nx\,dx\right]\\
&=\frac1\pi\left[k\,\frac{\cos nx}{n}\Big|_{-\pi}^{0}-k\,\frac{\cos nx}{n}\Big|_0^\pi\right]=\frac k{n\pi}\big[\cos0-\cos(-n\pi)-\cos n\pi+\cos0\big]=\frac{2k}{n\pi}(1-\cos n\pi)
\end{aligned}$$
$$\cos n\pi=\begin{cases}-1&n\ \text{فرد}\\ \ \ 1&n\ \text{زوج}\end{cases}\quad\Longrightarrow\quad1-\cos n\pi=\begin{cases}2&n\ \text{فرد}\\ 0&n\ \text{زوج}\end{cases}$$
$$b_1=\frac{4k}{\pi},\quad b_2=0,\quad b_3=\frac{4k}{3\pi},\quad b_4=0,\quad b_5=\frac{4k}{5\pi},\ \dots$$
$$f(x)=\frac{4k}\pi\left(\sin x+\frac13\sin3x+\frac15\sin5x+\cdots\right)$$
:::
:::

```{.figure #m01-square-wave caption="موج مربعی $f(x)$ با دورهٔ تناوب $2\\pi$ و مقادیر $\\pm k$"}
```

مجموع‌های جزئی سری:

$$S_1=\frac{4k}\pi\sin x,\qquad S_2=\frac{4k}\pi\left(\sin x+\frac13\sin3x\right),\qquad S_3=\frac{4k}\pi\left(\sin x+\frac13\sin3x+\frac15\sin5x\right)$$

```{.figure #m01-partial-sums caption="مجموع‌های جزئی $S_1$، $S_2$ و $S_3$ سری فوریهٔ موج مربعی (خط‌چین خود موج مربعی است)"}
```

با قرار دادن $x=\pi/2$:
$$f(\pi/2)=\frac{4k}\pi\left(1-\frac13+\frac15-\frac17+-\cdots\right)=k\quad\Longrightarrow\quad\pi=4\left(1-\frac13+\frac15-\frac17+-\cdots\right)$$

::: {.example}
سری فوریهٔ تابع زیر را به دست آورید:
$$f(x)=x,\qquad -\pi\le x\le\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=0$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}x\cos nx\,dx=\frac1\pi\left[x\left(\frac1n\sin nx\right)-(1)\left(-\frac1{n^2}\cos nx\right)\right]_{-\pi}^{\pi}=\frac1\pi\left[\frac1{n^2}\big(\cos n\pi-\cos(-n\pi)\big)\right]=0$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}x\sin nx\,dx=\frac2\pi\int_0^\pi x\sin nx\,dx=\frac2\pi\left[x\left(\frac{-1}n\cos nx\right)-(1)\left(\frac{-1}{n^2}\sin nx\right)\right]_0^\pi=\frac2\pi\left[\frac{-\pi}n\cos n\pi\right]=\frac2n(-1)^{n+1}$$
$$f(x)=\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin nx=2\left(\sin x-\frac12\sin2x+\frac13\sin3x-+\cdots\right)$$
:::
:::

```{.figure #m01-sawtooth caption="موج دندانه‌اره‌ای $f(x)=x$ روی $[-\\pi,\\pi]$ با ادامهٔ متناوب"}
```

با قرار دادن $x=\pi/2$:
$$f\!\left(\frac\pi2\right)=\frac\pi2=\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin\!\left(n\frac\pi2\right)=2\left(1-\frac13+\frac15-\frac17+-\cdots\right)=\sum_{n=1}^{\infty}\frac2{2n-1}(-1)^{n+1}\ \Longrightarrow\ \pi=\sum_{n=1}^{\infty}\frac4{2n-1}(-1)^{n+1}$$

مقدار سری در نقطهٔ ناپیوستگی $x=\pi$:
$$f(\pi)=\;?\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac2n(-1)^{n+1}\sin(n\pi)=0$$

::: {.important title="نکات مهم"}
1. اگر تابع تناوبی فرد باشد، ضرایب $a$ همگی صفرند.
2. مقدار سری فوریه در نقطهٔ ناپیوستگی تابع برابر است با متوسط حد بالا و پایین در آن نقطه.
:::

::: {.example}
سری فوریهٔ تابع زیر را به دست آورید:
$$f(x)=x^2,\qquad -\pi\le x\le\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}x^2\,dx=\frac{2}{2\pi}\int_0^\pi x^2\,dx=\frac1\pi\left[\frac13x^3\right]_0^\pi=\frac{\pi^2}{3}$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}x^2\cos nx\,dx=\frac2\pi\int_0^\pi x^2\cos nx\,dx=\frac2\pi\left[x^2\left(\frac1n\sin nx\right)-2x\left(\frac{-1}{n^2}\cos nx\right)+2\left(\frac{-1}{n^3}\sin nx\right)\right]_0^\pi=\frac2\pi\left[\frac{2\pi}{n^2}\cos n\pi\right]=\frac4{n^2}(-1)^n$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}x^2\sin nx\,dx=0$$
$$f(x)=\frac{\pi^2}3+\sum_{n=1}^{\infty}\frac4{n^2}(-1)^n\cos nx$$
:::
:::

```{.figure #m01-parabola caption="تابع $f(x)=x^2$ روی $[-\\pi,\\pi]$ با ادامهٔ متناوب"}
```

::: {.important title="نکتهٔ مهم"}
اگر تابع تناوبی زوج باشد، ضرایب $b$ همگی صفرند.
:::

با قرار دادن $x=0$:
$$f(0)=0=\frac{\pi^2}3+\sum_{n=1}^{\infty}\frac4{n^2}(-1)^n\cos(n\cdot0)\quad\Longrightarrow\quad\frac{\pi^2}3=\sum_{n=1}^{\infty}\frac4{n^2}(-1)^{n+1}$$
$$\pi^2=\sum_{n=1}^{\infty}\frac{12}{n^2}(-1)^{n+1}=12\left(1-\frac14+\frac19-\frac1{16}+-\cdots\right)$$

::: {.example}
سری فوریهٔ تابع زیر را به دست آورید:
$$f(x)=x^2,\qquad 0\le x\le2\pi,\qquad f(x+2\pi)=f(x)$$

::: {.solution}
$$a_0=\frac1{2\pi}\int_0^{2\pi}x^2\,dx=\frac1{2\pi}\left[\frac13x^3\right]_0^{2\pi}=\frac1{2\pi}\cdot\frac138\pi^3=\frac{4\pi^2}3$$
$$a_n=\frac1\pi\int_0^{2\pi}x^2\cos nx\,dx=\frac1\pi\left[x^2\left(\frac1n\sin nx\right)-2x\left(\frac{-1}{n^2}\cos nx\right)+2\left(\frac{-1}{n^3}\sin nx\right)\right]_0^{2\pi}=\frac1\pi(2\times2\pi)\left(\frac1{n^2}\cos2\pi n\right)=\frac4{n^2}$$
$$b_n=\frac1\pi\int_0^{2\pi}x^2\sin nx\,dx=\frac1\pi\left[x^2\left(\frac{-1}n\cos nx\right)-2x\left(\frac{-1}{n^2}\sin nx\right)+2\left(\frac1{n^3}\cos nx\right)\right]_0^{2\pi}=\frac1\pi\left[(4\pi^2)\left(\frac{-1}n\right)+2\cdot\frac1{n^3}-2\cdot\frac1{n^3}\right]=-\frac{4\pi}n$$
$$f(x)=\frac{4\pi^2}3+\sum_{n=1}^{\infty}\left(\frac4{n^2}\cos nx-\frac{4\pi}n\sin nx\right)$$
:::
:::

```{.figure #m01-shifted-parabola caption="تابع $f(x)=x^2$ روی $[0,2\\pi]$ با ادامهٔ متناوب"}
```

## سری فوریهٔ توابع متناوب با دورهٔ تناوب دلخواه

$$f(x+T)=f(x)$$
اگر از متغیر کمکی $t=\dfrac{2\pi}{T}x$ استفاده کنیم ($x:0\to T$ و $t:0\to2\pi$):
$$f\!\left(\frac T{2\pi}t\right)=a_0+\sum_{n=1}^{\infty}a_n\cos nt+b_n\sin nt$$
$$a_0=\frac1{2\pi}\int_{2\pi}f\!\left(\frac T{2\pi}t\right)dt,\qquad a_n=\frac1\pi\int_{2\pi}f\!\left(\frac T{2\pi}t\right)\cos nt\,dt,\qquad b_n=\frac1\pi\int_{2\pi}f\!\left(\frac T{2\pi}t\right)\sin nt\,dt$$
با بازگشت به $x=\dfrac T{2\pi}t$:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$a_0=\frac1{2\pi}\int_Tf(x)\frac{2\pi}T\,dx=\frac1T\int_Tf(x)\,dx$$
$$a_n=\frac1\pi\int_Tf(x)\cos\!\left(\frac{2\pi}Tnx\right)\frac{2\pi}T\,dx=\frac2T\int_Tf(x)\cos\!\left(\frac{2\pi}Tnx\right)dx$$
$$b_n=\frac1\pi\int_Tf(x)\sin\!\left(\frac{2\pi}Tnx\right)\frac{2\pi}T\,dx=\frac2T\int_Tf(x)\sin\!\left(\frac{2\pi}Tnx\right)dx$$

::: {.theorem title="سری فوریه (دورهٔ تناوب $T$)"}
اگر تابع $f(x)$ با دورهٔ تناوب $T$ متناوب باشد، آنگاه می‌توان آن را بر حسب یک سری مثلثاتی به صورت زیر بیان کرد:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx,\qquad f(x+T)=f(x)$$
$$a_0=\frac1T\int_Tf(x)\,dx,\qquad a_n=\frac2T\int_Tf(x)\cos\frac{2\pi}Tnx\,dx,\qquad b_n=\frac2T\int_Tf(x)\sin\frac{2\pi}Tnx\,dx$$
:::

::: {.remark}
مقدار سری فوریه در نقاط ناپیوستگی تابع برابر است با متوسط حد بالا و پایین در آن نقطه؛ مقدار سری فوریه در نقطهٔ $x$:
$$\frac{f(x^+)+f(x^-)}{2}$$
:::

## قضیهٔ دریشله

::: {.theorem title="قضیهٔ دریشله (Dirichlet Theorem)"}
اگر تابع $f(x)$ متناوب و **محدود** بوده، دارای تعداد **محدود ماکزیمم و مینیمم** و نیز تعداد **محدود نقاط ناپیوستگی** در هر دورهٔ تناوب باشد، آنگاه این تابع دارای سری فوریه بوده، مقدار سری فوریه در نقاط ناپیوستگی برابر مقدار متوسط حد راست و چپ در این نقاط است.
:::

مثال‌هایی از توابعی که شرایط دریشله را ندارند:

$$f(x)=1/x,\quad 0<x\le1,\qquad f(x+1)=f(x)$$
$$f(x)=\sin(1/x),\quad 0<x\le1,\qquad f(x+1)=f(x)$$

```{.figure #m01-dirichlet caption="توابعی که شرایط دریشله را ندارند: $1/x$ (نامحدود)، $\\sin(1/x)$ (بی‌نهایت ماکزیمم و مینیمم) و تابع پله‌ای با بی‌نهایت پله"}
```

## حل چند مسئله

::: {.example title="مسئلهٔ ۱"}
سری فوریهٔ تابع زیر را به دست آورید:
$$f(x)=\sin\alpha x,\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
از آنجا که این تابع فرد است، داریم $a_0=0$ و $a_n=0$.
$$\begin{aligned}
b_n&=\frac1\pi\int_{-\pi}^{\pi}\sin\alpha x\sin nx\,dx=\frac2\pi\int_0^\pi\sin\alpha x\sin nx\,dx=\frac1\pi\int_0^\pi\big[\cos(\alpha-n)x-\cos(\alpha+n)x\big]dx\\
&=\frac1\pi\left[\frac{\sin(\alpha-n)x}{\alpha-n}-\frac{\sin(\alpha+n)x}{\alpha+n}\right]_0^\pi=\cdots=\frac{2n(-1)^n\sin\alpha\pi}{\pi(\alpha^2-n^2)}
\end{aligned}$$
$$f(x)=\sum_{n=1}^{\infty}\frac{2n(-1)^n\sin\alpha\pi}{\pi(\alpha^2-n^2)}\sin nx$$

سری را وقتی $\alpha=1$ بررسی می‌کنیم:
$$\lim_{\alpha\to1}b_1=\lim_{\alpha\to1}\frac{2(-1)^1\sin\alpha\pi}{\pi(\alpha^2-1^2)}=\lim_{\alpha\to1}\frac{-2(\pi\cos\alpha\pi)}{\pi(2\alpha)}=1,\qquad b_n\Big|_{n\neq1}=0$$
بنابراین سری فوریه همان $f(x)=\sin x$ است.
:::
:::

::: {.exercise}
سری فوریه را وقتی $\alpha=m$، $m\in\mathbb{N}$ بررسی کنید.
:::

::: {.example title="مسئلهٔ ۲"}
سری فوریهٔ تابع زیر را به دست آورید و $\csc\alpha\pi$ را از روی آن بیابید.
$$f(x)=\cos\alpha x,\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
از آنجا که این تابع زوج است، داریم $b_n=0$ و $f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx$.
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}\cos\alpha x\,dx=\frac1\pi\int_0^\pi\cos\alpha x\,dx=\frac1\pi\left[\frac{\sin\alpha x}{\alpha}\right]_0^\pi=\frac1{\alpha\pi}\sin\alpha\pi$$
$$a_n=\frac2\pi\int_0^\pi\cos\alpha x\cos nx\,dx=\frac1\pi\int_0^\pi\big[\cos(\alpha-n)x+\cos(\alpha+n)x\big]dx=\frac1\pi\left[\frac{\sin(\alpha-n)x}{\alpha-n}+\frac{\sin(\alpha+n)x}{\alpha+n}\right]_0^\pi=\cdots=\frac{(-1)^n2\alpha\sin\alpha\pi}{\pi(\alpha^2-n^2)}$$
$$f(x)=\frac1{\alpha\pi}\sin\alpha\pi+\frac{2\alpha\sin\alpha\pi}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}\cos nx$$
تابع تناوبی در $x=0$ پیوسته است، بنابراین داریم:
$$f(0)=1=\frac1{\alpha\pi}\sin\alpha\pi+\frac{2\alpha\sin\alpha\pi}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}\quad\Longrightarrow\quad\frac1{\sin\alpha\pi}=\csc\alpha\pi=\frac1{\alpha\pi}+\frac{2\alpha}\pi\sum_{n=1}^{\infty}\frac{(-1)^n}{(\alpha^2-n^2)}$$
:::
:::

::: {.exercise}
ثابت کنید: اگر $\alpha=m$، $m\in\mathbb{N}$ خواهیم داشت:
$$a_0=0,\qquad a_n=\begin{cases}1&n=m\\ 0&n\neq m\end{cases}$$
:::

::: {.example title="مسئلهٔ ۳"}
سری فوریهٔ تابع زیر را به دست آورید و $\coth\alpha\pi$ را از روی آن بیابید.
$$f(x)=e^{-\alpha x},\qquad \alpha\in\mathbb{R},\qquad x\in[-\pi,\pi),\qquad f(x+2\pi)=f(x)$$

::: {.solution}
**لم ۱:**
$$\int e^{\alpha x}\cos nx\,dx=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\cos nx+n\sin nx\big)$$
اثبات: با انتگرال‌گیری جزء به جزء دو بار، با $I=\int e^{\alpha x}\cos nx\,dx$:
$$I=\frac1\alpha e^{\alpha x}\cos nx-\int\frac1\alpha e^{\alpha x}(-n\sin nx)\,dx=\frac1\alpha e^{\alpha x}\cos nx+\frac n\alpha\int e^{\alpha x}\sin nx\,dx$$
$$=\frac1\alpha e^{\alpha x}\cos nx+\frac n\alpha\left[\frac1\alpha e^{\alpha x}\sin nx-\int\frac1\alpha e^{\alpha x}(n\cos nx)\,dx\right]=\frac1\alpha e^{\alpha x}\cos nx+\frac n{\alpha^2}e^{\alpha x}\sin nx-\frac{n^2}{\alpha^2}I$$
$$\Longrightarrow\quad I=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\cos nx+n\sin nx\big)$$

**لم ۲:**
$$\int e^{\alpha x}\sin nx\,dx=\frac{e^{\alpha x}}{\alpha^2+n^2}\big(\alpha\sin nx-n\cos nx\big)$$
(اثبات به عنوان تمرین.)

تابع نه زوج است و نه فرد؛ لذا باید همهٔ ضرایب سری فوریه را حساب کنیم.
$$a_0=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-\alpha x}\,dx=\frac1{-2\pi\alpha}\Big[e^{-\alpha x}\Big]_{-\pi}^{\pi}=\frac1{2\pi\alpha}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{\sinh\alpha\pi}{\alpha\pi}$$
$$a_n=\frac1\pi\int_{-\pi}^{\pi}e^{-\alpha x}\cos nx\,dx=\left\{\frac{e^{-\alpha x}}{\pi(\alpha^2+n^2)}\big(-\alpha\cos nx+n\sin nx\big)\right\}_{-\pi}^{\pi}=\frac{\alpha(-1)^n}{\pi(\alpha^2+n^2)}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi$$
$$b_n=\frac1\pi\int_{-\pi}^{\pi}e^{-\alpha x}\sin nx\,dx=\left\{\frac{e^{-\alpha x}}{\pi(\alpha^2+n^2)}\big(-\alpha\sin nx-n\cos nx\big)\right\}_{-\pi}^{\pi}=\frac{n(-1)^n}{\pi(\alpha^2+n^2)}\big[e^{\alpha\pi}-e^{-\alpha\pi}\big]=\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi$$
$$\begin{aligned}
f(x)&=\frac{\sinh\alpha\pi}{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi\cos nx+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sinh\alpha\pi\sin nx\right)\\
&=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\cos nx+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sin nx\right)\right)
\end{aligned}$$
از آنجا که نقطهٔ $x=\pi$ نقطهٔ ناپیوستگی است مقدار سری فوریه در این نقطه برابر است با متوسط حد بالا و پایین تابع در این نقطه، به عبارت دیگر:
$$\frac{f(\pi^+)+f(\pi^-)}2=\frac{e^{\alpha\pi}+e^{-\alpha\pi}}2=\cosh\alpha\pi$$
$$\cosh\alpha\pi=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\left(\frac{2\alpha(-1)^n}{\pi(\alpha^2+n^2)}\cos n\pi+\frac{2n(-1)^n}{\pi(\alpha^2+n^2)}\sin n\pi\right)\right)=\sinh\alpha\pi\left(\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\frac{2\alpha}{\pi(\alpha^2+n^2)}\right)$$
$$\coth\alpha\pi=\frac{\cosh\alpha\pi}{\sinh\alpha\pi}=\frac1{\alpha\pi}+\sum_{n=1}^{\infty}\frac{2\alpha}{\pi(\alpha^2+n^2)}$$
:::
:::
