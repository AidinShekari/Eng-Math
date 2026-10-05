# انتگرال توابع مختلط

## انتگرال معین و مسیر انتگرال‌گیری

انتگرال توابع مختلط همچون توابع حقیقی به دو صورت مطرح می‌شود:

- انتگرال نامعین، که مثل محاسبهٔ تابع اولیه است؛
- انتگرال معین، که به عنوان انتگرال روی مسیر شناخته می‌شود.

انتگرال معین را در حوزهٔ توابع مختلط انتگرال روی مسیر یا Line Integral نیز می‌نامیم و با نماد زیر نشان می‌دهیم:
$$\int_C f(z)\,dz$$
به $C$ مسیر انتگرال‌گیری گوئیم.

```{.figure #m12-path caption="مسیر انتگرال‌گیری $C$ از نقطهٔ $A$ تا نقطهٔ $B$ در صفحهٔ $z$"}
```

### مسیر انتگرال‌گیری

مسیر انتگرال‌گیری در صفحهٔ مختلط از نقطهٔ شروع، مسیر میانی، و نقطهٔ پایانی تشکیل می‌شود. در بسیاری موارد بهترین نحوهٔ بیان مسیر، استفاده از یک متغیر کمکی است که با تغییرات صعودی خود مسیر از ابتدا تا پایان در جهت مطلوب طی می‌شود.

$$z(t)=x(t)+iy(t),\qquad a\le t\le b,\qquad t,a,b\in\mathbb{R}$$
$$z(a)=A,\qquad z(b)=B,\qquad z,A,B\in\mathbb{C}$$

```{.figure #m12-path-param caption="مسیر $C$ با جهت از $A=z(a)$ به $B=z(b)$"}
```

::: {.example}
$$z(t)=t+i2t,\qquad 1\le t\le2$$
این مسیر پاره‌خطی است از نقطهٔ $1+2i$ تا نقطهٔ $2+4i$.
:::

```{.figure #m12-line-path caption="مسیر $z(t)=t+i2t$، $1\\le t\\le2$"}
```

::: {.example}
$$z(t)=\cos t+i\sin t,\qquad 0\le t\le2\pi$$
$$z(t)=e^{it},\qquad 0\le t\le2\pi$$
این مسیر دایرهٔ واحد است که در جهت مثلثاتی پیموده می‌شود.
:::

```{.figure #m12-circle-path caption="مسیر $z(t)=e^{it}$، $0\\le t\\le2\\pi$ (دایرهٔ واحد)"}
```

### مشتق مسیر انتگرال‌گیری

$$\dot z(t)=\frac{d}{dt}z(t)=\lim_{\Delta t\to0}\frac{z(t+\Delta t)-z(t)}{\Delta t}=\frac{d}{dt}x(t)+i\frac{d}{dt}y(t)=\dot x(t)+i\dot y(t)$$

```{.figure #m12-tangent caption="مشتق مسیر $\\dot z(t)$ به عنوان حد $\\frac{z(t+\\Delta t)-z(t)}{\\Delta t}$"}
```

## انتگرال معین توابع مختلط

$$\int_Cf(z)\,dz=\int_C(u+iv)(dx+i\,dy)=\int_C(u\,dx-v\,dy)+i\int_C(v\,dx+u\,dy)$$
$$\int_Cf(z)\,dz=\int_tf\big(z(t)\big)\,\dot z(t)\,dt$$

::: {.definition title="مراحل محاسبهٔ انتگرال معین مختلط روی مسیر"}
1. بیان مسیر به صورت پارامتریک: $z(t)=x(t)+iy(t)$، $a\le t\le b$.
2. محاسبهٔ مشتق $z(t)$ نسبت به $t$: $\dot z(t)=\dot x(t)+i\,\dot y(t)$.
3. جایگذاری $z(t)$ در $f(z)$.
4. انتگرال‌گیری از $f\big(z(t)\big)\dot z(t)$ نسبت به $t$ برای $a\le t\le b$.
:::

::: {.example}
مطلوب است انتگرال روی مسیر شکل زیر از تابع $f(z)=\bar z$.

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

```{.figure #m12-parabola-path caption="مسیر $z(t)=t+it^2$، $-1\\le t\\le1$ از $-1+i$ تا $1+i$"}
```

::: {.example}
مطلوب است انتگرال روی مسیر شکل زیر از تابع $f(z)=\bar z$.

::: {.solution}
$$z(t)=t+i,\quad -1\le t\le1,\qquad \dot z(t)=1$$
$$f(z)=\bar z=x-iy,\qquad f\big(z(t)\big)=\bar z(t)=t-i$$
$$\int_{-1+i}^{1+i}\bar z\,dz=\int_{t=-1}^{1}(t-i)(1)\,dt=\left.\left(\frac{t^2}{2}-it\right)\right|_{-1}^{1}=0-i2$$
بنابراین برای این تابع مختلط مقدار انتگرال به مسیر انتخابی بستگی دارد.
:::
:::

```{.figure #m12-line-path-2 caption="مسیر $z(t)=t+i$، $-1\\le t\\le1$ از $-1+i$ تا $1+i$"}
```

### بعضی خواص انتگرال معین

$$\int_C\big[k_1f_1(z)+k_2f_2(z)\big]dz=k_1\int_Cf_1(z)\,dz+k_2\int_Cf_2(z)\,dz\qquad\text{(خطی بودن)}$$
$$\int_{z_0}^{Z}f(z)\,dz=-\int_{Z}^{z_0}f(z)\,dz\qquad\text{(معکوس کردن جهت انتگرال‌گیری)}$$
$$\int_Cf(z)\,dz=\int_{C_1}f(z)\,dz+\int_{C_2}f(z)\,dz\qquad\text{(چند تکه کردن مسیر انتگرال‌گیری)}$$

```{.figure #m12-split-path caption="مسیر $C$ از $z_0$ تا $Z$ که به دو تکهٔ $C_1$ و $C_2$ تقسیم شده است"}
```

## منحنی ساده بسته و ناحیهٔ همبند ساده

::: {.definition title="منحنی ساده بسته"}
منحنی ساده بسته، منحنی بسته‌ای است که خود را قطع نکند.
:::

```{.figure #m12-curve-types caption="منحنی‌های ساده بسته و غیر ساده بسته"}
```

::: {.definition title="ناحیهٔ همبند ساده"}
ناحیهٔ $D$ که اگر هر منحنی بستهٔ ساده‌ای به طور کامل در آن قرار گیرد، نقاط داخل منحنی همه مربوط به این ناحیه باشند.
:::

```{.figure #m12-connected-types caption="ناحیه‌های همبند ساده و غیر همبند"}
```

## انتگرال با تابع اولیه

::: {.theorem}
فرض کنید تابع مختلط $f(z)$ تابعی تحلیلی در ناحیهٔ همبند سادهٔ $D$ باشد. اگر تابع $F(z)$ تابع اولیهٔ $f(z)$ باشد، یعنی $F'(z)=f(z)$، آنگاه داریم:
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

## انتگرال توابع مختلط روی مسیر بسته

انتگرال روی مسیر بستهٔ سادهٔ $C$ که با نماد زیر بیان می‌شود از اهمیت زیادی برخوردار است.
$$\oint_Cf(z)\,dz$$

::: {.theorem title="قضیهٔ انتگرال کشی"}
اگر تابع $f(z)$ در ناحیهٔ همبند سادهٔ $D$ تحلیلی باشد، آنگاه برای هر مسیر سادهٔ بستهٔ $C$ در این ناحیه،
$$\oint_Cf(z)\,dz=0$$
:::

```{.figure #m12-cauchy-region caption="مسیر ساده بستهٔ $C$ در ناحیهٔ همبند سادهٔ $D$"}
```

::: {.proof}
طبق آنچه قبلاً دیدیم، از آنجا که تابع مختلط تحلیلی است، داریم:
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$
$$\oint_Cf(z)\,dz=\oint_C(u+iv)(dx+i\,dy)=\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy)$$
طبق قضیهٔ گرین (که در ریاضی ۲ آموخته‌اید) داریم:
$$\oint_C(L\,dx+M\,dy)=\iint_R\left(\frac{\partial M}{\partial x}-\frac{\partial L}{\partial y}\right)dx\,dy$$
بنابراین
$$\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy)=\iint_R\underbrace{\left(-\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)}_{0}dx\,dy+i\iint_R\underbrace{\left(\frac{\partial u}{\partial x}-\frac{\partial v}{\partial y}\right)}_{0}dx\,dy=0$$
که در آن عبارت اول به دلیل شرط دوم کشی–ریمان و عبارت دوم به دلیل شرط اول کشی–ریمان صفر می‌شوند.
:::

::: {.example}
اگر تابع در همهٔ صفحهٔ مختلط تحلیلی باشد، آنگاه انتگرال روی هر مسیر بسته‌ای صفر خواهد بود:
$$\oint_C\cos z\,dz=0,\qquad \oint_Ce^z\,dz=0,\qquad \oint_Cz^n\,dz=0,\quad n=1,2,3,\dots$$
:::

::: {.example}
اگر تابع نقاط تحلیلی نباشد، ولی آن نقاط بر روی مسیر و داخل $C$ قرار نداشته باشند، انتگرال باز هم صفر است:
$$\oint_{|z|=1}\sec z\,dz,\qquad \oint_{|z|=1}\frac{dz}{z^2+4}$$
(مسیر دایرهٔ واحد است.)
:::

::: {.example}
اگر تابع غیرتحلیلی باشد، انتگرال روی مسیر بسته **ممکن است** صفر نباشد:
$$\oint_{|z|=1}\bar z\,dz,\qquad z(t)=\cos t+i\sin t=e^{it},\quad\dot z(t)=ie^{it}$$
$$\oint_{|z|=1}\bar z\,dz=\int_0^{2\pi}e^{-it}\,ie^{it}\,dt=2\pi i$$
:::

::: {.example}
اگر تابع روی مسیر یا داخل آن غیرتحلیلی باشد، انتگرال روی مسیر بسته **ممکن است** صفر باشد:
$$\oint_C\frac1{z^2}\,dz=0$$
:::

::: {.exercise}
ثابت کنید $\displaystyle\oint_C\frac1{z^2}\,dz=0$.
:::

::: {.remark title="نتیجه ۱"}
همبند بودن ناحیه در قضیهٔ انتگرال کشی اهمیت اساسی دارد.
:::

::: {.remark title="نتیجه ۲"}
اگر تابع $f(z)$ در ناحیهٔ همبند سادهٔ $D$ تحلیلی باشد، آنگاه انتگرال معین به انتخاب مسیر مربوط نیست.
:::

$$\int_{C_1}f(z)\,dz+\int_{C_2^*}f(z)\,dz=0\;\Longrightarrow\;\int_{C_1}f(z)\,dz=-\int_{C_2^*}f(z)\,dz\;\Longrightarrow\;\int_{C_1}f(z)\,dz=\int_{C_2}f(z)\,dz$$

بنابراین انتگرال از مبدأ تا مقصد به مسیر انتخابی وابسته نیست.

```{.figure #m12-path-independence caption="مسیرهای $C_1$، $C_2$ و $C_2^*$ (مسیر $C_2$ با جهت معکوس) میان $z_1$ و $z_2$"}
```

### یک مثال بسیار مهم

$$\oint_C\frac{dz}{z-z_0}=\;?\qquad C:\ z(t)=z_0+re^{it}$$

```{.figure #m12-circle-integral caption="دایرهٔ $C$ به مرکز $z_0$ و شعاع $r$"}
```

$$z(t)=z_0+re^{it},\qquad \dot z(t)=rie^{it}$$
$$\oint_C\frac{dz}{z-z_0}=\int_0^{2\pi}\frac{rie^{it}}{re^{it}}\,dt=\int_0^{2\pi}i\,dt=2\pi i$$

::: {.important}
$$\oint_C\frac{dz}{z-z_0}=2\pi i$$
:::

## فرمول انتگرال کشی

::: {.theorem title="فرمول انتگرال کشی"}
اگر تابع $f(z)$ در ناحیهٔ همبند سادهٔ $D$ تحلیلی بوده و $z_0$ نقطه‌ای در داخل $C$ باشد، آنگاه
$$\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz=f(z_0)$$
:::

::: {.proof}
طبق آنچه قبلاً دیدیم، از آنجا که تابع $\dfrac{f(z)}{z-z_0}$ داخل ناحیهٔ همبند $\Gamma$ تحلیلی است، داریم:
$$\oint_\Gamma\frac{f(z)}{z-z_0}\,dz=0=\int_{ACA'}\frac{f(z)}{z-z_0}\,dz+\int_{A'B'}\frac{f(z)}{z-z_0}\,dz+\int_{B'C'B}\frac{f(z)}{z-z_0}\,dz+\int_{BA}\frac{f(z)}{z-z_0}\,dz$$
$$\lim_{\substack{A\to A'\\ B\to B'}}\int_{BA}\frac{f(z)}{z-z_0}\,dz=-\int_{A'B'}\frac{f(z)}{z-z_0}\,dz$$
در نتیجه (دو انتگرال روی پیوندها یکدیگر را خنثی می‌کنند)
$$\lim_{\substack{A\to A'\\ B\to B'}}\int_{ACA'}\frac{f(z)}{z-z_0}\,dz+\int_{B'C'B}\frac{f(z)}{z-z_0}\,dz=0\;\Longrightarrow\;\oint_C\frac{f(z)}{z-z_0}\,dz=\oint_{C'}\frac{f(z)}{z-z_0}\,dz$$
(در اینجا $C'$ در جهت مثلثاتی پیموده می‌شود.) ادامه:
$$\begin{aligned}
\oint_C\frac{f(z)}{z-z_0}\,dz&=\oint_{C'}\frac{f(z)}{z-z_0}\,dz=\oint_{C'}\frac{f(z)-f(z_0)+f(z_0)}{z-z_0}\,dz\\
&=\oint_{C'}\frac{f(z)-f(z_0)}{z-z_0}\,dz+\oint_{C'}\frac{f(z_0)}{z-z_0}\,dz\\
&=\oint_{C'}g(z)\,dz+f(z_0)\oint_{C'}\frac1{z-z_0}\,dz=0+2\pi i\,f(z_0)=2\pi i\,f(z_0)
\end{aligned}$$
که در آن
$$g(z)\triangleq\begin{cases}\dfrac{f(z)-f(z_0)}{z-z_0}&z\neq z_0\\[2mm] f'(z_0)&z=z_0\end{cases}$$
تابعی تحلیلی در داخل $C'$ است. بنابراین
$$\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz=f(z_0)$$
:::

```{.figure #m12-cauchy-proof caption="مسیر $\\Gamma$ در اثبات فرمول انتگرال کشی: منحنی $C$، دایرهٔ کوچک $C'$ به مرکز $z_0$ و دو پیوند $AA'$ و $BB'$"}
```

## کاربرد: محاسبهٔ انتگرال‌های حقیقی

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ با استفاده از فرمول انتگرال کشی.

::: {.solution}
تابع $g(z)$ را به صورت $g(z)=\dfrac{1}{1+z^2}$ در نظر می‌گیریم. با استفاده از مسیر مشخص شده در شکل انتگرال روی مسیر بسته را به دست می‌آوریم.
$$\oint_C\frac{dz}{1+z^2}=\oint_C\frac{\left[\dfrac1{z+i}\right]}{z-i}\,dz=2\pi i\,\frac1{i+i}=\pi,\qquad f(z)=\frac1{z+i},\quad z_0=i$$
از طرف دیگر
$$\oint_C\frac{dz}{1+z^2}=\int_{-R}^{R}\frac{dx}{1+x^2}+\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}$$
در عبارت بالا جملهٔ اول وقتی $R\to\infty$ مقدار مطلوب خواهد بود.
$$\oint_C\frac{dz}{1+z^2}=\pi=\int_{-\infty}^{\infty}\frac{dx}{1+x^2}+I,\qquad I=\lim_{R\to\infty}\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}=0$$
بنابراین
$$\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi$$
:::
:::

```{.figure #m12-semicircle-1 caption="مسیر نیم‌دایره در نیم‌صفحهٔ بالایی؛ قطب‌ها در $z=\\pm i$"}
```

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle\int_{-\infty}^{\infty}\frac{\cos\omega x}{1+x^2}\,dx$ با استفاده از فرمول انتگرال کشی ($\omega>0$).

::: {.solution}
تابع $g(z)$ را به صورت $g(z)=\dfrac{e^{i\omega z}}{1+z^2}$ در نظر می‌گیریم. با استفاده از مسیر مشخص شده در شکل (همان نیم‌دایرهٔ شکل قبل) انتگرال روی مسیر بسته را به دست می‌آوریم.
$$\oint_C\frac{e^{i\omega z}}{1+z^2}\,dz=\oint_C\frac{\left[\dfrac{e^{i\omega z}}{z+i}\right]}{z-i}\,dz=2\pi i\,\frac{e^{i\omega i}}{i+i}=\pi e^{-\omega},\qquad f(z)=\frac{e^{i\omega z}}{z+i},\quad z_0=i$$
از طرف دیگر
$$\oint_C\frac{e^{i\omega z}\,dz}{1+z^2}=\int_{-R}^{R}\frac{e^{i\omega x}\,dx}{1+x^2}+\int_0^\pi\frac{e^{i\omega Re^{it}}\,iRe^{it}\,dt}{1+R^2e^{i2t}}$$
اما:
$$I_1=\lim_{R\to\infty}\int_0^\pi\frac{e^{i\omega Re^{it}}\,iRe^{it}\,dt}{1+R^2e^{i2t}}\to0$$
**اثبات:**
$$e^{i\omega Re^{it}}=e^{i\omega R(\cos t+i\sin t)}=e^{i\omega R\cos t}\,e^{-\omega R\sin t}$$
$$\lim_{R\to\infty}\left|e^{i\omega Re^{it}}\right|=\lim_{R\to\infty}\left|e^{i\omega R\cos t}\right|\times\left|e^{-\omega R\sin t}\right|=1\times0=0,\qquad t\in[0,\pi]$$
از طرف دیگر در انتگرال $I_1$ بقیهٔ انتگرند زمانی که $R$ بی‌نهایت می‌شود به سمت صفر میل می‌کند. پس حد $I_1$ وقتی $R\to\infty$ صفر می‌شود.

بنابراین
$$\pi e^{-\omega}=\oint_C\frac{e^{i\omega z}\,dz}{1+z^2}=\int_{-R}^{R}\frac{e^{i\omega x}\,dx}{1+x^2}=\int_{-R}^{R}\frac{(\cos x+i\sin x)\,dx}{1+x^2}=\int_{-R}^{R}\frac{\cos x\,dx}{1+x^2}+i\int_{-R}^{R}\frac{\sin x\,dx}{1+x^2}$$
انتگرال دوم صفر است. چرا؟
$$\int_{-\infty}^{\infty}\frac{\cos\omega x}{1+x^2}\,dx=\pi e^{-\omega}$$
:::
:::

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle I=\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)(x^2+4)}$ با استفاده از فرمول انتگرال کشی.

::: {.solution}
$$\frac{1}{(x^2+1)(x^2+4)}=\frac{A}{x^2+1}+\frac{B}{x^2+4}=\frac{1/3}{x^2+1}+\frac{-1/3}{x^2+4}$$
$$\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)(x^2+4)}=\frac13\int_{-\infty}^{\infty}\frac{dx}{x^2+1}-\frac13\int_{-\infty}^{\infty}\frac{dx}{x^2+4}$$

**انتگرال اول:** $I_1=\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+1}$ و $g_1(z)=\dfrac1{z^2+1}$:
$$\oint_Cg_1(z)\,dz=\oint_C\frac1{z^2+1}\,dz=\oint_C\frac{\left[\dfrac1{z+i}\right]}{z-i}\,dz=2\pi i\,\frac1{i+i}=\pi$$
$$\oint_C\frac1{z^2+1}\,dz=\pi=\int_{-R}^{R}\frac{dx}{1+x^2}+\int_0^\pi\frac{iRe^{it}\,dt}{1+R^2e^{i2t}}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^2+1}\,dz=\int_{-R}^{R}\frac{dx}{1+x^2}+0=\pi\;\Longrightarrow\;I_1=\pi$$

**انتگرال دوم:** $I_2=\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+4}$ و $g_2(z)=\dfrac1{z^2+4}$:
$$\oint_Cg_2(z)\,dz=\oint_C\frac1{z^2+4}\,dz=\oint_C\frac{\left[\dfrac1{z+2i}\right]}{z-2i}\,dz=2\pi i\,\frac1{2i+2i}=\frac\pi2$$
$$\oint_C\frac1{z^2+4}\,dz=\frac\pi2=\int_{-R}^{R}\frac{dx}{x^2+4}+\int_0^\pi\frac{iRe^{it}\,dt}{R^2e^{i2t}+4}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^2+4}\,dz=\int_{-R}^{R}\frac{dx}{x^2+4}+0=\frac\pi2\;\Longrightarrow\;I_2=\frac\pi2$$

در نتیجه
$$I=\frac13I_1-\frac13I_2=\frac13\pi-\frac13\times\frac\pi2=\frac\pi6$$
:::
:::

```{.figure #m12-semicircle-2 caption="مسیر نیم‌دایره؛ قطب‌ها در $z=\\pm i$ و $z=\\pm2i$"}
```

::: {.example}
مطلوب است محاسبهٔ انتگرال $\displaystyle I=\int_0^\infty\frac{dx}{x^4+1}$ با استفاده از فرمول انتگرال کشی.

::: {.solution}
$$g(z)=\frac1{z^4+1},\qquad z^4+1=0\;\Longrightarrow\;z_1=e^{i\pi/4},\quad z_2=e^{i3\pi/4},\quad z_3=e^{i5\pi/4},\quad z_4=e^{i7\pi/4}$$
در داخل مسیر $C$ فقط دو قطب $z_1$ و $z_2$ قرار دارند:
$$\begin{aligned}
\oint_Cg(z)\,dz&=\oint_C\frac1{z^4+1}\,dz=\oint_{C_1}\frac1{z^4+1}\,dz+\oint_{C_2}\frac1{z^4+1}\,dz\\
&=\oint_{C_1}\frac{\dfrac1{(z-z_2)(z-z_3)(z-z_4)}}{z-z_1}\,dz+\oint_{C_2}\frac{\dfrac1{(z-z_1)(z-z_3)(z-z_4)}}{z-z_2}\,dz\\
&=2\pi i\left.\frac1{(z-z_2)(z-z_3)(z-z_4)}\right|_{z=z_1}+2\pi i\left.\frac1{(z-z_1)(z-z_3)(z-z_4)}\right|_{z=z_2}\\
&=2\pi i\,\frac1{\underbrace{(e^{i\pi/4}-e^{i3\pi/4})}_{\sqrt2}\underbrace{(e^{i\pi/4}-e^{i5\pi/4})}_{\sqrt2+i\sqrt2}\underbrace{(e^{i\pi/4}-e^{i7\pi/4})}_{i\sqrt2}}\\
&\quad+2\pi i\,\frac1{\underbrace{(e^{i3\pi/4}-e^{i\pi/4})}_{-\sqrt2}\underbrace{(e^{i3\pi/4}-e^{i5\pi/4})}_{i\sqrt2}\underbrace{(e^{i3\pi/4}-e^{i7\pi/4})}_{-\sqrt2+i\sqrt2}}=\frac\pi{\sqrt2}
\end{aligned}$$
از طرف دیگر
$$\oint_C\frac1{z^4+1}\,dz=\frac\pi{\sqrt2}=\int_{-R}^{R}\frac{dx}{x^4+1}+\int_0^\pi\frac{iRe^{it}\,dt}{R^4e^{i4t}+1}$$
$$\lim_{R\to\infty}\oint_C\frac1{z^4+1}\,dz=\int_{-\infty}^{\infty}\frac{dx}{x^4+1}+\underbrace{\lim_{R\to\infty}\int_0^\pi\frac{iRe^{it}\,dt}{R^4e^{i4t}+1}}_{0}=\frac\pi{\sqrt2}$$
$$\int_{-\infty}^{\infty}\frac{dx}{x^4+1}=\frac\pi{\sqrt2}\;\Longrightarrow\;\int_0^\infty\frac{dx}{x^4+1}=\frac\pi{2\sqrt2}$$
:::
:::

```{.figure #m12-semicircle-3 caption="مسیر نیم‌دایره و دایره‌های $C_1$ و $C_2$ حول قطب‌های $z_1$ و $z_2$؛ قطب‌های $z_3$ و $z_4$ در نیم‌صفحهٔ پایینی"}
```

## قضیهٔ انتگرال کشی برای چند نقطهٔ غیرتحلیلی

::: {.theorem}
اگر تابع $f(z)$ در همهٔ نقاط ناحیهٔ $D$ بجز نقاط $z_1,z_2,z_3,\dots,z_n$ در داخل $C$ تحلیلی باشد، آنگاه
$$\oint_Cf(z)\,dz=\oint_{C_1}f(z)\,dz+\oint_{C_2}f(z)\,dz+\cdots+\oint_{C_n}f(z)\,dz$$
که در این رابطه، دایرهٔ $C_k$ دایره‌ای به مرکز $z_k$ است که داخل $C$ قرار داشته سایر نقاط $z_1$ تا $z_n$ را شامل نشود.
:::

```{.figure #m12-multi-points caption="مسیر $C$ و نقاط غیرتحلیلی $z_1,\\dots,z_n$ در داخل آن"}
```

::: {.proof}
مسیر $\Gamma$ را از $C$ (در جهت مثلثاتی)، دایره‌های کوچک $C_1,\dots,C_n$ (در جهت ساعت‌گرد) و پیوندهایی که آن‌ها را به $C$ وصل می‌کنند می‌سازیم؛ انتگرال روی هر پیوند دو بار و در دو جهت مخالف محاسبه می‌شود و حذف می‌گردد. تابع در داخل $\Gamma$ تحلیلی است، پس
$$\oint_\Gamma f(z)\,dz=0\;\Longrightarrow\;\oint_Cf(z)\,dz+\oint_{C_1^{\circlearrowright}}f(z)\,dz+\cdots+\oint_{C_n^{\circlearrowright}}f(z)\,dz=0$$
$$\oint_Cf(z)\,dz=-\oint_{C_1^{\circlearrowright}}f(z)\,dz-\cdots-\oint_{C_n^{\circlearrowright}}f(z)\,dz=\oint_{C_1}f(z)\,dz+\cdots+\oint_{C_n}f(z)\,dz$$
که در آن $C_k^{\circlearrowright}$ دایرهٔ $C_k$ در جهت ساعت‌گرد و $C_k$ همان دایره در جهت مثلثاتی است.
:::

```{.figure #m12-multi-proof caption="مسیر $\\Gamma$ برای اثبات: $C$، دایره‌های $C_1,\\dots,C_n$ و پیوندها"}
```

## مشتق‌های تابع تحلیلی

::: {.theorem title="فرمول انتگرال کشی برای مشتق"}
اگر تابع $f(z)$ در ناحیهٔ همبند سادهٔ $D$ تحلیلی بوده و $z_0$ نقطه‌ای در داخل $C$ باشد، آنگاه
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

::: {.theorem title="تعمیم فرمول انتگرال کشی"}
اگر تابع $f(z)$ در ناحیهٔ همبند سادهٔ $D$ تحلیلی بوده و $z_0$ نقطه‌ای در داخل $C$ باشد، آنگاه
$$\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz=f^{(n)}(z_0)$$
:::

::: {.exercise}
از طریق استقراء ریاضی ثابت کنید.
:::

::: {.example}
مطلوب است محاسبهٔ انتگرال زیر. ($C$ دایرهٔ واحد است.)
$$I=\oint_C\frac{z^2}{(2z-1)^2}\,dz$$

::: {.solution}
$$I=\oint_C\frac{z^2}{4(z-1/2)^2}\,dz=\frac14\oint_C\frac{z^2}{(z-1/2)^2}\,dz=\frac14\times2\pi i\times\left.\frac{d}{dz}\big(z^2\big)\right|_{z=1/2}=\frac14\times2\pi i\times(2z)\Big|_{z=1/2}=\frac\pi2\,i$$
($z=1/2$ داخل دایرهٔ واحد است.)
:::
:::

::: {.example}
مطلوب است محاسبهٔ انتگرال زیر. ($C$ دایرهٔ واحد است.)
$$I=\oint_C\frac{e^{-z}\sin z}{z^2}\,dz$$

::: {.solution}
$$f(z)=e^{-z}\sin z,\quad z_0=0,\qquad f'(z)=-e^{-z}\sin z+e^{-z}\cos z,\qquad f'(z_0)=f'(0)=1$$
$$I=2\pi i\,f'(z_0)=2\pi i$$
:::
:::

::: {.exercise title="مسئله"}
هرگاه $f(z)$ در تمام صفحهٔ $z$ تحلیلی و در تمام صفحه کران‌دار باشد، یعنی $|f(z)|<M$، ثابت کنید: $f(z)=k$، $k\in\mathbb{C}$.

::: {.solution}
مسیر $C$ را به صورت دایره‌ای به شعاع $R$ و به مرکز $z_0$ انتخاب می‌کنیم و $R$ را به سمت بی‌نهایت میل می‌دهیم.
$$f'(z_0)=\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz$$
$$|f'(z_0)|=\left|\frac1{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz\right|\le\frac1{2\pi}\oint_C\frac{|f(z)|}{|z-z_0|^2}\,|dz|\le\frac1{2\pi}\,\frac{M}{R^2}\oint_C|dz|=\frac1{2\pi}\,\frac{M}{R^2}\cdot2\pi R=\frac MR\to0\quad(R\to\infty)$$
$$\Longrightarrow\;|f'(z_0)|=0\;\Longrightarrow\;f'(z)=0\;\Longrightarrow\;f(z)=k$$
:::
:::

```{.figure #m12-liouville-circle caption="دایرهٔ $C$ به مرکز $z_0$ و شعاع $R$"}
```

::: {.exercise}
مطلوب است محاسبهٔ انتگرال‌های زیر:

1. $\displaystyle\oint_C\frac{z^2}{(2z-1)^4}\,dz$، $C$: دایرهٔ واحد
2. $\displaystyle\int_{1+i}^{1+3i}e^z\sin z\,dz$
3. $\displaystyle\int_{1+i}^{2+2i}\operatorname{Re}\{z^2\}\,dz$ روی مسیر خط راست
4. $\displaystyle\oint_C\frac{e^{\cos z}\sin z}{1+z^6}\,dz$ روی مسیر زیر
:::

```{.figure #m12-exercise-circle caption="مسیر تمرین ۴: دایره‌ای به مرکز $3+3i$ و شعاع $r=1$"}
```
