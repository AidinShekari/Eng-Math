# معادلهٔ موجی یک‌بعدی و روش جداسازی متغیرها

## مقدمه

::: {.definition title="معادلهٔ دیفرانسیل"}
معادله‌ای که در آن تابع و مشتقات وجود داشته باشند.
:::

::: {.definition title="معادلهٔ دیفرانسیل معمولی"}
معادله‌ای که بر حسب فقط یک متغیر مستقل و مشتقات تابع فقط بر حسب آن متغیر نوشته شده باشد.
:::

::: {.definition title="معادلهٔ دیفرانسیل با مشتقات جزئی"}
معادلهٔ دیفرانسیلی که تابع به چند متغیر مستقل وابسته بوده، مشتقات جزئی تابع بر حسب متغیرهای مختلف در معادله وجود داشته باشد.
:::

**معادلهٔ دیفرانسیل موج:**
$$\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2},\qquad \frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right),\qquad \frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}\right)$$

**معادلهٔ دیفرانسیل انتقال حرارت:**
$$\frac{\partial u}{\partial t}=c^2\frac{\partial^2u}{\partial x^2},\qquad \frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right),\qquad \frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}\right)$$

**معادلهٔ دیفرانسیل لاپلاس:**
$$\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0,\qquad \frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}=0,\qquad \nabla^2u=0$$

## معادلهٔ دیفرانسیل موجی یک‌بعدی

مدلسازی یک تار مرتعش (به‌دست آوردن معادلهٔ حاکم بر $u(x,t)$).

**فرضیات فیزیکی:**

- جرم به صورت یکنواخت در طول تار توزیع شده (تار همگن)، کاملاً انعطاف‌پذیر است.
- تار چنان محکم کشیده شده است که نیروی جاذبه در آن قابل چشم‌پوشی است.
- میزان انحراف تار از حالت تعادل بسیار کوچک است.

```{.figure #m04-string caption="قطعهٔ $PQ$ از تار مرتعش: کشش‌های $T_1$ و $T_2$ در دو انتها با زوایای $\\alpha$ و $\\beta$"}
```

$$T_1\cos\alpha=T_2\cos\beta=T=\text{const.}$$
$$T_2\sin\beta-T_1\sin\alpha=\rho\,\Delta s\,\frac{\partial^2u}{\partial t^2}$$
که در آن $\rho$ چگالی جرمی تار و $\Delta s$ دیفرانسیل طول تار است. با تقسیم بر $T$:
$$T\big(\tan\beta-\tan\alpha\big)=\rho\,\Delta s\,\frac{\partial^2u}{\partial t^2}\quad\Longrightarrow\quad T\left(\frac{\partial u}{\partial x}\bigg|_{(x+\Delta x,t)}-\frac{\partial u}{\partial x}\bigg|_{(x,t)}\right)=\rho\,\Delta s\,\frac{\partial^2u}{\partial t^2}$$

با استفاده از قضیهٔ مقدار میانی ($f(b)-f(a)=f'(l)(b-a)$، $l\in[a,b]$):
$$T\left(\frac{\partial u}{\partial x}\bigg|_{(x+\Delta x,t)}-\frac{\partial u}{\partial x}\bigg|_{(x,t)}\right)=T\frac{\partial^2u}{\partial x^2}\bigg|_{(l,t)}\Delta x=\rho\,\Delta s\,\frac{\partial^2u}{\partial t^2},\qquad x<l<x+\Delta x$$
طبق فرض $\displaystyle\lim_{\Delta x\to0}\frac{\Delta x}{\Delta s}=1$، پس:
$$T\frac{\partial^2u}{\partial x^2}=\rho\frac{\partial^2u}{\partial t^2},\qquad c^2\triangleq\frac T\rho\quad\Longrightarrow\quad\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2}$$

برای حل یکتای این معادله نیاز به شرایط مرزی و شرایط اولیه داریم:

- شرایط مرزی (Boundary Conditions): $u(0,t)=u(L,t)=0$
- شرایط اولیه (Initial Conditions): $u(x,0)=f(x)$ و $u_t(x,0)=g(x)$، که در آن $u_t\triangleq\dfrac{\partial u}{\partial t}$

## حل معادلهٔ دیفرانسیل موجی یک‌بعدی

$$\begin{cases}\dfrac{\partial^2u}{\partial t^2}=c^2\dfrac{\partial^2u}{\partial x^2}\\[2mm] u(0,t)=u(L,t)=0\\ u(x,0)=f(x)\\ u_t(x,0)=g(x)\end{cases}$$

در اینجا برای حل این معادله از روش **جداسازی متغیرها** استفاده می‌کنیم. فرض:
$$u(x,t)=X(x)\times T(t)$$
$$\frac{\partial^2u}{\partial x^2}=X''(x)T(t),\qquad \frac{\partial^2u}{\partial t^2}=X(x)T''(t)\quad\Longrightarrow\quad X(x)T''(t)=c^2X''(x)T(t)\quad\Longrightarrow\quad\frac{T''}{c^2T}=\frac{X''}{X}=k$$

$k$ باید حتماً یک عدد منفی باشد. بررسی حالت‌ها:

**اگر $k=0$:**
$$\frac{X''}{X}=0\ \Rightarrow\ X''=0\ \Rightarrow\ X(x)=Ax+B,\qquad X(0)=0\Rightarrow B=0,\quad X(L)=0\Rightarrow A=0\ \Rightarrow\ X(x)=0$$

**اگر $k>0$ ($k=\lambda^2$):**
$$\frac{X''}{X}=\lambda^2\ \Rightarrow\ X''-\lambda^2X=0\ \Rightarrow\ X(x)=Ae^{\lambda x}+Be^{-\lambda x},\qquad X(0)=0\Rightarrow A+B=0,\quad X(L)=0\Rightarrow Ae^{\lambda L}+Be^{-\lambda L}=0$$
$$\Longrightarrow\ A=B=0\ \Rightarrow\ X(x)=0$$

بنابراین $k$ باید حتماً یک عدد منفی باشد ($k=-\lambda^2$):
$$\frac{T''}{c^2T}=\frac{X''}{X}=-\lambda^2\quad\Longrightarrow\quad\begin{cases}X''+\lambda^2X=0\\ T''+c^2\lambda^2T=0\end{cases}$$
$$X(x)=A\cos\lambda x+B\sin\lambda x,\qquad X(0)=0\Rightarrow A=0$$
$$X(L)=0\ \Rightarrow\ B\sin\lambda L=0\ \Rightarrow\ \lambda L=n\pi\ \ (n\in\mathbb{Z})\ \Rightarrow\ \lambda=\frac{n\pi}L=\lambda_n$$
$$X_n(x)=B_n\sin\lambda_nx,\qquad \lambda_n=\frac{n\pi}L\ \ (n\in\mathbb{Z})$$
$$T''+c^2\lambda_n^2T=0\ \Rightarrow\ T_n(t)=C_n\cos(c\lambda_nt)+D_n\sin(c\lambda_nt)$$
$$u_n(x,t)=X_n(x)\times T_n(t)=B_n\sin\lambda_nx\times\big(C_n\cos(c\lambda_nt)+D_n\sin(c\lambda_nt)\big)$$
با برهم‌نهی جواب‌ها:
$$u(x,t)=\sum_{n=1}^{\infty}\left[a_n\cos\!\left(\frac{cn\pi}Lt\right)+b_n\sin\!\left(\frac{cn\pi}Lt\right)\right]\sin\frac{n\pi}Lx$$

**اعمال شرایط اولیه.** شرط $u(x,0)=f(x)$:
$$u(x,0)=\sum_{n=1}^{\infty}a_n\sin\frac{n\pi}Lx=f(x)$$
تابع $f(x)$ با یک تابع تناوبی و فرد برابر شده است، بنابراین برای محاسبهٔ ضرایب مجهول فوریه باید $f(x)$ را یک تابع تناوبی (با دورهٔ تناوب $2L$) و فرد فرض کنیم. به این صورت خواهیم داشت:
$$a_n=\frac2{2L}\int_{-L}^{L}f(x)\sin\!\left(\frac{2\pi}{2L}nx\right)dx=\frac1L\int_{-L}^{L}f(x)\sin\!\left(\frac{n\pi}Lx\right)dx=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx$$
شرط $u_t(x,0)=g(x)$:
$$u_t(x,t)=\sum_{n=1}^{\infty}\left[-a_n\frac{cn\pi}L\sin\!\left(\frac{cn\pi}Lt\right)+b_n\frac{cn\pi}L\cos\!\left(\frac{cn\pi}Lt\right)\right]\sin\frac{n\pi}Lx$$
$$u_t(x,0)=\sum_{n=1}^{\infty}b_n\frac{cn\pi}L\sin\frac{n\pi}Lx=g(x)\quad\Longrightarrow\quad b_n=\frac2{cn\pi}\int_0^Lg(x)\sin\!\left(\frac{n\pi}Lx\right)dx$$

::: {.important title="جواب معادلهٔ موجی یک‌بعدی (روش جداسازی متغیرها)"}
$$u(x,t)=\sum_{n=1}^{\infty}\left[a_n\cos\!\left(\frac{cn\pi}Lt\right)+b_n\sin\!\left(\frac{cn\pi}Lt\right)\right]\sin\frac{n\pi}Lx$$
$$a_n=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx,\qquad b_n=\frac2{cn\pi}\int_0^Lg(x)\sin\!\left(\frac{n\pi}Lx\right)dx$$
:::

::: {.example title="مثال ۱"}
جواب معادلهٔ موجی یک‌بعدی زیر را به‌دست آورید.
$$\frac{\partial^2u}{\partial t^2}=\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=u(\pi,t)=0,\qquad u(x,0)=k\sin2x,\qquad u_t(x,0)=0$$

::: {.solution}
با توجه به اینکه سرعت اولیهٔ تار مرتعش صفر است، $g(x)=0\Rightarrow b_n=0$. بنابراین ($c=1$، $L=\pi$):
$$u(x,t)=\sum_{n=1}^{\infty}a_n\cos\!\left(\frac{cn\pi}Lt\right)\sin\frac{n\pi}Lx=\sum_{n=1}^{\infty}a_n\cos nt\,\sin nx$$
$$a_n=\frac2L\int_0^Lf(x)\sin\!\left(\frac{n\pi}Lx\right)dx=\frac2\pi\int_0^\pi k\sin2x\sin nx\,dx=\begin{cases}0&n\neq2\\ k&n=2\end{cases}$$
$$u(x,t)=k\sin2x\cos2t$$
:::
:::

```{.figure #m04-mode2 caption="مود دوم ارتعاش تار: $u(x,t)=k\\sin2x\\cos2t$ در لحظه‌های مختلف"}
```

::: {.example title="مثال ۲"}
جواب معادلهٔ موجی یک‌بعدی زیر را به‌دست آورید.
$$\frac{\partial^2u}{\partial t^2}=\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=u(\pi,t)=0,\qquad u(x,0)=f(x),\qquad u_t(x,0)=0$$
که در آن $f(x)$ تابع مثلثی شکل زیر است: $f(x)=\dfrac kax$ برای $0\le x\le a$ و $f(x)=\dfrac k{a-\pi}(x-\pi)$ برای $a\le x\le\pi$.

::: {.solution}
$u_t(x,0)=g(x)=0\Rightarrow b_n=0$ و
$$u(x,t)=\sum_{n=1}^{\infty}a_n\cos nt\,\sin nx$$
$$\begin{aligned}
a_n&=\frac2\pi\int_0^\pi f(x)\sin nx\,dx=\frac2\pi\int_0^a\frac ka\,x\sin nx\,dx+\frac2\pi\int_a^\pi\frac k{a-\pi}(x-\pi)\sin nx\,dx\\
&=\frac{2k}{a\pi}\left[x\left(\frac{-1}n\cos nx\right)-(1)\left(\frac{-1}{n^2}\sin nx\right)\right]_0^a+\frac{2k}{(a-\pi)\pi}\left[(x-\pi)\left(\frac{-1}n\cos nx\right)-(1)\left(\frac{-1}{n^2}\sin nx\right)\right]_a^\pi\\
&=\cdots=\frac{2k\sin na}{an^2(\pi-a)}
\end{aligned}$$
$$u(x,t)=\frac{2k}{a(\pi-a)}\sum_{n=1}^{\infty}\frac{\sin na}{n^2}\cos nt\,\sin nx$$
:::
:::

```{.figure #m04-triangle caption="توزیع اولیهٔ مثلثی $f(x)$ با قلهٔ $k$ در $x=a$"}
```

::: {.example title="مثال ۳"}
جواب معادلهٔ موجی یک‌بعدی زیر را به‌دست آورید.
$$\frac{\partial^2u}{\partial t^2}=\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=u(\pi,t)=0,\qquad u(x,0)=kx(\pi-x),\qquad u_t(x,0)=0$$

::: {.solution}
$g(x)=0\Rightarrow b_n=0$ و
$$u(x,t)=\sum_{n=1}^{\infty}a_n\cos nt\,\sin nx$$
$$a_n=\frac2\pi\int_0^\pi kx(\pi-x)\sin nx\,dx=\frac{2k}\pi\Big[(-x^2+\pi x)\Big(\frac{-1}n\cos nx\Big)-(-2x+\pi)\Big(\frac{-1}{n^2}\sin nx\Big)+(-2)\Big(\frac1{n^3}\cos nx\Big)\Big]_0^\pi=\cdots=\frac{4k\big(1-(-1)^n\big)}{\pi n^3}$$
$$u(x,t)=\frac{4k}\pi\sum_{n=1}^{\infty}\frac{1-(-1)^n}{n^3}\cos nt\,\sin nx$$
:::
:::

```{.figure #m04-parabola caption="توزیع اولیهٔ سهمی‌شکل $f(x)=kx(\\pi-x)$"}
```

::: {.exercise}
(الف) مقدار نسبت $\dfrac{a_1^2}{a_1^2+a_2^2+\cdots}$ را به دست آورید.

(ب) نسبت $a_{2n-1}/a_{2n+1}$ را بر حسب $n\in\mathbb{N}$ رسم کنید.
:::

## روش جداسازی متغیرها: مثال‌ها

::: {.example title="مثال ۱"}
مطلوب است حل معادلهٔ دیفرانسیل مقابل به روش جداسازی متغیرها: $xu_x=yu_y$.

::: {.solution}
$$x\frac{\partial u}{\partial x}=y\frac{\partial u}{\partial y},\qquad u(x,y)=X(x)\cdot Y(y)$$
$$xX'Y=yXY'\ \Rightarrow\ \frac{xX'}X=\frac{yY'}Y=k$$
$$\frac{X'}X=\frac kx\ \Rightarrow\ \ln X=k\ln x+c_1\ \Rightarrow\ X(x)=C_1x^k,\qquad \frac{Y'}Y=\frac ky\ \Rightarrow\ \ln Y=k\ln y+c_2\ \Rightarrow\ Y(y)=C_2y^k$$
$$u(x,y)=X(x)Y(y)=C_1x^kC_2y^k=C(xy)^k$$
:::
:::

::: {.example title="مثال ۲"}
مطلوب است حل معادلهٔ دیفرانسیل مقابل به روش جداسازی متغیرها: $u_{xx}+u_{yy}=0$.

::: {.solution}
$$u(x,y)=X(x)\cdot Y(y)\ \Rightarrow\ X''Y+XY''=0\ \Rightarrow\ \frac{X''}X=-\frac{Y''}Y=k$$
$$\begin{cases}X''-kX=0\ \Rightarrow\ X(x)=Ae^{\sqrt kx}+Be^{-\sqrt kx}\\ Y''+kY=0\ \Rightarrow\ Y(y)=Ce^{\sqrt{-k}\,y}+De^{-\sqrt{-k}\,y}\end{cases}$$
$$u(x,y)=X(x)Y(y)=\big(Ae^{\sqrt kx}+Be^{-\sqrt kx}\big)\big(Ce^{\sqrt{-k}\,y}+De^{-\sqrt{-k}\,y}\big)$$
:::
:::

::: {.example title="مثال ۳"}
مطلوب است حل معادلهٔ دیفرانسیل مقابل به روش جداسازی متغیرها: $x^2u_{xy}=-3y^2u$.

::: {.solution}
$$x^2\frac{\partial^2u}{\partial x\partial y}+3y^2u=0,\qquad u(x,y)=X(x)\cdot Y(y)\ \Rightarrow\ x^2X'Y'+3y^2XY=0\ \Rightarrow\ \frac{x^2X'}X=\frac{-3y^2Y}{Y'}=k$$
$$\frac{X'}X=\frac k{x^2}\ \Rightarrow\ \ln X=\frac{-k}x+c_1\ \Rightarrow\ X(x)=C_1e^{-k/x}$$
$$\frac{Y'}Y=\frac{-3y^2}k\ \Rightarrow\ \ln Y=-\frac{y^3}k+c_2\ \Rightarrow\ Y(y)=C_2e^{-y^3/k}$$
$$u(x,y)=X(x)Y(y)=C_1e^{-k/x}\times C_2e^{-y^3/k}=Ce^{-(k/x+y^3/k)}$$
:::
:::

## معادلهٔ موجی یک‌بعدی با شرایط مرزی غیرصفر

::: {.example title="مسئله"}
جواب معادلهٔ دیفرانسیل موجی یک‌بعدی زیر را به‌دست آورید.
$$\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=P_0,\quad u(L,t)=P_1,\quad u(x,0)=f(x),\quad u_t(x,0)=g(x)$$

::: {.solution}
$$u(x,t)=w(x,t)+v(x)\quad\Longrightarrow\quad\begin{cases}w(0,t)+v(0)=P_0\\ w(L,t)+v(L)=P_1\end{cases}$$
$$\frac{\partial^2w}{\partial t^2}=c^2\left(\frac{\partial^2w}{\partial x^2}+\frac{\partial^2v}{\partial x^2}\right)$$
تابع $v(x)$ را چنان انتخاب می‌کنیم که مسئلهٔ $w$ شرایط مرزی همگن داشته باشد:
$$\begin{cases}\dfrac{\partial^2v}{\partial x^2}=0\\ v(0)=P_0\\ v(L)=P_1\end{cases}\quad\Longrightarrow\quad v(x)=\left(\frac{P_1-P_0}L\right)x+P_0$$
$$\begin{cases}\dfrac{\partial^2w}{\partial t^2}=c^2\dfrac{\partial^2w}{\partial x^2}\\ w(0,t)=w(L,t)=0\end{cases}\quad\Longrightarrow\quad w(x,t)=\sum_{n=1}^{\infty}\left[A_n\cos\!\left(\frac{cn\pi}Lt\right)+B_n\sin\!\left(\frac{cn\pi}Lt\right)\right]\sin\frac{n\pi}Lx$$
$$u(x,t)=\underbrace{\sum_{n=1}^{\infty}\left[A_n\cos\!\left(\frac{cn\pi}Lt\right)+B_n\sin\!\left(\frac{cn\pi}Lt\right)\right]\sin\frac{n\pi}Lx}_{w(x,t)}+\underbrace{\left(\frac{P_1-P_0}L\right)x+P_0}_{v(x)}$$
شرط اولیهٔ $u(x,0)=f(x)$:
$$\sum_{n=1}^{\infty}A_n\sin\frac{n\pi}Lx=f(x)-\left(\frac{P_1-P_0}L\right)x-P_0\triangleq f_1(x)$$
$$A_n=\frac2L\int_0^Lf_1(x)\sin\frac{n\pi}Lx\,dx=\frac2L\int_0^L\left[f(x)-\left(\frac{P_1-P_0}L\right)x-P_0\right]\sin\frac{n\pi}Lx\,dx$$
:::
:::

::: {.exercise}
$B_n$ را برای حالت (الف) $g(x)=0$ و (ب) $g(x)$ دلخواه به دست آورید.
:::

## معادلهٔ موجی یک‌بعدی با سرعت اولیهٔ صفر (امواج متحرک)

اگر سرعت اولیه صفر باشد ($g(x)=0$) آنگاه خواهیم داشت:
$$u(x,t)=\sum_{n=1}^{\infty}a_n\cos\!\left(\frac{cn\pi}Lt\right)\sin\frac{n\pi}Lx,\qquad u(x,0)=\sum_{n=1}^{\infty}a_n\sin\frac{n\pi}Lx=f(x)\equiv\tilde f(x)$$
با استفاده از $\sin\alpha\cos\beta=\frac12\big(\sin(\alpha+\beta)+\sin(\alpha-\beta)\big)$:
$$\begin{aligned}
u(x,t)&=\sum_{n=1}^{\infty}a_n\frac12\left[\sin\!\left(\frac{n\pi}Lx+\frac{cn\pi}Lt\right)+\sin\!\left(\frac{n\pi}Lx-\frac{cn\pi}Lt\right)\right]\\
&=\frac12\sum_{n=1}^{\infty}a_n\left[\sin\frac{n\pi}L(x+ct)+\sin\frac{n\pi}L(x-ct)\right]\\
&=\frac12\sum_{n=1}^{\infty}a_n\sin\frac{n\pi}L(x+ct)+\frac12\sum_{n=1}^{\infty}a_n\sin\frac{n\pi}L(x-ct)=\frac12\Big[\tilde f(x+ct)+\tilde f(x-ct)\Big]
\end{aligned}$$

::: {.important title="امواج متحرک"}
$$u(x,t)=\frac12\Big[\tilde f(x+ct)+\tilde f(x-ct)\Big]$$
$\tilde f$ ادامهٔ فرد و متناوب (با دورهٔ $2L$) تابع اولیهٔ $f$ است؛ جواب برهم‌نهی دو موج با نیمی از دامنهٔ اولیه است که با سرعت $c$ در دو جهت مخالف حرکت می‌کنند.
:::

```{.figure #m04-traveling caption="ادامهٔ فرد و متناوب $\\tilde f(x)$ و دو موج $\\frac12\\tilde f(x+ct)$ و $\\frac12\\tilde f(x-ct)$ که در دو جهت مخالف حرکت می‌کنند"}
```

::: {.example}
جواب معادلهٔ موجی یک‌بعدی زیر را با فرض سرعت اولیهٔ صفر در زمان‌های مختلف رسم کنید.
$$\frac{\partial^2u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2},\qquad u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x),\qquad u_t(x,0)=0$$
$$f(x)=\begin{cases}\dfrac{2k}Lx&0<x<\dfrac L2\\[7mm] \dfrac{2k}L(L-x)&\dfrac L2<x<L\end{cases}$$

::: {.solution}
با رسم $\frac12\tilde f(x+ct)$ و $\frac12\tilde f(x-ct)$ و جمع آنها در زمان‌های $t=0$، $t=L/5c$، $t=2L/5c$، $t=L/2c$ و $t=3L/5c$ شکل جواب به دست می‌آید.
:::
:::

```{.figure #m04-triangle-time caption="جواب مثال برای $t=0$، $L/5c$، $2L/5c$، $L/2c$ و $3L/5c$؛ در $t=L/2c$ شکل تار صاف است"}
```
