# خواص سری فوریه، قضیهٔ پارسوال و صورت مختلط

## تقریب یک تابع متناوب توسط یک سری مثلثاتی با تعداد جملات محدود

::: {.theorem}
برای تقریب $N$ جمله‌ای یک تابع متناوب $f(x)$ توسط یک سری سینوسی و کسینوسی، بهترین ضرایب (با معیار MMSE) ضرایب سری فوریه می‌باشند.
:::

تابع متناوب با دورهٔ تناوب $2\pi$ را در نظر بگیرید:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+b_n\sin nx,\qquad f(x)=f(x+2\pi)$$
تقریب $N$ جمله‌ای مثلثاتی:
$$f(x)\approx a_0+\sum_{n=1}^{N}a_n\cos nx+b_n\sin nx$$
آیا تقریب مثلثاتی مقابل **بهتر** نیست؟
$$F(x)\triangleq\alpha_0+\sum_{n=1}^{N}\alpha_n\cos nx+\beta_n\sin nx$$
**معیار** بهتر بودن تقریب چیست؟ یک معیار: تابع خطا:
$$E(x)=\big|f(x)-F(x)\big|=\left|f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right|$$
یک معیار خوب: متوسط مجذور خطا:
$$D\triangleq\int_{-\pi}^{\pi}E^2(x)\,dx=\int_{-\pi}^{\pi}\left|f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right|^2dx$$

::: {.proof}
برای بهترین تقریب متوسط مجذور خطا را کمینه می‌کنیم. این کار با مشتق‌گیری از $D$ بر حسب ضرایب سری مثلثاتی و برابر قرار دادن این مشتق با صفر به دست می‌آید. به عبارت دیگر:
$$\frac{\partial D}{\partial\alpha_0}=-2\int_{-\pi}^{\pi}\left[f(x)-\alpha_0-\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right]dx=0$$
$$\int_{-\pi}^{\pi}f(x)\,dx=\int_{-\pi}^{\pi}\left[\alpha_0+\sum_{n=1}^{N}\big(\alpha_n\cos nx+\beta_n\sin nx\big)\right]dx=2\pi\alpha_0\quad\Longrightarrow\quad\alpha_0=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=a_0$$
$$\frac{\partial D}{\partial\alpha_m}=0\quad\Longrightarrow\quad\alpha_m=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos mx\,dx=a_m$$
$$\frac{\partial D}{\partial\beta_m}=0\quad\Longrightarrow\quad\beta_m=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin mx\,dx=b_m$$
بهترین تقریب مثلثاتی با تعداد جملات محدود از یک تابع تناوبی سری فوریه با جملات محدود است.
:::

## مشتق و انتگرال سری فوریه

::: {.theorem title="مشتق سری فوریه"}
اگر تابع $f(x)$ با دورهٔ تناوب $T$ تناوبی بوده، پیوسته و دارای سری فوریه باشد، آنگاه مشتق این تابع نیز تناوبی بوده سری فوریه آن با استفاده از مشتق‌گیری از سری فوریه تابع به دست می‌آید.
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$\Longrightarrow\quad f'(x)=\sum_{n=1}^{\infty}\left(\frac{2\pi}Tnb_n\right)\cos\frac{2\pi}Tnx+\left(-\frac{2\pi}Tna_n\right)\sin\frac{2\pi}Tnx$$
:::

::: {.theorem title="انتگرال سری فوریه"}
اگر تابع $f(x)$ با دورهٔ تناوب $T$ تناوبی بوده و دارای سری فوریه باشد، آنگاه انتگرال معین این تابع با استفاده از انتگرال‌گیری از سری فوریه تابع قابل محاسبه است.
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$\Longrightarrow\quad\int_0^xf(t)\,dt=a_0x+\sum_{n=1}^{\infty}\left(\frac T{2\pi n}a_n\sin\frac{2\pi}Tnx-\frac T{2\pi n}b_n\cos\frac{2\pi}Tnx+\frac T{2\pi n}b_n\right)$$
:::

## قضیهٔ رایلی

::: {.theorem title="قضیهٔ رایلی (Rayleigh's Theorem)"}
اگر دو تابع $f(x)$ و $g(x)$ با دورهٔ تناوب $T$ تناوبی بوده و سری فوریه این دو تابع به صورت زیر وجود داشته باشند:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
$$g(x)=\alpha_0+\sum_{n=1}^{\infty}\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx$$
آنگاه خواهیم داشت:
$$\frac2T\int_Tf(x)\,\overline{g(x)}\,dx=2a_0\overline{\alpha_0}+\sum_{n=1}^{\infty}a_n\overline{\alpha_n}+b_n\overline{\beta_n}$$
:::

::: {.proof}
اثبات با فرض حقیقی بودن $g(x)$:
$$\begin{aligned}
\frac2T\int_Tf(x)g(x)\,dx&=\frac2T\int_Tf(x)\left(\alpha_0+\sum_{n=1}^{\infty}\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx\right)dx\\
&=\frac2T\int_Tf(x)\alpha_0\,dx+\sum_{n=1}^{\infty}\frac2T\int_Tf(x)\left(\alpha_n\cos\frac{2\pi}Tnx+\beta_n\sin\frac{2\pi}Tnx\right)dx\\
&=\underbrace{\frac2T\int_Tf(x)\,dx}_{2a_0}\,\alpha_0+\sum_{n=1}^{\infty}\underbrace{\frac2T\int_Tf(x)\cos\frac{2\pi}Tnx\,dx}_{a_n}\,\alpha_n+\underbrace{\frac2T\int_Tf(x)\sin\frac{2\pi}Tnx\,dx}_{b_n}\,\beta_n\\
&=2a_0\alpha_0+\sum_{n=1}^{\infty}a_n\alpha_n+b_n\beta_n
\end{aligned}$$
:::

## قضیهٔ پارسوال

::: {.theorem title="قضیهٔ پارسوال (Parseval's Theorem)"}
اگر تابع $f(x)$ با دورهٔ تناوب $T$ تناوبی بوده و سری فوریه آن به صورت زیر وجود داشته باشد:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{2\pi}Tnx+b_n\sin\frac{2\pi}Tnx$$
آنگاه خواهیم داشت:
$$\frac2T\int_T|f(x)|^2\,dx=2|a_0|^2+\sum_{n=1}^{\infty}\big(|a_n|^2+|b_n|^2\big)$$
:::

::: {.proof}
در تساوی رایلی اگر به جای $g(x)$ تابع $f(x)$ را قرار دهیم به تساوی پارسوال می‌رسیم.
:::

با توجه به تساوی پارسوال مقدار توان تابع $f(x)$ را می‌شود با استفاده از ضرایب سری فوریه به دست آورد. اگر تابع توسط تقریب $N$ جمله‌ای از سینوس‌ها و کسینوس‌ها بیان شود طبق رابطهٔ بالا توان تابع تقریبی کمتر از توان تابع $f(x)$ خواهد بود و داریم:

::: {.important title="نامساوی بسل"}
$$\frac2T\int_T|f(x)|^2\,dx\ \ge\ 2|a_0|^2+\sum_{n=1}^{N}\big(|a_n|^2+|b_n|^2\big)$$
:::

::: {.example}
برای تابع $f(x)$ زیر، چند جمله از سری فوریه نیاز است تا حداقل ۹۴ درصد توان در تابع تقریبی باقی بماند.

::: {.solution}
$$f(x)=\sum_{n=1}^{\infty}\frac{2k}{n\pi}(1-\cos n\pi)\sin nx$$
$$\frac2T\int_T|f(x)|^2\,dx=\frac1\pi\int_{-\pi}^{\pi}k^2\,dx=\frac2\pi\big[k^2x\big]_0^\pi=2k^2$$
$$\frac{\displaystyle\sum_{n=1}^{N}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\ge0.94$$
$$\frac{\displaystyle\sum_{n=1}^{7}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\cong0.9496,\qquad \frac{\displaystyle\sum_{n=1}^{5}\left(\frac{2k}{n\pi}(1-\cos n\pi)\right)^2}{2k^2}\cong0.9331\quad\Longrightarrow\quad N=7$$
:::
:::

```{.figure #m02-power-example caption="موج مربعی $\\pm k$ با دورهٔ تناوب $2\\pi$ در مثال توان"}
```

## صورت مختلط سری فوریه

فرض کنید تابع $f(x)$ تناوبی و صرفاً جهت سادگی دارای دورهٔ تناوب $2\pi$ می‌باشد. لذا داریم:
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+b_n\sin nx$$
با استفاده از رابطهٔ اویلر $e^{ix}=\cos x+i\sin x$:
$$\cos nx=\frac{e^{inx}+e^{-inx}}2,\qquad \sin nx=\frac{e^{inx}-e^{-inx}}{2i},\qquad \frac1i=-i$$
$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\left(\frac{e^{inx}+e^{-inx}}2\right)+b_n\left(\frac{e^{inx}-e^{-inx}}{2i}\right)=\underbrace{a_0}_{c_0}+\sum_{n=1}^{\infty}\underbrace{\left(\frac{a_n-ib_n}2\right)}_{c_n}e^{inx}+\underbrace{\left(\frac{a_n+ib_n}2\right)}_{c_{-n}}e^{-inx}$$
$$c_n=\frac{a_n-ib_n}2=\frac12\left\{\frac1\pi\int_{2\pi}f(x)\cos nx\,dx-i\frac1\pi\int_{2\pi}f(x)\sin nx\,dx\right\}=\frac1{2\pi}\int_{2\pi}f(x)\big(\cos nx-i\sin nx\big)\,dx=\frac1{2\pi}\int_{2\pi}f(x)e^{-inx}\,dx$$
$$c_{-n}=\frac{a_n+ib_n}2=\frac1{2\pi}\int_{2\pi}f(x)\big(\cos nx+i\sin nx\big)\,dx=\frac1{2\pi}\int_{2\pi}f(x)e^{inx}\,dx$$

::: {.important title="صورت مختلط سری فوریه"}
$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{inx},\qquad c_n=\frac1{2\pi}\int_{2\pi}f(x)e^{-inx}\,dx$$
برای دورهٔ تناوب دلخواه:
$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{i\frac{2\pi}Tnx},\qquad c_n=\frac1T\int_Tf(x)e^{-i\frac{2\pi}Tnx}\,dx$$
$$\frac1T\int_T|f(x)|^2\,dx=\sum_{n=-\infty}^{\infty}|c_n|^2$$
:::
