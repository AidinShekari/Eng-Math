# سری لورنت، نقاط تکین و مانده‌ها

## سری لورنت

::: {.theorem title="سری لورنت"}
اگر تابع $f(z)$ تابعی تحلیلی در ناحیهٔ $D$ باشد، سری لورنت این تابع حول نقطهٔ $z_0$ به صورت زیر نوشته می‌شود:
$$f(z)=\sum_{n=-\infty}^{\infty}a_n\,(z-z_0)^n,\qquad a_n=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{n+1}}\,dv$$
که در آن $C$ دایره‌ای به مرکز $z_0$ است و تابع در همهٔ نقاط داخل و روی این دایره، مگر استثنائاً در $z_0$ تحلیلی است.

شعاع همگرائی، فاصلهٔ $z_0$ تا نزدیک‌ترین نقطهٔ غیرتحلیلی تابع $f(z)$ است.
:::

برای $n$ های نامنفی داریم:
$$a_n=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{n+1}}\,dv=\frac{f^{(n)}(z_0)}{n!},\qquad n=0,1,2,\dots$$
بنابراین خواهیم داشت:
$$\begin{aligned}
f(z)&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=-\infty}^{-1}a_n(z-z_0)^n\\
&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=1}^{\infty}a_{-n}(z-z_0)^{-n}\\
&=\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n+\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n},\qquad A_n=a_{-n}
\end{aligned}$$
$$A_n=a_{-n}=\frac1{2\pi i}\oint_C\frac{f(v)}{(v-z_0)^{-n+1}}\,dv=\frac1{2\pi i}\oint_C(v-z_0)^{n-1}f(v)\,dv,\qquad n=1,2,\dots$$

::: {.important title="سری لورنت: بخش تیلور و بخش تکین"}
$$f(z)=\underbrace{\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n}_{\text{بخش سری تیلور}}+\underbrace{\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n}}_{\text{بخش تکین}},\qquad A_n=\frac1{2\pi i}\oint_C(v-z_0)^{n-1}f(v)\,dv$$
:::

در صورتی که $z_0$ نقطه‌ای غیر عادی (تکین) باشد، به عبارت دیگر تابع در این نقطه تحلیلی نباشد، بخش سری تیلور برای بیان تابع به تنهائی کافی نیست.

### حالت‌های مختلف نقطهٔ $z_0$

1. اگر تمامی $A_n$ ها صفر باشند، نقطهٔ $z_0$ یک نقطهٔ **معمولی** (Regular) نامیده می‌شود. سری لورنت در این حالت همان سری تیلور خواهد بود.
2. اگر $A_p\neq0$ ولی $(A_n=0\ \ \forall n>p)$، آنگاه $z_0$ را **قطب** (pole) **از مرتبهٔ $p$** می‌نامند.
3. اگر $z_0$ نقطهٔ عادی نبوده و ضمناً قطب نیز نباشد، (به عبارت دیگر مقداری مانند $p$ یافت نشود به قسمی که $A_p\neq0$ ولی $(A_n=0\ \ \forall n>p)$)، آنگاه $z_0$ را نقطهٔ **تکین اصلی** (Essential Singularity) می‌نامند.

## مانده

::: {.definition title="مانده (Residue)"}
مانده تابع $f(z)$ در نقطهٔ $z_0$: $A_1$.
$$\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=A_1=\frac1{2\pi i}\oint_Cf(v)\,dv$$
:::

::: {.theorem}
اگر تابع $f(z)$ در نقطهٔ $z_0$ دارای قطب از مرتبهٔ $p$ باشد داریم:
$$A_k=\frac1{(p-k)!}\left.\frac{d^{\,p-k}}{dz^{\,p-k}}\Big[(z-z_0)^p\,f(z)\Big]\right|_{z=z_0},\qquad k=1,2,\dots,p$$
:::

::: {.proof}
$$f(z)=\sum_{n=1}^{\infty}\frac{A_n}{(z-z_0)^n}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$
اگر تابع $f(z)$ در نقطهٔ $z_0$ دارای قطب از مرتبهٔ $p$ باشد داریم:
$$f(z)=\frac{A_p}{(z-z_0)^p}+\frac{A_{p-1}}{(z-z_0)^{p-1}}+\cdots+\frac{A_2}{(z-z_0)^2}+\frac{A_1}{z-z_0}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$
اگر طرفین را در $(z-z_0)^p$ ضرب کنیم داریم:
$$(z-z_0)^pf(z)=A_p+A_{p-1}(z-z_0)+\cdots+A_2(z-z_0)^{p-2}+A_1(z-z_0)^{p-1}+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p}$$
حال اگر به $z$ مقدار $z_0$ بدهیم، داریم:
$$(z-z_0)^pf(z)\Big|_{z=z_0}=A_p$$
اگر از طرفین $(z-z_0)^pf(z)$ یک بار مشتق بگیریم و به $z$ مقدار $z_0$ بدهیم، داریم:
$$\begin{aligned}
\frac{d}{dz}\Big[(z-z_0)^pf(z)\Big]\Big|_{z=z_0}&=\Bigg\{A_{p-1}+\cdots+A_2(p-2)(z-z_0)^{p-3}+A_1(p-1)(z-z_0)^{p-2}\\
&\qquad+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p-1}(n+p)\Bigg\}\Bigg|_{z=z_0}=A_{p-1}
\end{aligned}$$
اگر از طرفین $(z-z_0)^pf(z)$ دو بار مشتق بگیریم و به $z$ مقدار $z_0$ بدهیم، داریم:
$$\begin{aligned}
\frac{d^2}{dz^2}\Big[(z-z_0)^pf(z)\Big]\Big|_{z=z_0}&=\Bigg\{2A_{p-2}+\cdots+A_2(p-2)(p-3)(z-z_0)^{p-4}+A_1(p-1)(p-2)(z-z_0)^{p-3}\\
&\qquad+\sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^{n+p-2}(n+p)(n+p-1)\Bigg\}\Bigg|_{z=z_0}=2A_{p-2}
\end{aligned}$$
$$\Longrightarrow\quad A_{p-2}=\frac1{2!}\left.\frac{d^2}{dz^2}\Big[(z-z_0)^pf(z)\Big]\right|_{z=z_0}$$
:::

::: {.exercise}
به همین ترتیب مشتق‌گیری را ادامه دهید و اثبات قضیه را کامل کنید.
:::

::: {.remark title="نتیجه"}
در حالت خاص، در صورتی که تابع $f(z)$ در نقطهٔ $z_0$ دارای قطب از مرتبهٔ $p$ باشد، مقدار مانده از رابطهٔ زیر به دست می‌آید:
$$\operatorname{Res}\{f(z)\}=A_1=\frac1{(p-1)!}\left.\frac{d^{\,p-1}}{dz^{\,p-1}}\Big[(z-z_0)^p\,f(z)\Big]\right|_{z=z_0}$$
:::

## قضیهٔ مانده‌ها

::: {.theorem title="قضیهٔ مانده‌ها"}
اگر تابع $f(z)$ در همه‌جای داخل مسیر $C$ به‌جز نقاط $z_1,z_2,\dots,z_n$ تحلیلی باشد و مانده تابع در این نقاط به ترتیب $A_1^1,A_1^2,\dots,A_1^n$ باشد، آنگاه:
$$\oint_Cf(z)\,dz=2\pi i\sum_{k=1}^{n}A_1^k$$
:::

```{.figure #m06-residue-theorem caption="مسیر $C$ و نقاط تکین $z_1,\\dots,z_n$ در داخل آن؛ حول هر نقطه دایره‌ای کوچک رسم شده است"}
```

اثبات به عنوان تمرین بر عهدهٔ خواننده است.

## مثال‌هایی از بسط تیلور و لورنت

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\dfrac1{z^4+1}$ در همسایگی نقطهٔ $z_0=0$.

::: {.solution}
دیده می‌شود که تابع $f(z)$ در نقطهٔ $z_0=0$ تحلیلی است و لذا این نقطه یک نقطهٔ معمولی است و سری لورنت همان سری تیلور (مک‌لورن) خواهد بود. لذا داریم:
$$f(z)=f(0)+\frac1{1!}f^{(1)}(0)z+\frac1{2!}f^{(2)}(0)z^2+\frac1{3!}f^{(3)}(0)z^3+\cdots$$
سری هندسی:
$$1+q+q^2+q^3+q^4+\cdots=\frac1{1-q},\qquad |q|<1$$
$$\frac1{1+z^4}=1-z^4+z^8-z^{12}+-\cdots,\qquad |z^4|<1\ \Longrightarrow\ |z|<1$$
(سری تیلور/مک‌لورن؛ ناحیهٔ همگرائی با شعاع ۱.)
$$z^4+1=0\;\Longrightarrow\;z_1=e^{i\pi/4},\quad z_2=e^{i3\pi/4},\quad z_3=e^{i5\pi/4},\quad z_4=e^{i7\pi/4}$$
مشاهده می‌شود که فاصلهٔ $z_0=0$ تا نزدیک‌ترین نقطهٔ غیرتحلیلی تابع (شعاع همگرائی) عدد ۱ می‌باشد.
:::
:::

```{.figure #m06-radius-1 caption="چهار قطب $z^4+1=0$ روی دایرهٔ واحد؛ شعاع همگرائی سری حول مبدأ برابر ۱ است"}
```

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\dfrac{4z^2+30z+68}{(z+4)^2(z-2)}$ در همسایگی نقطهٔ $z_0=0$.

::: {.solution}
دیده می‌شود که تابع $f(z)$ در نقطهٔ $z_0=0$ تحلیلی است و لذا این نقطه یک نقطهٔ معمولی است و سری لورنت همان سری تیلور (مک‌لورن) خواهد بود. لذا داریم:
$$f(z)=f(0)+\frac1{1!}f^{(1)}(0)z+\frac1{2!}f^{(2)}(0)z^2+\frac1{3!}f^{(3)}(0)z^3+\cdots$$
$$\frac1{z-2}=\frac{-1}{2-z}=\frac{-1}2\,\frac1{1-z/2}=\frac{-1}2\left(1+\frac z2+\frac{z^2}4+\frac{z^3}8+\cdots\right),\qquad \left|\frac z2\right|<1\ \Longrightarrow\ |z|<2$$
$$\frac1{4+z}=\frac14\,\frac1{1+z/4}=\frac14\left(1-\frac z4+\frac{z^2}{16}-\frac{z^3}{64}+\cdots\right),\qquad \left|-\frac z4\right|<1\ \Longrightarrow\ |z|<4$$
$$\frac d{dz}\left(\frac1{4+z}\right)=\frac{-1}{(4+z)^2}=\frac14\left(-\frac14+\frac{2z}{16}-\frac{3z^2}{64}+\cdots\right)\;\Longrightarrow\;\frac1{(4+z)^2}=\frac14\left(\frac14-\frac{2z}{16}+\frac{3z^2}{64}-\cdots\right)$$
$$f(z)=(4z^2+30z+68)\times\frac1{(z+4)^2}\times\frac1{z-2}$$
$$f(z)=(4z^2+30z+68)\times\left(\frac{-1}2\right)\left(1+\frac z2+\frac{z^2}4+\frac{z^3}8+\cdots\right)\times\frac14\left(\frac14-\frac z8+\frac{3z^2}{64}-\cdots\right)$$
$$f(z)=\frac{-1}{16}\left(34+15z+\frac{67}8z^2+\cdots\right),\qquad |z|<2$$
(ناحیهٔ همگرائی با شعاع ۲.)
:::
:::

```{.figure #m06-radius-2 caption="قطب‌های $z=-4$ و $z=2$؛ دایرهٔ همگرائی حول مبدأ شعاع ۲ دارد"}
```

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\cos z^2$ در همسایگی نقطهٔ $z_0=0$.

::: {.solution}
با توجه به تعریف تابع کسینوس، داریم:
$$\cos z=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots$$
$$f(z)=\cos z^2=1-\frac{z^4}{2!}+\frac{z^8}{4!}-\frac{z^{12}}{6!}+-\cdots$$
ناحیهٔ همگرائی تمام صفحهٔ مختلط با شعاع همگرائی بی‌نهایت.
:::
:::

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\dfrac{\cos z}{1-z^2}$ در همسایگی نقطهٔ $z_0=0$.

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
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\dfrac1{z^4}$ در همسایگی نقطهٔ $z_0=1$.

::: {.solution}
$$g(z)=\frac1z=\frac1{z-1+1}=\frac1{1+(z-1)}=1-(z-1)+(z-1)^2-(z-1)^3+-\cdots,\qquad |z-1|<1$$
$$\frac d{dz}g(z)=\frac{-1}{z^2}=-1+2(z-1)-3(z-1)^2+4(z-1)^3-+\cdots,\qquad |z-1|<1$$
$$\frac{d^2}{dz^2}g(z)=\frac2{z^3}=2-6(z-1)+12(z-1)^2-20(z-1)^3+-\cdots,\qquad |z-1|<1$$
$$\frac{d^3}{dz^3}g(z)=\frac{-6}{z^4}=-6+24(z-1)-60(z-1)^2-+\cdots,\qquad |z-1|<1$$
$$f(z)=\frac1{z^4}=1-4(z-1)+10(z-1)^2-+\cdots$$
:::
:::

```{.figure #m06-radius-3 caption="ناحیهٔ همگرائی سری حول $z_0=1$ دایره‌ای به شعاع ۱ است (تا قطب $z=0$)"}
```

::: {.exercise}
مطلوب است بسط لورنت توابع زیر در همسایگی $z_0=0$:

1. $f_1(z)=\dfrac1{\sqrt{1-z^2}}$
2. $f_2(z)=\sin^{-1}z$
3. $f_3(z)=\dfrac{e^z}{z^2(z^2+1)}$
4. تابع $\sinh z$ را بر حسب توانهائی از $(z-\pi i)$ بسط داده، ثابت کنید: $\displaystyle\lim_{z\to\pi i}\frac{\sinh z}{z-\pi i}=-1$
5. ثابت کنید: $\displaystyle z\cosh z^2=z+\sum_{n=1}^{\infty}\frac1{(2n)!}\,z^{4n+1}$
:::

## مثال‌هایی از نقاط تکین و مانده

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\dfrac{z}{(z+1)(z+4)^3}$ در همسایگی نقاط غیرتحلیلی آن و محاسبهٔ مانده در آن نقاط.

::: {.solution}
تابع در $z=-1$ و $z=-4$ تحلیلی نیست.

**الف)** در همسایگی $z=-1$ دایره‌ای به مرکز این نقطه و به شعاع کمتر از ۳ ($|z+1|<3$) نقطهٔ تکین (ایزولهٔ) $z=-4$ را در بر ندارد.
$$\frac{z}{(z+4)^3}=\frac{z+4-4}{(z+4)^3}=\frac{z+4}{(z+4)^3}+\frac{-4}{(z+4)^3}=\frac1{(z+4)^2}-\frac4{(z+4)^3}$$
$$\frac1{z+4}=\frac1{(z+1)+3}=\frac13\,\frac1{1+\frac{z+1}3}=\frac13\left[1-\frac{z+1}3+\left(\frac{z+1}3\right)^2-\left(\frac{z+1}3\right)^3+-\cdots\right]$$
$$\frac{-1}{(z+4)^2}=\frac13\left[-\frac13+\frac2{3^2}(z+1)-\frac3{3^3}(z+1)^2+-\cdots\right]\;\Longrightarrow\;\frac1{(z+4)^2}=\frac19-\frac2{27}(z+1)+\frac1{27}(z+1)^2-+\cdots$$
$$\frac1{(z+4)^3}=\frac16\left[\frac2{3^2}-\frac{2\times3}{3^3}(z+1)+\frac{3\times4}{3^4}(z+1)^2-\frac{4\times5}{3^5}(z+1)^3+-\cdots\right]=\frac1{27}-\frac1{27}(z+1)+\frac2{81}(z+1)^2-+\cdots$$
$$\frac z{(z+4)^3}=\frac1{(z+4)^2}-\frac4{(z+4)^3}=-\frac1{27}+\frac2{27}(z+1)-\frac5{81}(z+1)^2+\cdots$$
$$f(z)=\frac1{z+1}\,\frac z{(z+4)^3}=-\frac1{27}\,\frac1{z+1}+\frac2{27}-\frac5{81}(z+1)+\cdots$$
نوع نقطهٔ تکین: قطب ساده (از مرتبهٔ ۱). مانده: $\operatorname{Res}\{f(z)\}\big|_{z=-1}=-\dfrac1{27}$.

**ب)** در همسایگی $z=-4$ دایره‌ای به مرکز این نقطه و به شعاع کمتر از ۳ ($|z+4|<3$) نقطهٔ تکین (ایزولهٔ) $z=-1$ را در بر ندارد.
$$\frac z{z+1}=\frac{z+1-1}{z+1}=\frac{z+1}{z+1}-\frac1{z+1}=1-\frac1{z+1}$$
$$\frac1{z+1}=\frac1{z+4-3}=\frac1{-3+(z+4)}=\frac{-1}3\,\frac1{1-\frac{z+4}3}=\frac{-1}3\left[1+\frac{z+4}3+\frac{(z+4)^2}{3^2}+\cdots\right],\qquad |z+4|<3$$
$$\frac z{z+1}=1+\frac13+\frac1{3^2}(z+4)+\frac1{3^3}(z+4)^2+\frac1{3^4}(z+4)^3+\cdots$$
$$f(z)=\frac z{(z+1)(z+4)^3}=\frac1{(z+4)^3}\,\frac z{z+1}=\frac{4/3}{(z+4)^3}+\frac1{3^2}\frac1{(z+4)^2}+\frac1{3^3}\frac1{z+4}+\frac1{3^4}+\frac1{3^5}(z+4)+\frac1{3^6}(z+4)^2+\cdots$$
نوع نقطهٔ تکین: قطب از مرتبهٔ ۳. مانده: $\operatorname{Res}\{f(z)\}\big|_{z=-4}=\dfrac1{27}$.
:::
:::

```{.figure #m06-poles-1 caption="قطب‌های $z=-1$ و $z=-4$ تابع $f(z)=\\frac{z}{(z+1)(z+4)^3}$"}
```

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=e^{1/z}$ در همسایگی نقطهٔ غیرتحلیلی آن و محاسبهٔ مانده در آن نقطه.

::: {.solution}
$$e^z=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots\;\Longrightarrow\;e^{1/z}=1+\frac1z+\frac1{2!\,z^2}+\frac1{3!\,z^3}+\cdots$$
نوع نقطهٔ تکین: تکین اصلی (بی‌نهایت جمله با توان‌های منفی). مانده: $\operatorname{Res}\{f(z)\}\big|_{z=0}=1$.
:::
:::

::: {.example}
مطلوب است محاسبهٔ سری لورنت تابع $f(z)=\cos\!\left(\dfrac z{z-1}\right)$ در همسایگی نقطهٔ غیرتحلیلی آن و محاسبهٔ مانده در آن نقطه.

::: {.solution}
$$\frac z{z-1}=1+\frac1{z-1}\;\Longrightarrow\;\cos\!\left(\frac z{z-1}\right)=\cos\!\left(1+\frac1{z-1}\right)=\cos1\cos\!\left(\frac1{z-1}\right)-\sin1\sin\!\left(\frac1{z-1}\right)$$
$$\cos z=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\frac{z^6}{6!}+-\cdots,\qquad \sin z=z-\frac{z^3}{3!}+\frac{z^5}{5!}-+\cdots$$
$$\begin{aligned}
\cos\!\left(\frac z{z-1}\right)&=\cos1\left(1-\frac1{2!}\frac1{(z-1)^2}+\frac1{4!}\frac1{(z-1)^4}-+\cdots\right)\\
&\quad-\sin1\left(\frac1{z-1}-\frac1{3!}\frac1{(z-1)^3}+\frac1{5!}\frac1{(z-1)^5}-+\cdots\right)\\
&=\cos1-\sin1\,\frac1{z-1}-\cos1\,\frac1{2!}\frac1{(z-1)^2}+\sin1\,\frac1{3!}\frac1{(z-1)^3}+\cdots
\end{aligned}$$
نوع نقطهٔ تکین: تکین اصلی. مانده: $\operatorname{Res}\{f(z)\}\big|_{z=1}=-\sin1$.
:::
:::

::: {.theorem title="مانده در قطب ساده"}
ثابت کنید هرگاه تابع $f(z)=q(z)/g(z)$ بوده و $g(z)$ در نقطهٔ $z_0$ ریشهٔ مرتبهٔ اول داشته باشد، آنگاه
$$\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=\frac{q(z_0)}{g'(z_0)}$$
:::

::: {.proof}
چون نقطهٔ $z_0$ قطب مرتبهٔ ۱ است داریم ($p=1$):
$$\begin{aligned}
\operatorname{Res}\{f(z)\}\Big|_{z=z_0}=A_1&=\frac1{(p-1)!}\left.\frac{d^{\,p-1}}{dz^{\,p-1}}\Big[(z-z_0)^pf(z)\Big]\right|_{z=z_0}=(z-z_0)\frac{q(z)}{g(z)}\Bigg|_{z=z_0}\\
&=(z-z_0)\frac{q(z)}{g(z)-g(z_0)}\Bigg|_{z=z_0}=\frac{q(z)}{\dfrac{g(z)-g(z_0)}{z-z_0}}\Bigg|_{z=z_0}=\frac{q(z_0)}{g'(z_0)}
\end{aligned}$$
:::

::: {.exercise}
سری لورنت توابع زیر را حول $z=0$ به دست آورده، نوع این نقطه را تعیین کنید.
$$f_1(z)=\frac z{e^z-1},\qquad f_2(z)=\frac{e^{-z}}{z^3},\qquad f_3(z)=\frac1{z^2(1-z^2)},\qquad f_4(z)=\frac{\sin z^2}{z^3}$$
:::
