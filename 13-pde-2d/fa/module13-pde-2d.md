# معادلات دو‌بعدی موج و گرما: مستطیل و دایره

## معادلهٔ موجی دو‌بعدی

مدلسازی یک غشاء مرتعش (به‌دست آوردن معادلهٔ حاکم بر $u(x,y,t)$).

**فرضیات فیزیکی:**

- جرم به صورت یکنواخت در طول غشاء توزیع شده (غشاء همگن)، کاملاً انعطاف‌پذیر است.
- غشاء چنان محکم کشیده شده‌است که نیروی جاذبه در آن قابل چشم‌پوشی است.
- میزان انحراف غشاء از حالت تعادل بسیار کوچک است.

```{.figure #m13-membrane caption="المان $\\Delta x\\times\\Delta y$ از غشاء مرتعش و نیروهای کششی $T\\Delta x$ و $T\\Delta y$ وارد بر آن"}
```

با فرایند مدلسازی مشابه حالت یک‌بعدی، معادلهٔ ارتعاش غشاء دوبعدی به دست می‌آید:
$$\frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)=c^2\nabla^2u$$
برای حل یکتای این معادله نیاز به شرایط مرزی و شرایط اولیه داریم:

- شرایط مرزی: $u(x,y,t)=0$ روی مرزهای غشاء
- شرایط اولیه: $u(x,y,0)=f(x,y)$ و $u_t(x,y,0)=g(x,y)$، که در آن $u_t\triangleq\dfrac{\partial u}{\partial t}$

## معادلهٔ موجی دو‌بعدی با شرایط مرزی مستطیل

```{.figure #m13-rectangle caption="ناحیهٔ مستطیلی $0\\le x\\le a$، $0\\le y\\le b$"}
```

$$\frac{\partial^2u}{\partial t^2}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)$$

- شرایط مرزی: $u(0,y,t)=u(a,y,t)=0$ و $u(x,0,t)=u(x,b,t)=0$
- شرایط اولیه: $u(x,y,0)=f(x,y)$ و $u_t(x,y,0)=g(x,y)$

### حل معادله

در اینجا برای حل این معادله از روش **جداسازی متغیرها** استفاده می‌کنیم. فرض: $u(x,y,t)=X(x)\times Y(y)\times T(t)$.
$$\frac{\partial^2u}{\partial x^2}=X''YT,\qquad\frac{\partial^2u}{\partial y^2}=XY''T,\qquad\frac{\partial^2u}{\partial t^2}=XYT''\quad\Longrightarrow\quad XYT''=c^2\big(X''YT+XY''T\big)$$
$$\frac{T''}{c^2T}=\frac{X''}X+\frac{Y''}Y=-\lambda^2\ \Rightarrow\ \frac{Y''}Y=-\lambda^2-\frac{X''}X=-\rho^2\ \Rightarrow\ \frac{X''}X=-\lambda^2+\rho^2=-\mu^2$$
$$\begin{cases}X''+\mu^2X=0\\ Y''+\rho^2Y=0\\ T''+c^2\lambda^2T=0\end{cases}\qquad\lambda^2=\mu^2+\rho^2$$
**جواب در راستای $x$:**
$$X(x)=A_1\cos\mu x+A_2\sin\mu x,\quad X(0)=0\Rightarrow A_1=0,\quad X(a)=0\Rightarrow A_2\sin\mu a=0\Rightarrow\mu a=n\pi\Rightarrow\mu_n=\frac{n\pi}a$$
$$X_n(x)=A_n\sin\mu_nx,\qquad \mu_n=\frac{n\pi}a$$
**جواب در راستای $y$:**
$$Y(y)=B_1\cos\rho y+B_2\sin\rho y,\quad Y(0)=0\Rightarrow B_1=0,\quad Y(b)=0\Rightarrow B_2\sin\rho b=0\Rightarrow\rho b=m\pi\Rightarrow\rho_m=\frac{m\pi}b$$
$$Y_m(y)=B_m\sin\rho_my,\qquad \rho_m=\frac{m\pi}b$$
**جواب در راستای زمان:**
$$\lambda_{nm}^2=\mu_n^2+\rho_m^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2,\qquad T_{nm}(t)=C_1\cos(c\lambda_{nm}t)+C_2\sin(c\lambda_{nm}t)$$
$$u_{nm}(x,y,t)=\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right),\qquad n,m=1,2,\dots$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)$$

**اعمال شرط اولیه $u(x,y,0)=f(x,y)$:**
$$f(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)=\sum_{n=1}^{\infty}K_n(y)\sin\frac{n\pi}ax,\qquad K_n(y)\triangleq\sum_{m=1}^{\infty}A_{nm}\sin\frac{m\pi}by$$
$$K_n(y)=\frac2a\int_0^af(x,y)\sin\frac{n\pi}ax\,dx,\qquad A_{nm}=\frac2b\int_0^bK_n(y)\sin\frac{m\pi}by\,dy$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$

::: {.exercise}
ثابت کنید:
$$B_{nm}=\frac4{abc\lambda_{nm}}\int_0^b\left\{\int_0^ag(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$
:::

::: {.important title="جواب معادلهٔ موجی دو‌بعدی در مستطیل"}
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\big[A_{nm}\cos(c\lambda_{nm}t)+B_{nm}\sin(c\lambda_{nm}t)\big]\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right),\qquad\lambda_{nm}^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy,\qquad B_{nm}=\frac4{abc\lambda_{nm}}\int_0^b\left\{\int_0^ag(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$
:::

::: {.example}
مطلوب است جواب معادلهٔ حرکت دو‌بعدی بالا با فرض $g(x,y)=0$ و $f(x,y)=xy$.

::: {.solution}
$$g(x,y)=0\ \Rightarrow\ B_{nm}=0$$
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^axy\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy=\frac4{ab}\left\{\left[\int_0^by\sin\frac{m\pi}by\,dy\right]\times\left[\int_0^ax\sin\frac{n\pi}ax\,dx\right]\right\}$$
$$=\frac4{ab}\left[y\left(\frac{-b}{m\pi}\cos\frac{m\pi}by\right)-(1)\left(\frac{-b^2}{m^2\pi^2}\sin\frac{m\pi}by\right)\right]_0^b\times\left[x\left(\frac{-a}{n\pi}\cos\frac{n\pi}ax\right)-(1)\left(\frac{-a^2}{n^2\pi^2}\sin\frac{n\pi}ax\right)\right]_0^a$$
$$=\frac4{ab}\cdot\frac{-b^2}{m\pi}(-1)^m\cdot\frac{-a^2}{n\pi}(-1)^n=\frac{4ab}{nm\pi^2}(-1)^{n+m}$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\frac{4ab}{nm\pi^2}(-1)^{n+m}\cos(c\lambda_{nm}t)\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)$$
:::
:::

## معادلهٔ گرمای دو‌بعدی با شرایط مرزی مستطیل

$$\frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)=c^2\nabla^2u$$

- شرط مرزی: $u(x,y,t)=0$ روی مرزهای غشاء
- شرط اولیه: $u(x,y,0)=f(x,y)$

### حل معادله

فرض: $u(x,y,t)=X(x)\times Y(y)\times T(t)$.
$$\frac{\partial^2u}{\partial x^2}=X''YT,\qquad\frac{\partial^2u}{\partial y^2}=XY''T,\qquad\frac{\partial u}{\partial t}=XYT'\quad\Longrightarrow\quad XYT'=c^2\big(X''YT+XY''T\big)$$
$$\frac{T'}{c^2T}=\frac{X''}X+\frac{Y''}Y=-\lambda^2,\qquad \frac{Y''}Y=-\lambda^2-\frac{X''}X=-\rho^2,\qquad\frac{X''}X=-\lambda^2+\rho^2=-\mu^2$$
$$\begin{cases}X''+\mu^2X=0\\ Y''+\rho^2Y=0\\ T'+c^2\lambda^2T=0\end{cases}\qquad\lambda^2=\mu^2+\rho^2$$
مشابه حالت موجی ($X_n(x)=A_n\sin\mu_nx$ با $\mu_n=n\pi/a$ و $Y_m(y)=B_m\sin\rho_my$ با $\rho_m=m\pi/b$) و با
$$T_{nm}(t)=C_1e^{-c^2\lambda_{nm}^2t},\qquad\lambda_{nm}^2=\mu_n^2+\rho_m^2=\left(\frac{n\pi}a\right)^2+\left(\frac{m\pi}b\right)^2$$
$$u_{nm}(x,y,t)=A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)e^{-c^2\lambda_{nm}^2t},\qquad n=1,2,\dots,\ m=1,2,\dots$$
$$u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}A_{nm}\sin\!\left(\frac{n\pi}ax\right)\sin\!\left(\frac{m\pi}by\right)e^{-c^2\lambda_{nm}^2t}$$
**اعمال شرط اولیه:** دقیقاً مانند حالت موجی
$$A_{nm}=\frac4{ab}\int_0^b\left\{\int_0^af(x,y)\sin\frac{n\pi}ax\,dx\right\}\sin\frac{m\pi}by\,dy$$

## بیان لاپلاسین در مختصات قطبی

هدف آن است که $\nabla^2u=u_{xx}+u_{yy}$ در مختصات قطبی بر حسب $r,\theta$ نوشته شود.

```{.figure #m13-polar caption="مختصات قطبی: $x=r\\cos\\theta$، $y=r\\sin\\theta$"}
```

$$r=\sqrt{x^2+y^2},\quad x=r\cos\theta,\qquad\theta=\tan^{-1}\!\left(\frac yx\right),\quad y=r\sin\theta$$
$$u_x=u_rr_x+u_\theta\theta_x\ \Rightarrow\ u_{xx}=\big(u_rr_x+u_\theta\theta_x\big)_x=u_{rr}r_x^2+u_{\theta\theta}\theta_x^2+2r_x\theta_xu_{r\theta}+r_{xx}u_r+\theta_{xx}u_\theta$$
$$u_y=u_rr_y+u_\theta\theta_y\ \Rightarrow\ u_{yy}=u_{rr}r_y^2+u_{\theta\theta}\theta_y^2+2r_y\theta_yu_{r\theta}+r_{yy}u_r+\theta_{yy}u_\theta$$
$$r_x=\frac xr,\quad r_{xx}=\frac{y^2}{r^3},\quad\theta_x=\frac{-y}{r^2},\quad\theta_{xx}=\frac{2xy}{r^4},\qquad r_y=\frac yr,\quad r_{yy}=\frac{x^2}{r^3},\quad\theta_y=\frac x{r^2},\quad\theta_{yy}=\frac{-2xy}{r^4}$$
$$u_{xx}=\frac{x^2}{r^2}u_{rr}+\frac{y^2}{r^4}u_{\theta\theta}+\frac{-2xy}{r^3}u_{r\theta}+\frac{y^2}{r^3}u_r+\frac{2xy}{r^4}u_\theta$$
$$u_{yy}=\frac{y^2}{r^2}u_{rr}+\frac{x^2}{r^4}u_{\theta\theta}+\frac{2xy}{r^3}u_{r\theta}+\frac{x^2}{r^3}u_r+\frac{-2xy}{r^4}u_\theta$$
با جمع این دو رابطه:

::: {.important title="لاپلاسین در مختصات قطبی"}
$$\nabla^2u=u_{rr}+\frac1{r^2}u_{\theta\theta}+\frac1ru_r$$
:::

## معادلهٔ موجی دو‌بعدی با شرایط مرزی دایره

```{.figure #m13-disc caption="غشاء دایره‌ای به شعاع $R$"}
```

$$\frac{\partial^2u}{\partial t^2}=c^2\nabla^2u,\qquad u(R,t)=0\ \ \text{(شرط مرزی)},\qquad u(r,0)=f(r),\ \ u_t(r,0)=g(r)\ \ \text{(شرایط اولیه)}$$

### حل معادله

با توجه به تقارن دایروی در این مسئله، بهتر است آن را در مختصات قطبی حل کنیم. بر روی غشاء دایروی، ارتعاش تابعی از $\theta$ نیست، لذا داریم:
$$\begin{cases}\dfrac{\partial^2u}{\partial t^2}=c^2\left(u_{rr}+\dfrac1ru_r\right)\\[2mm] u(R,t)=0,\quad u(r,0)=f(r),\quad u_t(r,0)=g(r)\end{cases}$$
حال با فرض تفکیک‌پذیری متغیرها $u(r,t)=P(r)\times T(t)$ داریم:
$$PT''=c^2\left(P''T+\frac1rP'T\right)\ \Rightarrow\ \frac{T''}{c^2T}=\frac{P''}P+\frac1r\frac{P'}P=-\lambda^2\ \Rightarrow\ \begin{cases}P''+\dfrac1rP'+\lambda^2P=0\\[1mm] T''+c^2\lambda^2T=0\end{cases}$$

### معادلهٔ دیفرانسیل بسل از مرتبهٔ $n$

$$y''+\frac1xy'+\left(1-\frac{n^2}{x^2}\right)y=0\quad\Longrightarrow\quad y(x)=AJ_n(x)+BY_n(x)$$
که در آن $J_n$ توابع بسل نوع اول و از مرتبهٔ $n$ و $Y_n$ توابع بسل نوع دوم و از مرتبهٔ $n$ هستند.

```{.figure #m13-bessel caption="توابع بسل نوع اول $J_0,\\dots,J_4$ و نوع دوم $Y_0,\\dots,Y_4$ برای $0<x\\le10$"}
```

با تغییر متغیر $s=\lambda r$:
$$P'=\frac{dP}{dr}=\frac{dP}{ds}\frac{ds}{dr}=\lambda\frac{dP}{ds},\qquad P''=\lambda^2\frac{d^2P}{ds^2},\qquad\frac1r\lambda=\frac{\lambda^2}s$$
$$\lambda^2\frac{d^2P}{ds^2}+\frac1r\lambda\frac{dP}{ds}+\lambda^2P=0\ \Rightarrow\ \frac{d^2P}{ds^2}+\frac1s\frac{dP}{ds}+P=0$$
این معادلهٔ دیفرانسیل بسل از مرتبهٔ صفر است ($n=0$)، پس:
$$P(r)=AJ_0(\lambda r)+BY_0(\lambda r)$$
**اعمال شرایط مرزی:**

- چون $P(0)\neq\infty$ و $Y_0$ در مبدأ بی‌کران است: $D=0$ (ضریب $Y_0$ صفر است) و $P(r)=CJ_0(\lambda r)$.
- $P(R)=0$ نتیجه می‌دهد $J_0(\lambda R)=0$، یعنی $\lambda R=\alpha_m$ که در آن $\alpha_m$ ریشه‌های $J_0$ هستند:
$$\lambda=\lambda_m=\frac{\alpha_m}R,\quad m=1,2,\dots\quad\Longrightarrow\quad P_m(r)=C_mJ_0\!\left(\frac{\alpha_m}Rr\right)$$

```{.figure #m13-j0-zeros caption="تابع $J_0(x)$ و ریشه‌های آن $\\alpha_1,\\alpha_2,\\alpha_3$"}
```

$$T''+c^2\lambda_m^2T=0\ \Rightarrow\ T_m(t)=A_m\cos(c\lambda_mt)+B_m\sin(c\lambda_mt)$$

::: {.important title="جواب معادلهٔ موجی دو‌بعدی در دایره"}
$$u(r,t)=\sum_{m=1}^{\infty}\big(A_m\cos(c\lambda_mt)+B_m\sin(c\lambda_mt)\big)J_0\!\left(\frac{\alpha_m}Rr\right),\qquad\lambda_m=\frac{\alpha_m}R$$
:::

::: {.remark title="تحقیق (تا ۱ نمرهٔ اضافه)"}
گزارشی کامل از معادلهٔ دیفرانسیل بسل از مرتبهٔ $n$ و توابع بسل نوع اول و دوم و خواص آنها و نیز حل کامل معادلهٔ دیفرانسیل موجی دوبعدی با شرایط مرزی دایره تهیه کنید (گزارش تایپ شده و در فرمت Word باشد).
:::
