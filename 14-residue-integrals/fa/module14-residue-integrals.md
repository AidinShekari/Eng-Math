# محاسبهٔ انتگرال‌های معین به روش مانده‌ها

::: {.theorem title="قضیهٔ مانده‌ها"}
اگر تابع $f(z)$ در همه‌جای داخل مسیر $C$ به‌جز نقاط $z_1,z_2,\dots,z_n$ تحلیلی باشد و مانده تابع در این نقاط به ترتیب $A_1^1,A_1^2,\dots,A_1^n$ باشد، آنگاه:
$$\oint_Cf(z)\,dz=2\pi i\sum_{k=1}^{n}A_1^k$$
:::

دسته انتگرال‌های مختلفی توسط روش مانده‌ها قابل حل هستند. در اینجا به دو دستهٔ آنها اشاره می‌شود:

::: {.definition title="انتگرال‌های دستهٔ اول"}
در این نوع انتگرال‌ها، مخرج انتگرند به صورت چندجمله‌ای بوده، صورت به فرم تابعی از نوع چندجمله‌ای یا نمائی و یا توابع سینوس یا کسینوس (که آنها هم به صورت نمائی قابل بیان هستند) می‌باشد.
:::

::: {.definition title="انتگرال‌های دستهٔ دوم"}
در این نوع انتگرال‌ها، انتگرند تابعی از سینوس یا کسینوس می‌باشد.
:::

## انتگرال‌های دستهٔ اول

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx$ ($\omega>0$).

::: {.solution}
تابع $f(z)=e^{i\omega z}\big/(1+z^2)^2$ را در نظر می‌گیریم. این تابع در $z=i$ و $z=-i$ تحلیلی نیست. مسیر $C$ نیم‌دایرهٔ بالایی به شعاع $R$ است.
$$\begin{aligned}
\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz&=2\pi i\times\operatorname{Res}\left\{\frac{e^{i\omega z}}{(1+z^2)^2}\right\}\Bigg|_{z=i}\\
&=2\pi i\times\left[\frac d{dz}\left\{(z-i)^2\,\frac{e^{i\omega z}}{(z-i)^2(z+i)^2}\right\}\right]_{z=i}\\
&=2\pi i\times\left[\frac{i\omega e^{i\omega z}(z+i)-2e^{i\omega z}}{(z+i)^3}\right]_{z=i}\\
&=2\pi i\times e^{-\omega}\left(\frac{i\omega(2i)-2}{(2i)^3}\right)\\
&=2\pi i\times e^{-\omega}\,\frac{\omega+1}{4i}=\frac\pi2(\omega+1)e^{-\omega}
\end{aligned}$$
از طرف دیگر
$$\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz=\int_{-R}^{R}\frac{e^{i\omega x}}{(1+x^2)^2}\,dx+\int_0^\pi\frac{e^{i\omega Re^{it}}\,Rie^{it}}{(1+R^2e^{i2t})^2}\,dt$$
و وقتی $R\to\infty$ انتگرال روی نیم‌دایره صفر می‌شود و بخش موهومی انتگرال روی محور حقیقی (تابع فرد $\sin\omega x/(1+x^2)^2$) صفر است:
$$\oint_C\frac{e^{i\omega z}}{(1+z^2)^2}\,dz\ \xrightarrow{\ R\to\infty\ }\ 2\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx$$
$$\int_0^\infty\frac{\cos\omega x}{(1+x^2)^2}\,dx=\frac\pi4(\omega+1)e^{-\omega}$$
:::
:::

```{.figure #m14-semicircle caption="مسیر نیم‌دایرهٔ بالایی؛ قطب مرتبهٔ دوم $z=i$ داخل مسیر و $z=-i$ بیرون آن است"}
```

## انتگرال‌های دستهٔ دوم

$$\int_0^{2\pi}f(a\cos t,\,b\sin t)\,dt$$
برای حل این‌گونه انتگرال‌ها فرض می‌کنیم $z=e^{it}$، در این صورت داریم:
$$dz=ie^{it}\,dt\;\Longrightarrow\;dt=\frac{dz}{ie^{it}}=\frac{dz}{iz}$$
$$\sin t=\frac{e^{it}-e^{-it}}{2i}=\frac{z-z^{-1}}{2i},\qquad \cos t=\frac{e^{it}+e^{-it}}2=\frac{z+z^{-1}}2$$

::: {.important}
$$\int_0^{2\pi}f(a\cos t,\,b\sin t)\,dt=\oint_Cf\!\left(a\,\frac{z+z^{-1}}{2},\;b\,\frac{z-z^{-1}}{2i}\right)\frac{dz}{iz}$$
:::

در اینجا $C$ دایرهٔ واحد است و به سهولت با استفاده از روش مانده‌ها انتگرال حل می‌شود.

```{.figure #m14-unit-circle caption="دایرهٔ واحد $z=e^{it}$، $0\\le t\\le2\\pi$"}
```

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle\int_0^{2\pi}\frac1{2+\cos x}\,dx$.

::: {.solution}
$$z=e^{ix},\qquad dz=ie^{ix}dx,\qquad dx=\frac{dz}{iz},\qquad \cos x=\frac{z+z^{-1}}2=\frac{z^2+1}{2z}$$
$$2+\cos x=2+\frac{z^2+1}{2z}=\frac{z^2+4z+1}{2z}$$
$$\int_0^{2\pi}\frac1{2+\cos x}\,dx=\oint_C\frac{2z}{z^2+4z+1}\,\frac{dz}{iz}=\frac2i\oint_C\frac1{z^2+4z+1}\,dz=\frac2i\times2\pi i\times\sum_k\operatorname{Res}\left\{\frac1{z^2+4z+1}\right\}\Bigg|_{z=z_k}$$
$$z^2+4z+1=0\;\Longrightarrow\;z_1=-2+\sqrt3\approx-0.27,\qquad z_2=-2-\sqrt3\approx-3.73$$
فقط $z_1$ داخل دایرهٔ واحد قرار دارد.
$$\int_0^{2\pi}\frac1{2+\cos x}\,dx=4\pi\times\operatorname{Res}\left\{\frac1{z^2+4z+1}\right\}\Bigg|_{z=z_1}=4\pi\left[\big(z+2-\sqrt3\big)\frac1{\big(z+2-\sqrt3\big)\big(z+2+\sqrt3\big)}\right]_{z_1=-2+\sqrt3}=\frac{2\pi}{\sqrt3}$$
:::
:::

```{.figure #m14-poles-cos caption="دایرهٔ واحد و قطب‌های $z_1\\approx-0.27$ (داخل) و $z_2\\approx-3.73$ (بیرون)"}
```

::: {.exercise title="کاربرد قضیهٔ مانده‌ها در حل انتگرال"}
با استفاده از قضیهٔ مانده‌ها مقدار انتگرال‌های معین زیر را به دست آورید:
$$I_1=\int_0^{2\pi}\frac{dt}{1-2p\cos t+p^2},\qquad I_2=\int_{-\infty}^{\infty}\frac{\sin2x}{x^2+x+1}\,dx$$
$$I_3=\int_{-\infty}^{\infty}\frac{x}{(x^2-2x+2)^2}\,dx,\qquad I_4=\int_{-\infty}^{\infty}\frac{\cos^4x}{(x^2+1)(x^2+4)}\,dx$$
:::
