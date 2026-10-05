# توابع مختلط مقدماتی

توابع مقدماتی مختلط تعمیم توابع مقدماتی حقیقی‌اند (Elementary Complex Functions).

## تابع نمایی

تابع نمایی حقیقی $f(x)=e^x$ دارای خواص زیر است:

$$\begin{aligned}
&1)\quad f(x_1+x_2)=f(x_1)f(x_2)\qquad &&e^{x_1}e^{x_2}=e^{x_1+x_2}\\
&2)\quad \frac{d}{dx}f(x)=f(x)\qquad &&\frac{d}{dx}e^x=e^x\\
&3)\quad e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+\cdots
\end{aligned}$$

تابع نمایی مختلط را با الهام از خاصیت سوم تعریف می‌کنیم و سایر خواص را در مورد این تابع تحقیق می‌نمائیم.

::: {.definition title="تابع نمایی مختلط"}
$$w=e^z\triangleq1+z+\frac{z^2}{2!}+\cdots+\frac{z^n}{n!}+\cdots$$
:::

اگر در تعریف تابع نمایی مختلط به جای $z$ مقدار $z=iy$ قرار دهیم:

$$\begin{aligned}
e^{iy}&=1+iy+\frac1{2!}(iy)^2+\frac1{3!}(iy)^3+\cdots\\
&=1+iy-\frac1{2!}y^2-\frac{i}{3!}y^3+\frac1{4!}y^4+\frac{i}{5!}y^5+\cdots\\
&=\underbrace{\left(1-\frac1{2!}y^2+\frac1{4!}y^4+\cdots\right)}_{\cos y}+i\underbrace{\left(y-\frac1{3!}y^3+\frac1{5!}y^5+\cdots\right)}_{\sin y}=\cos y+i\sin y
\end{aligned}$$

::: {.important}
$$w=e^z=e^{x+iy}=e^xe^{iy}=e^x(\cos y+i\sin y)$$
:::

::: {.example}
آیا تابع $w=e^z$ تحلیلی است؟

::: {.solution}
$$u(x,y)=e^x\cos y,\qquad v(x,y)=e^x\sin y$$
$$\frac{\partial u}{\partial x}=e^x\cos y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=-e^x\sin y=-\frac{\partial v}{\partial x}\ \checkmark$$
چون شرایط کشی–ریمان در تمام صفحهٔ مختلط برقرار است، تابع $w=e^z$ در تمام صفحهٔ مختلط مشتق‌پذیر است.
:::
:::

::: {.example}
مشتق تابع $w=e^z$ را به‌دست آورید.

::: {.solution}
$$\frac{d}{dz}e^z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^z$$
:::
:::

::: {.important title="نکتهٔ مهم"}
از این پس می‌توانیم هر عدد مختلط را به صورت نمائی نمایش دهیم:
$$z=x+iy=|z|(\cos\theta+i\sin\theta)=|z|\,e^{i\theta}$$
:::

مشاهده می‌شود که:
$$e^{z+i2k\pi}=e^ze^{i2k\pi}=e^z\big[\cos(2k\pi)+i\sin(2k\pi)\big]=e^z$$
پس تابع $w=e^z$ در صفحهٔ اعداد مختلط تابعی متناوب با دورهٔ تناوب $i2\pi$ است.

```{.figure #m03-exp-strip caption="باند اصلی تابع نمایی: $-\\pi<y\\le\\pi$"}
```

## توابع مثلثاتی

$$e^{i\theta}=\cos\theta+i\sin\theta\quad\Longrightarrow\quad e^{-i\theta}=\cos\theta-i\sin\theta$$
$$\Longrightarrow\quad\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\qquad \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}$$

::: {.definition title="کسینوس و سینوس مختلط"}
$$\cos z\triangleq\frac{e^{iz}+e^{-iz}}{2},\qquad \sin z\triangleq\frac{e^{iz}-e^{-iz}}{2i}$$
:::

$$\begin{aligned}
\cos z&=\frac12\Big[e^{i(x+iy)}+e^{-i(x+iy)}\Big]=\frac12\Big[e^{ix}e^{-y}+e^{-ix}e^{y}\Big]\\
&=\frac12\Big[e^{-y}(\cos x+i\sin x)+e^{y}(\cos x-i\sin x)\Big]\\
&=\cos x\left(\frac{e^y+e^{-y}}{2}\right)-i\sin x\left(\frac{e^y-e^{-y}}{2}\right)\\
&=\cos x\cosh y-i\sin x\sinh y
\end{aligned}$$

$$\begin{aligned}
\sin z&=\frac1{2i}\Big[e^{i(x+iy)}-e^{-i(x+iy)}\Big]=\frac1{2i}\Big[e^{ix}e^{-y}-e^{-ix}e^{y}\Big]\\
&=\frac1{2i}\Big[e^{-y}(\cos x+i\sin x)-e^{y}(\cos x-i\sin x)\Big]\\
&=\sin x\left(\frac{e^y+e^{-y}}{2}\right)+i\cos x\left(\frac{e^y-e^{-y}}{2}\right)\\
&=\sin x\cosh y+i\cos x\sinh y
\end{aligned}$$

### تحلیلی بودن و مشتق‌پذیری $\cos z$

$$\cos z=u(x,y)+iv(x,y)=\cos x\cosh y-i\sin x\sinh y,\qquad u=\cos x\cosh y,\quad v=-\sin x\sinh y$$
$$\frac{\partial u}{\partial x}=-\sin x\cosh y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\cos x\sinh y=-\frac{\partial v}{\partial x}\ \checkmark$$
پس این تابع در همهٔ صفحهٔ مختلط تحلیلی است. مشتق این تابع را توسط یکی از روش‌های ذکر شده به‌دست می‌آوریم:
$$f'(z)=\frac{d}{dz}\cos z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=-\sin x\cosh y-i\cos x\sinh y=-\sin z$$

### تحلیلی بودن و مشتق‌پذیری $\sin z$

$$\sin z=u(x,y)+iv(x,y)=\sin x\cosh y+i\cos x\sinh y,\qquad u=\sin x\cosh y,\quad v=\cos x\sinh y$$
$$\frac{\partial u}{\partial x}=\cos x\cosh y=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\sin x\sinh y=-\frac{\partial v}{\partial x}\ \checkmark$$
پس این تابع در همهٔ صفحهٔ مختلط تحلیلی است و
$$f'(z)=\frac{d}{dz}\sin z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\cos x\cosh y-i\sin x\sinh y=\cos z$$

::: {.important}
$$(\sin z)'=\cos z,\qquad (\cos z)'=-\sin z$$
:::

### بی‌کرانی $\sin z$ و $\cos z$

$$|\cos z|=\sqrt{\cos^2x\cosh^2y+\sin^2x\sinh^2y}=\sqrt{\cos^2x+\sinh^2y},\qquad(\cosh^2y=1+\sinh^2y,\ \ \sin^2x=1-\cos^2x)$$
$$|\sin z|=\sqrt{\sin^2x\cosh^2y+\cos^2x\sinh^2y}=\sqrt{\sin^2x+\sinh^2y},\qquad(\cosh^2y=1+\sinh^2y,\ \ \cos^2x=1-\sin^2x)$$

از آنجائی که $\sinh y$ تابعی بی‌کران است، پس توابع $\cos z$ و $\sin z$ توابعی **بی‌کران** خواهند بود.

### تناوب

$$\begin{aligned}
\cos(z+2\pi)&=\cos(x+iy+2\pi)=\cos(x+2\pi)\cosh y-i\sin(x+2\pi)\sinh y\\
&=\cos x\cosh y-i\sin x\sinh y=\cos z
\end{aligned}$$
به همین ترتیب $\sin(z+2\pi)=\sin z$.

```{.figure #m03-trig-strip caption="باند اصلی توابع $\\sin z$ و $\\cos z$: $-\\pi<x\\le\\pi$"}
```

### نکته

$$\cos(iy)=\cosh y,\qquad \sin(iy)=i\sinh y$$
$$\cos(x+iy)=\cos x\cos(iy)-\sin x\sin(iy)=\cos x\cosh y-i\sin x\sinh y$$
$$\sin(x+iy)=\sin x\cos(iy)+\cos x\sin(iy)=\sin x\cosh y+i\cos x\sinh y$$

سایر توابع مثلثاتی:
$$\tan z\triangleq\frac{\sin z}{\cos z},\qquad \cot z\triangleq\frac{\cos z}{\sin z},\qquad \sec z\triangleq\frac1{\cos z},\qquad \csc z\triangleq\frac1{\sin z}$$
$$(\tan z)'=\sec^2z,\quad\dots$$

## توابع هذلولی‌گون

$$\cosh z\triangleq\frac{e^z+e^{-z}}{2},\qquad \sinh z\triangleq\frac{e^z-e^{-z}}{2},\qquad e^z=e^x(\cos y+i\sin y)$$

::: {.exercise}
تحقیق کنید:
$$\cosh z=\cosh x\cos y+i\sinh x\sin y,\qquad \sinh z=\sinh x\cos y+i\cosh x\sin y$$
:::

::: {.exercise}
تحقیق کنید توابع $\cosh z$ و $\sinh z$ در تمام صفحهٔ مختلط تحلیلی‌اند و مشتق آنها از طریق روابط زیر به دست می‌آید:
$$(\cosh z)'=\sinh z,\qquad (\sinh z)'=\cosh z$$
:::

$$\tanh z=\frac{\sinh z}{\cosh z},\quad \coth z=\frac{\cosh z}{\sinh z},\quad \operatorname{sech}z=\frac1{\cosh z},\quad \operatorname{csch}z=\frac1{\sinh z}$$

$$\cosh(z+i2\pi)=\cosh(z),\qquad \sinh(z+i2\pi)=\sinh(z)$$

```{.figure #m03-hyp-strip caption="باند اصلی توابع هذلولی‌گون: $-\\pi<y\\le\\pi$"}
```

## تابع لگاریتم

$$w=\ln z,\qquad z=|z|e^{i\arg z}=e^w=e^{\ln|z|}e^{i\arg z}$$
$$w=\ln z=\ln|z|+i\arg z=\ln\!\big(x^2+y^2\big)^{1/2}+i\tan^{-1}\frac yx$$
$$u(x,y)=\frac12\ln\!\big(x^2+y^2\big),\qquad v(x,y)=\tan^{-1}\frac yx$$
$$\frac{\partial u}{\partial x}=\frac{x}{x^2+y^2}=\frac{\partial v}{\partial y}\ \checkmark\qquad\qquad \frac{\partial u}{\partial y}=\frac{y}{x^2+y^2}=-\frac{\partial v}{\partial x}\ \checkmark$$

بنابراین تابع لگاریتم در تمام صفحهٔ مختلط بجز مبدأ تحلیلی است.

$$\frac{d}{dz}\ln z=\frac{\partial u}{\partial x}+i\,\frac{\partial v}{\partial x}=\frac{x}{x^2+y^2}+i\,\frac{-y}{x^2+y^2}=\frac{\bar z}{z\bar z}=\frac1z$$

$$z=re^{i\theta}=re^{i(\theta+2k\pi)}$$

برای آنکه تعریف تابع نقض نشود برد این تابع ناحیهٔ نشان داده شده در شکل است.

```{.figure #m03-log-range caption="برد تابع لگاریتم: نوار $-\\pi<\\operatorname{Im}w\\le\\pi$"}
```

خواص زیر برای تابع لگاریتم برقرارند:
$$\ln(z_1\times z_2)=\ln z_1+\ln z_2,\qquad \ln\!\left(\frac{z_1}{z_2}\right)=\ln z_1-\ln z_2,\qquad \ln(z^c)=c\ln z$$
