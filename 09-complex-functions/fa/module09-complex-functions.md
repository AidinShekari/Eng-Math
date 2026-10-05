# توابع مختلط، مشتق و شرایط کشی–ریمان

## توابع مختلط

```{.figure #m09-mapping caption="تابع مختلط $w=f(z)$ نقاط دامنه در صفحهٔ $z$ را به نقاط برد در صفحهٔ $w$ می‌نگارد"}
```

$$z=x+iy,\qquad w=u+iv$$
$$f:\mathbb{C}\to\mathbb{C},\qquad f:\begin{cases}u=u(x,y)\\ v=v(x,y)\end{cases}$$

::: {.example}
تابع $w=z^2$ را در نظر بگیرید:
$$u+iv=(x+iy)^2=(x^2-y^2)+i(2xy)\quad\Longrightarrow\quad\begin{cases}u=x^2-y^2\\ v=2xy\end{cases}$$
:::

## چند مکان هندسی مهم

```{.figure #m09-loci caption="مکان‌های هندسی مهم: دایره، $\\rho$-همسایگی نقطهٔ $a$ و ناحیهٔ حلقوی"}
```

$$|z|=1,\qquad |z-a|=\rho,\qquad |z-a|<\rho,\qquad \rho_1<|z-a|<\rho_2$$

مجموعهٔ $|z-a|<\rho$ را $\rho$-همسایگی $a$ می‌نامند.

## حد توابع مختلط

::: {.definition title="حد"}
اگر به ازاء هر $\varepsilon>0$ بتوان $\delta>0$ به‌دست آورد، به طوری که از نامساوی $|z-z_0|<\delta$ نتیجه شود $|f(z)-l|<\varepsilon$، آنگاه
$$\lim_{z\to z_0}f(z)=l$$
بنابراین به ازاء کلیهٔ نقاط داخل دایره‌ای به مرکز $z_0$ و به شعاع $\delta$ لازم است که $f(z)$ داخل دایره‌ای به مرکز $l$ و به شعاع $\varepsilon$ باشد. در اینجا $\varepsilon$ داده می‌شود و $\delta(\varepsilon)$ را بایستی به‌دست آورد. واضح است مفهوم حد در اینجا گسترده‌تر از حد در توابع حقیقی است.
:::

```{.figure #m09-limit caption="تعریف حد: دایرهٔ $\\delta$-همسایگی $z_0$ در صفحهٔ $z$ و دایرهٔ $\\varepsilon$-همسایگی $l$ در صفحهٔ $w$"}
```

## پیوستگی توابع مختلط

::: {.definition title="پیوستگی در یک نقطه"}
تابع $w=f(z)$ در نقطهٔ $z=z_0$ پیوسته است هرگاه سه شرط زیر برقرار باشد:

1. $f(z)$ در نقطهٔ $z=z_0$ معین باشد.
2. $\displaystyle\lim_{z\to z_0}f(z)$ وجود داشته باشد.
3. $\displaystyle\lim_{z\to z_0}f(z)=f(z_0)$ باشد.
:::

::: {.example}
آیا تابع $f(z)=\sin\frac1z$ در نقطهٔ $z=0$ پیوسته است؟
:::

::: {.example}
آیا تابع
$$f(z)=\begin{cases}\sin\frac1z&z\neq0\\ 5+4i&z=0\end{cases}$$
در نقطهٔ $z=0$ پیوسته است؟
:::

::: {.example}
آیا تابع
$$f(z)=\begin{cases}3z^3+4&z\neq0\\ 17&z=0\end{cases}$$
در نقطهٔ $z=0$ پیوسته است؟
:::

### خواص توابع مختلط پیوسته

::: {.theorem title="قضایا"}
1. اگر توابع $f(z),g(z)$ در نقطهٔ $z_0$ پیوسته باشند، آنگاه $f(z)\pm g(z)$ در $z_0$ پیوسته است.
2. اگر توابع $f(z),g(z)$ در نقطهٔ $z_0$ پیوسته باشند، آنگاه $f(z)\times g(z)$ در $z_0$ پیوسته است.
3. اگر توابع $f(z),g(z)$ در نقطهٔ $z_0$ پیوسته باشند و $g(z_0)\neq0$ آنگاه $\dfrac{f(z)}{g(z)}$ در $z_0$ پیوسته است.
:::

::: {.definition title="پیوستگی در یک میدان"}
تابع $w=f(z)$ در میدان $D$ پیوسته است هرگاه تابع $f$ در تمام نقاط میدان $D$ پیوسته باشد.

میدان: تمام نقاط داخل یک منحنی بسته.
:::

```{.figure #m09-domain caption="میدان $D$ در صفحهٔ مختلط"}
```

## مشتق توابع مختلط

::: {.definition title="مشتق"}
تابع $w=f(z)$ در نقطهٔ $z=z_0$ مشتق‌پذیر است هرگاه حد زیر موجود باشد:
$$f'(z_0)=\lim_{|\Delta z|\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}$$
:::

::: {.remark}
وجود مشتق در توابع مختلط نیازمند شرایط سخت‌تری نسبت به توابع حقیقی است، زیرا اگر در صفحهٔ $z$ از *تمام* جهات به نقطهٔ $z_0$ نزدیک شویم، بایستی این حد موجود بوده به مسیر انتخابی بستگی به سمت $z_0$ بستگی نداشته باشد.
:::

```{.figure #m09-approach caption="نزدیک شدن به نقطهٔ $z_0$ از تمام جهات"}
```

## شرایط کشی–ریمان

::: {.theorem title="شرط لازم مشتق‌پذیری"}
شرط لازم برای آنکه تابع مختلط $w=f(z)$ مشتق‌پذیر باشد آن‌است که شرایط کشی–ریمان (شرایط مقابل) برقرار باشند:
$$\begin{cases}\dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}\\[2mm] \dfrac{\partial u}{\partial y}=-\dfrac{\partial v}{\partial x}\end{cases}\qquad w=u+iv=f(x+iy)=f(z)$$
:::

::: {.proof}
$$f'(z)=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z},\qquad z=x+iy,\qquad \Delta z=\Delta x+i\Delta y$$
$$\begin{aligned}
f(z+\Delta z)-f(z)&=\big[u(x+\Delta x,y+\Delta y)+iv(x+\Delta x,y+\Delta y)\big]-\big[u(x,y)+iv(x,y)\big]\\
&=\big[u(x+\Delta x,y+\Delta y)-u(x,y)\big]+i\big[v(x+\Delta x,y+\Delta y)-v(x,y)\big]
\end{aligned}$$
$$\frac{f(z+\Delta z)-f(z)}{\Delta z}=\frac{u(x+\Delta x,y+\Delta y)-u(x,y)}{\Delta x+i\Delta y}+i\,\frac{v(x+\Delta x,y+\Delta y)-v(x,y)}{\Delta x+i\Delta y}$$
شرط لازم برای وجود مشتق $w=f(z)$ آن است که اگر از هر جهت به نقطهٔ $z$ نزدیک شویم (از جمله در راستای افقی یا عمودی) مقدار حد مربوط به $f'(z)$ تغییر نکند.

**مسیر ۱: راستای قائم.** $\Delta z=\Delta x+i\Delta y$ و $\Delta x=0$، یعنی $\Delta z=i\Delta y$:
$$\begin{aligned}
f'(z)&=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}\\
&=\lim_{\Delta y\to0}\left[\frac{u(x,y+\Delta y)-u(x,y)}{i\Delta y}+i\,\frac{v(x,y+\Delta y)-v(x,y)}{i\Delta y}\right]\\
&=\frac1i\,\frac{\partial u}{\partial y}+\frac{\partial v}{\partial y}=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}
\end{aligned}$$

**مسیر ۲: راستای افقی.** $\Delta z=\Delta x+i\Delta y$ و $\Delta y=0$، یعنی $\Delta z=\Delta x$:
$$\begin{aligned}
f'(z)&=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}\\
&=\lim_{\Delta x\to0}\left[\frac{u(x+\Delta x,y)-u(x,y)}{\Delta x}+i\,\frac{v(x+\Delta x,y)-v(x,y)}{\Delta x}\right]\\
&=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}
\end{aligned}$$

بنابراین
$$f'(z)=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}$$
و با مساوی قرار دادن بخش‌های حقیقی و موهومی:
:::

```{.figure #m09-cr-paths caption="دو مسیر نزدیک شدن به $z$: راستای قائم ($\\Delta z=i\\Delta y$) و راستای افقی ($\\Delta z=\\Delta x$)"}
```

::: {.important title="شرایط کشی–ریمان"}
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$
:::

::: {.remark title="نتیجه"}
1. اگر این شرایط برقرار نباشد مشتق در نقطهٔ $z$ وجود ندارد.
2. روش‌های زیر جهت مشتق‌گیری پیشنهاد می‌شود:
$$f'(z)=\lim_{|\Delta z|\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\frac{\partial v}{\partial y}-i\,\frac{\partial u}{\partial y}=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\frac{\partial u}{\partial x}-i\,\frac{\partial u}{\partial y}=\frac{\partial v}{\partial y}+i\,\frac{\partial v}{\partial x}$$
:::

::: {.theorem title="شرط کافی مشتق‌پذیری"}
شرط کافی برای آنکه تابع مختلط $w=f(z)$ مشتق‌پذیر باشد آن‌است که شرایط کشی–ریمان برقرار باشند.

اثبات خارج از حوصلهٔ کلاس است.
:::

::: {.theorem title="قضیهٔ کشی–ریمان"}
شرط لازم و کافی برای آنکه تابع مختلط $w=f(z)$ مشتق‌پذیر باشد آن‌است که شرایط کشی–ریمان (شرایط مقابل) برقرار باشند.
$$\begin{cases}\dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}\\[2mm] \dfrac{\partial u}{\partial y}=-\dfrac{\partial v}{\partial x}\end{cases}\qquad w=u+iv=f(x+iy)=f(z)$$
:::

### نتیجهٔ برقراری شرایط کشی–ریمان (تحلیلی بودن یک تابع)

از شرایط کشی–ریمان نسبت به $x$ و $y$ مشتق می‌گیریم:

$$\left.\begin{aligned}\frac{\partial^2u}{\partial x^2}&=\frac{\partial^2v}{\partial x\partial y}\\[1mm] \frac{\partial^2u}{\partial y^2}&=-\frac{\partial^2v}{\partial x\partial y}\end{aligned}\right\}\ \xrightarrow{\ \text{جمع}\ }\ \frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0$$

$$\left.\begin{aligned}\frac{\partial^2u}{\partial x\partial y}&=\frac{\partial^2v}{\partial y^2}\\[1mm] \frac{\partial^2u}{\partial x\partial y}&=-\frac{\partial^2v}{\partial x^2}\end{aligned}\right\}\ \xrightarrow{\ \text{تفریق}\ }\ \frac{\partial^2v}{\partial x^2}+\frac{\partial^2v}{\partial y^2}=0$$

::: {.remark title="نتیجه"}
قسمت حقیقی و موهومی یک تابع تحلیلی در معادلهٔ لاپلاس دوبعدی صدق می‌کند.
:::

## مشتق‌پذیری توابع مختلط: مثال‌ها

::: {.example}
تابع $w=z^2$ را در نظر بگیرید؛ آیا این تابع تحلیلی است؟

::: {.solution}
$$w=f(z)=z^2=(x+iy)^2=(x^2-y^2)+i\,2xy,\qquad u(x,y)=x^2-y^2,\qquad v(x,y)=2xy$$
$$\frac{\partial u}{\partial x}=2x=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=-2y=-\frac{\partial v}{\partial x}\ \checkmark$$
$$f'(z)=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=2x+i\,2y=2(x+iy)=2z$$
$$\nabla^2u=2-2=0,\qquad \nabla^2v=0+0=0$$
:::
:::

::: {.example}
تابع $w=|z|^2$ را در نظر بگیرید؛ آیا این تابع تحلیلی است؟

::: {.solution}
$$w=f(z)=|z|^2=(x+iy)(x-iy)=x^2+y^2,\qquad u(x,y)=x^2+y^2,\qquad v(x,y)=0$$
$$\frac{\partial u}{\partial x}=2x,\quad \frac{\partial v}{\partial y}=0,\qquad \frac{\partial u}{\partial y}=2y,\quad -\frac{\partial v}{\partial x}=0$$
$$\nabla^2u=2+2=4,\qquad \nabla^2v=0+0=0$$
تحلیلی در هیچ‌جا به جز مبدأ.
:::
:::

::: {.exercise}
بررسی کنید آیا هر کدام از توابع زیر تحلیلی‌اند. در صورت تحلیلی بودن مشتق آن توابع را به دست آورید.

1. $f(z)=\bar z$
2. $f(z)=\operatorname{Re}\{z\}$
3. $f(z)=z^3+2z^2+3i$
:::

## توابع مختلط تحلیلی

::: {.example}
$u=x^2-y^2$ قسمت حقیقی یک تابع تحلیلی $f(z)$ است. مطلوب است محاسبهٔ $f(z)$.

::: {.solution}
از آنجائی که $f(z)$ تحلیلی است، قسمت‌های حقیقی و موهومی تابع در شرایط کوشی–ریمان صدق می‌کنند و در نتیجه این قسمت‌ها در معادلهٔ لاپلاس دو بعدی نیز باید صدق کنند.

۱) اول چک کنیم که آیا قسمت حقیقی تابع در معادلهٔ لاپلاس ۲ بعدی صدق می‌کند؟
$$\nabla^2u=\frac{\partial^2}{\partial x^2}(x^2-y^2)+\frac{\partial^2}{\partial y^2}(x^2-y^2)=2-2=0\ \checkmark$$

۲) از روابط کشی–ریمان استفاده می‌کنیم:
$$\frac{\partial u}{\partial x}=2x=\frac{\partial v}{\partial y}\quad\Longrightarrow\quad v(x,y)=2xy+\varphi(x)$$
$$-\frac{\partial v}{\partial x}=-2y-\varphi'(x)=\frac{\partial u}{\partial y}=-2y\quad\Longrightarrow\quad\varphi'(x)=0\quad\Longrightarrow\quad\varphi(x)=c,\ \ c\in\mathbb{R}$$
$$f(z)=(x^2-y^2)+i(2xy+c)=z^2+C$$
:::
:::

::: {.example}
اگر $u=\cos x\cosh y$،
الف) نشان دهید این تابع در صفحه هارمونیک است ($\nabla^2u=0$).
ب) تابع $v(x,y)$ را چنان بیابید که $u+iv$ تحلیلی شود.

::: {.solution}
الف) چک کنیم که آیا قسمت حقیقی تابع در معادلهٔ لاپلاس ۲ بعدی صدق می‌کند؟
$$\nabla^2u=\frac{\partial^2}{\partial x^2}(\cos x\cosh y)+\frac{\partial^2}{\partial y^2}(\cos x\cosh y)=-\cos x\cosh y+\cos x\cosh y=0\ \checkmark$$

ب) از روابط کشی–ریمان استفاده می‌کنیم:
$$\frac{\partial u}{\partial x}=-\sin x\cosh y=\frac{\partial v}{\partial y}\quad\Longrightarrow\quad v(x,y)=-\sin x\sinh y+\varphi(x)$$
$$-\frac{\partial v}{\partial x}=\cos x\sinh y-\varphi'(x)=\frac{\partial u}{\partial y}=\cos x\sinh y\quad\Longrightarrow\quad\varphi'(x)=0$$
$$\varphi(x)=c,\ \ c\in\mathbb{R}\quad\Longrightarrow\quad v(x,y)=-\sin x\sinh y+c$$
:::
:::

## شرایط کشی–ریمان در مختصات قطبی

$$\begin{cases}x=r\cos\theta\\ y=r\sin\theta\end{cases}\qquad\begin{cases}r=\sqrt{x^2+y^2}\\ \theta=\tan^{-1}\dfrac{y}{x}\end{cases}\qquad r_x=\frac{x}{r},\quad\theta_x=\frac{-y}{r^2},\quad r_y=\frac{y}{r},\quad\theta_y=\frac{x}{r^2}$$

$$\frac{\partial u}{\partial x}=\frac{\partial u}{\partial r}\frac{\partial r}{\partial x}+\frac{\partial u}{\partial\theta}\frac{\partial\theta}{\partial x}=\frac xr\frac{\partial u}{\partial r}-\frac{y}{r^2}\frac{\partial u}{\partial\theta}=\cos\theta\frac{\partial u}{\partial r}-\frac1r\sin\theta\frac{\partial u}{\partial\theta}$$

$$\frac{\partial v}{\partial y}=\frac{\partial v}{\partial r}\frac{\partial r}{\partial y}+\frac{\partial v}{\partial\theta}\frac{\partial\theta}{\partial y}=\frac yr\frac{\partial v}{\partial r}+\frac{x}{r^2}\frac{\partial v}{\partial\theta}=\sin\theta\frac{\partial v}{\partial r}+\frac1r\cos\theta\frac{\partial v}{\partial\theta}$$

$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}\;\Longrightarrow\;\cos\theta\frac{\partial u}{\partial r}-\frac1r\sin\theta\frac{\partial u}{\partial\theta}=\sin\theta\frac{\partial v}{\partial r}+\frac1r\cos\theta\frac{\partial v}{\partial\theta}$$

مشابهاً

$$\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}\;\Longrightarrow\;\sin\theta\frac{\partial u}{\partial r}+\frac1r\cos\theta\frac{\partial u}{\partial\theta}=-\cos\theta\frac{\partial v}{\partial r}+\frac1r\sin\theta\frac{\partial v}{\partial\theta}$$

::: {.important title="شرایط کشی–ریمان در فرم قطبی"}
$$\frac{\partial u}{\partial r}=\frac1r\frac{\partial v}{\partial\theta},\qquad -\frac1r\frac{\partial u}{\partial\theta}=\frac{\partial v}{\partial r}$$
:::

::: {.exercise}
با استفاده از شرایط کشی–ریمان در فرم قطبی ثابت کنید که $u$ و $v$ در معادلهٔ لاپلاس در فرم قطبی صدق می‌کنند، یعنی:
$$\nabla^2u=u_{rr}+\frac1{r^2}u_{\theta\theta}+\frac1ru_r=0,\qquad \nabla^2v=v_{rr}+\frac1{r^2}v_{\theta\theta}+\frac1rv_r=0$$
:::
