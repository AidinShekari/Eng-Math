# تبدیل لاپلاس

## تبدیل لاپلاس یک‌طرفه

::: {.definition title="تبدیل لاپلاس یک‌طرفه"}
$$F(s)=\mathcal{L}\{f(t)\}\triangleq\int_0^\infty f(t)\,e^{-st}\,dt\qquad\Longleftrightarrow\qquad f(t)=\mathcal{L}^{-1}\{F(s)\}$$
:::

تبدیل لاپلاس یکی از ابزارهای مهم در کاربردهای مختلف مهندسی و ریاضی است. یکی از کاربردهای تبدیل لاپلاس حل معادلات دیفرانسیل است (فصل ۶ کتاب مرجع درس را مطالعه فرمایید).

تبدیل لاپلاس یک عملگر خطی است:
$$\mathcal{L}\{af(t)+bg(t)\}=a\,\mathcal{L}\{f(t)\}+b\,\mathcal{L}\{g(t)\}$$

::: {.example title="مثال ۱"}
$$f(t)=\begin{cases}1&t\ge0\\ 0&t<0\end{cases}\ \Longrightarrow\ \mathcal{L}\{f(t)\}=F(s)=\;?$$

::: {.solution}
$$\mathcal{L}\{f(t)\}=\int_0^\infty1\times e^{-st}\,dt=-\frac1se^{-st}\Big|_0^\infty=\frac1s$$
:::
:::

::: {.example title="مثال ۲"}
$$f(t)=\begin{cases}e^{at}&t\ge0\\ 0&t<0\end{cases}\ \Longrightarrow\ \mathcal{L}\{f(t)\}=F(s)=\;?$$

::: {.solution}
$$\mathcal{L}\{f(t)\}=\int_0^\infty e^{at}\times e^{-st}\,dt=\int_0^\infty e^{-(s-a)t}\,dt=-\frac1{s-a}e^{-(s-a)t}\Big|_0^\infty=\frac1{s-a}$$
:::
:::

::: {.example title="مثال ۳"}
::: {.solution}
$$\mathcal{L}\{\cosh(at)\}=\mathcal{L}\left\{\tfrac12e^{at}+\tfrac12e^{-at}\right\}=\tfrac12\mathcal{L}\{e^{at}\}+\tfrac12\mathcal{L}\{e^{-at}\}=\frac12\frac1{s-a}+\frac12\frac1{s+a}=\frac s{s^2-a^2}$$
:::
:::

::: {.example title="مثال ۴"}
::: {.solution}
$$\mathcal{L}\{\sinh(at)\}=\mathcal{L}\left\{\tfrac12e^{at}-\tfrac12e^{-at}\right\}=\tfrac12\mathcal{L}\{e^{at}\}-\tfrac12\mathcal{L}\{e^{-at}\}=\frac12\frac1{s-a}-\frac12\frac1{s+a}=\frac a{s^2-a^2}$$
:::
:::

::: {.example title="مثال ۵"}
::: {.solution}
با استفاده از $\displaystyle\int e^{ax}\cos nx\,dx=\frac{e^{ax}}{a^2+n^2}\big(a\cos nx+n\sin nx\big)$:
$$\mathcal{L}\{\cos\omega t\}=\int_0^\infty\cos\omega t\,e^{-st}\,dt=\frac{e^{-st}}{s^2+\omega^2}\big(-s\cos\omega t+\omega\sin\omega t\big)\Big|_0^\infty=\frac s{s^2+\omega^2}$$
:::
:::

::: {.example title="مثال ۶"}
::: {.solution}
با استفاده از $\displaystyle\int e^{ax}\sin nx\,dx=\frac{e^{ax}}{a^2+n^2}\big(a\sin nx-n\cos nx\big)$:
$$\mathcal{L}\{\sin\omega t\}=\int_0^\infty\sin\omega t\,e^{-st}\,dt=\frac{e^{-st}}{s^2+\omega^2}\big(-s\sin\omega t-\omega\cos\omega t\big)\Big|_0^\infty=\frac\omega{s^2+\omega^2}$$
:::
:::

### جدول تبدیل‌های لاپلاس (جدول ۶٫۱ کتاب؛ جدول مفصل‌تر در فصل ۶٫۹ کتاب)

| | $f(t)$ | $\mathcal{L}(f)$ | | | $f(t)$ | $\mathcal{L}(f)$ |
|:---:|:---:|:---:|---|:---:|:---:|:---:|
| 1 | $1$ | $1/s$ | | 7 | $\cos\omega t$ | $\dfrac{s}{s^2+\omega^2}$ |
| 2 | $t$ | $1/s^2$ | | 8 | $\sin\omega t$ | $\dfrac{\omega}{s^2+\omega^2}$ |
| 3 | $t^2$ | $2!/s^3$ | | 9 | $\cosh at$ | $\dfrac{s}{s^2-a^2}$ |
| 4 | $t^n$ $(n=0,1,\dots)$ | $\dfrac{n!}{s^{n+1}}$ | | 10 | $\sinh at$ | $\dfrac{a}{s^2-a^2}$ |
| 5 | $t^a$ ($a$ مثبت) | $\dfrac{\Gamma(a+1)}{s^{a+1}}$ | | 11 | $e^{at}\cos\omega t$ | $\dfrac{s-a}{(s-a)^2+\omega^2}$ |
| 6 | $e^{at}$ | $\dfrac1{s-a}$ | | 12 | $e^{at}\sin\omega t$ | $\dfrac{\omega}{(s-a)^2+\omega^2}$ |

$$\Gamma(x)=\int_0^\infty e^{-t}t^{x-1}\,dt$$

### خواص تبدیل لاپلاس یک‌طرفه (جدول فصل ۶٫۸ کتاب)

با تعریف تابع پلهٔ واحد
$$u(t)\triangleq\begin{cases}1&t\ge0\\ 0&t<0\end{cases}$$

| عنوان خاصیت | خاصیت |
|:---|:---:|
| تعریف تبدیل لاپلاس | $F(s)=\mathcal{L}\{f(t)\}\triangleq\displaystyle\int_0^\infty f(t)e^{-st}\,dt$ |
| معکوس تبدیل لاپلاس | $f(t)=\mathcal{L}^{-1}\{F(s)\}$ |
| خطی بودن | $\mathcal{L}\{af(t)+bg(t)\}=a\mathcal{L}\{f(t)\}+b\mathcal{L}\{g(t)\}$ |
| شیفت زمانی | $\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$ |
| شیفت در حوزهٔ $s$ | $\mathcal{L}\{e^{at}f(t)\}=F(s-a)$ |
| تغییر مقیاس زمانی | $\mathcal{L}\{f(at)\}=\dfrac1aF(s/a)$ |
| مشتق زمانی | $\mathcal{L}\{f^{(n)}(t)\}=s^nF(s)-s^{n-1}f(0)-s^{n-2}f^{(1)}(0)-\cdots-f^{(n-1)}(0)$ |
| انتگرال زمانی | $\mathcal{L}\left\{\displaystyle\int_0^tf(\tau)\,d\tau\right\}=\dfrac1sF(s)$ |
| مشتق در حوزهٔ $s$ | $\mathcal{L}\{tf(t)\}=-F'(s)$ |
| انتگرال در حوزهٔ $s$ | $\mathcal{L}\left\{\dfrac{f(t)}t\right\}=\displaystyle\int_s^\infty F(\nu)\,d\nu$ |

## استفاده از تبدیل لاپلاس در حل معادلات دیفرانسیل

مراحل حل یک معادلهٔ دیفرانسیل با شرایط اولیه با استفاده از تبدیل لاپلاس:

1. تبدیل مسئلهٔ مقدار اولیه به یک مسئلهٔ جبری؛
2. محاسبهٔ جواب مسئلهٔ جبری؛
3. حل مسئلهٔ مقدار اولیه (بازگرداندن جواب به حوزهٔ زمان).

```{.figure #m14-solve-scheme caption="مراحل حل مسئلهٔ مقدار اولیه با تبدیل لاپلاس: مسئلهٔ مقدار اولیه $\\xrightarrow{1}$ مسئلهٔ جبری $\\xrightarrow{2}$ جواب مسئلهٔ جبری $\\xrightarrow{3}$ جواب مسئلهٔ مقدار اولیه"}
```

### معادلات دیفرانسیل معمولی

::: {.example}
معادلهٔ دیفرانسیل $y''-y=t$، $y(0)=1$، $y'(0)=1$ را با استفاده از تبدیل لاپلاس حل کنید.

::: {.solution}
$$s^2Y-sy(0)-y'(0)-Y=\frac1{s^2}\ \Longrightarrow\ (s^2-1)Y(s)=s+1+\frac1{s^2}$$
$$Y(s)=\frac{s+1}{s^2-1}+\frac1{s^2(s^2-1)}=\frac1{s-1}+\left(\frac1{s^2-1}-\frac1{s^2}\right)$$
$$y(t)=\mathcal{L}^{-1}\{Y(s)\}=\mathcal{L}^{-1}\left\{\frac1{s-1}\right\}+\mathcal{L}^{-1}\left\{\frac1{s^2-1}\right\}-\mathcal{L}^{-1}\left\{\frac1{s^2}\right\}=e^tu(t)+\sinh t\,u(t)-t\,u(t)$$
:::
:::

### معادلات دیفرانسیل با مشتقات جزئی

::: {.example}
معادلهٔ دیفرانسیل با مشتقات جزئی زیر را با استفاده از تبدیل لاپلاس حل کنید.
$$\frac{\partial w}{\partial x}+x\frac{\partial w}{\partial t}=0,\qquad w(x,0)=0,\qquad w(0,t)=t\,u(t)$$

::: {.solution}
از طرفین نسبت به $t$ تبدیل لاپلاس می‌گیریم:
$$\mathcal{L}_t\left\{\frac{\partial w}{\partial x}+x\frac{\partial w}{\partial t}\right\}=\mathcal{L}_t\left\{\frac{\partial w}{\partial x}\right\}+x\,\mathcal{L}_t\left\{\frac{\partial w}{\partial t}\right\}=0$$
$$\frac\partial{\partial x}w(x,s)+x\big[s\,w(x,s)-w(x,0)\big]=0,\qquad w(x,0)=0$$
$$\frac\partial{\partial x}w(x,s)+xs\,w(x,s)=0\ \Rightarrow\ \frac{dw}w=-sx\,dx\ \Rightarrow\ \ln w=-s\frac{x^2}2+\ln C\ \Rightarrow\ w(x,s)=Ce^{-\frac{x^2}2s}$$
از شرط $w(0,t)=t\,u(t)$ داریم $w(0,s)=\mathcal{L}\{w(0,t)\}=1/s^2=C$:
$$w(x,s)=\frac1{s^2}e^{-\frac{x^2}2s}$$
با استفاده از خاصیت شیفت زمانی $\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$:
$$w(x,t)=\left(t-\frac{x^2}2\right)\times u\!\left(t-\frac{x^2}2\right)$$
:::
:::
