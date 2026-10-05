# اعداد مختلط

## مجموعهٔ اعداد مختلط

::: {.definition title="اعداد مختلط"}
مجموعهٔ اعداد مختلط تعمیم اعداد واقع بر محور اعداد حقیقی به صفحه‌ای از اعداد دارای دو مولفهٔ حقیقی و موهومی می‌باشد.
$$\mathbb{R}\to\mathbb{C}$$
:::

$$\mathbb{C}=\{(x,y)\mid x,y\in\mathbb{R}\},\qquad z=(x,y),\qquad x=\operatorname{Re}\{z\},\qquad y=\operatorname{Im}\{z\}$$

```{.figure #m08-complex-plane caption="نمایش عدد مختلط $z=(x,y)$ در صفحهٔ مختلط؛ اندازهٔ $|z|$ و آرگومان $\\theta$"}
```

اندازه یا نرم (norm) عدد مختلط:
$$|z|=\sqrt{x^2+y^2}$$

فاز یا آرگومان:
$$\theta=\measuredangle z=\tan^{-1}\!\left(\frac{y}{x}\right),\qquad z=|z|\measuredangle\theta$$
$$x=|z|\cos\theta,\qquad y=|z|\sin\theta$$

$$z=x\times(1,0)+y\times(0,1)=x+iy$$

::: {.important}
$$i^2=-1$$
:::

## چهار عمل اصلی

فرض کنید $z_1=(a_1,b_1)=a_1+ib_1$ و $z_2=(a_2,b_2)=a_2+ib_2$.

**(I) جمع:**
$$z_1+z_2=(a_1+a_2,\,b_1+b_2)=a_1+a_2+i(b_1+b_2)$$

**(II) تفریق:**
$$z_1-z_2=(a_1-a_2,\,b_1-b_2)=a_1-a_2+i(b_1-b_2)$$

**(III) ضرب:**
$$\begin{aligned}
z_1\times z_2&=(a_1+ib_1)\times(a_2+ib_2)\\
&=a_1\times a_2+a_1\times ib_2+ib_1\times a_2+ib_1\times ib_2\\
&=(a_1a_2-b_1b_2)+i(a_1b_2+b_1a_2)
\end{aligned}$$

ضرب در یک عدد حقیقی:
$$\forall\alpha\in\mathbb{R}:\quad \alpha z_1=\alpha a_1+i\alpha b_1$$

**(IV) تقسیم:**
$$\begin{aligned}
z_1\div z_2&=(a_1+ib_1)\div(a_2+ib_2)=\frac{a_1+ib_1}{a_2+ib_2}=\frac{(a_1+ib_1)(a_2-ib_2)}{(a_2+ib_2)(a_2-ib_2)}\\
&=\frac{(a_1a_2+b_1b_2)+i(b_1a_2-a_1b_2)}{a_2^2+b_2^2}
=\frac{a_1a_2+b_1b_2}{a_2^2+b_2^2}+i\,\frac{b_1a_2-a_1b_2}{a_2^2+b_2^2}
\end{aligned}$$

## خواص جمع و ضرب

::: {.theorem title="میدان بودن اعداد مختلط"}
مجموعهٔ اعداد مختلط همراه با دو عمل جمع و ضرب تشکیل یک میدان غیرترتیب‌پذیر می‌دهد.
:::

برای $z_1,z_2,z_3\in\mathbb{C}$:

$$z_1+z_2\in\mathbb{C},\qquad z_1\times z_2\in\mathbb{C}$$
$$z_1+z_2=z_2+z_1,\qquad z_1\times z_2=z_2\times z_1$$
$$(z_1+z_2)+z_3=z_1+(z_2+z_3),\qquad (z_1z_2)z_3=z_1(z_2z_3)$$
$$z_1(z_2+z_3)=z_1z_2+z_1z_3$$
$$z_1+(0,0)=z_1+0=z_1,\qquad z_1+(-z_1)=(0,0)=0$$
$$-z_1=-(a_1,b_1)=(-a_1,-b_1)=-a_1-ib_1$$
$$z_1\times(1,0)=z_1\times1=z_1,\qquad z_1\times z_1^{-1}=(1,0)=1$$
$$z_1^{-1}=\left(\frac{a_1}{a_1^2+b_1^2},\frac{-b_1}{a_1^2+b_1^2}\right)=\frac{a_1}{a_1^2+b_1^2}-i\,\frac{b_1}{a_1^2+b_1^2}$$

::: {.remark title="عدم ترتیب‌پذیری"}
در مجموعهٔ اعداد مختلط نمی‌توان رابطهٔ ترتیب $z_1<z_2$ تعریف کرد.
:::

## مزدوج مختلط

::: {.definition title="مزدوج مختلط یک عدد"}
$$z=x+iy\quad\Longrightarrow\quad \bar z\triangleq x-iy$$
:::

::: {.example}
مزدوج عدد مختلط $z=5+2i$ را در صفحهٔ مختلط رسم کنید.
:::

```{.figure #m08-conjugate caption="عدد مختلط $z=5+2i$ و مزدوج آن $\\bar z=5-2i$"}
```

::: {.exercise}
عبارت‌های زیر را ثابت کنید.
$$\operatorname{Re}\{z\}=\frac12\,(z+\bar z),\qquad \operatorname{Im}\{z\}=\frac{1}{2i}\,(z-\bar z),\qquad |z|^2=z\cdot\bar z$$
$$\overline{z_1+z_2}=\bar z_1+\bar z_2,\qquad \overline{z_1\cdot z_2}=\bar z_1\cdot\bar z_2,\qquad \overline{\left(\frac{z_1}{z_2}\right)}=\frac{\bar z_1}{\bar z_2}$$
$$|z|=|\bar z|,\qquad |\operatorname{Re}\{z\}|\le|z|,\qquad |\operatorname{Im}\{z\}|\le|z|$$
:::

## نامساوی مثلثی

```{.figure #m08-triangle caption="نامساوی مثلثی: مثلثی با رئوس $0$، $z_1$ و $z_1+z_2$"}
```

::: {.exercise}
- نامساوی مثلثی را برای هر دو عدد مختلط ثابت کنید: $|z_1+z_2|\le|z_1|+|z_2|$.
- فرم کلی نامساوی مثلثی را برای $n$ عدد مختلط دلخواه ثابت کنید:
$$|z_1+z_2+\cdots+z_n|\le|z_1|+|z_2|+\cdots+|z_n|$$
- ثابت کنید: $|z_1+z_2|\ge|z_1|-|z_2|$.
:::

## فرم قطبی اعداد مختلط

$$z=x+iy,\qquad \left.\begin{aligned}x&=|z|\cos\theta\\ y&=|z|\sin\theta\end{aligned}\right\}\;\Longrightarrow\; z=|z|\,(\cos\theta+i\sin\theta)$$

$$\theta=\operatorname{Arg}(z)=\tan^{-1}(y/x),\qquad -\pi<\theta\le\pi$$
$$\arg(z)=\operatorname{Arg}(z)+2k\pi,\qquad k\in\mathbb{Z}$$

## ضرب دو عدد مختلط در فرم قطبی

$$z_1=|z_1|(\cos\theta_1+i\sin\theta_1),\qquad z_2=|z_2|(\cos\theta_2+i\sin\theta_2)$$

$$\begin{aligned}
z_1\cdot z_2&=|z_1||z_2|(\cos\theta_1+i\sin\theta_1)(\cos\theta_2+i\sin\theta_2)\\
&=|z_1||z_2|\big[(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)\\
&\qquad\qquad+\,i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)\big]
\end{aligned}$$

::: {.important}
$$z_1\cdot z_2=|z_1||z_2|\big[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\big]$$
:::

::: {.remark title="نتیجهٔ ۱"}
در هنگام ضرب دو عدد مختلط، اندازه‌ها در هم ضرب و فازها با هم جمع می‌شوند.
:::

::: {.remark title="نتیجهٔ ۲"}
اگر یک عدد مختلط را به توان یک عدد طبیعی برسانیم، اندازه را به توان آن عدد طبیعی رسانده، آرگومان (فاز) را در آن عدد طبیعی ضرب می‌کنیم (به روش استقراء ثابت کنید). به عبارت دیگر:
$$z^k=|z|^k(\cos k\theta+i\sin k\theta)$$
:::

$$z^k=\big[|z|(\cos\theta+i\sin\theta)\big]^k=|z|^k(\cos\theta+i\sin\theta)^k=|z|^k(\cos k\theta+i\sin k\theta)$$

::: {.important title="رابطهٔ دموار"}
$$(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta$$
:::

::: {.exercise}
با استفاده از رابطهٔ دموار $\cos3\theta$ و $\cos4\theta$ را بر حسب $\cos\theta$ و $\sin\theta$ به دست آورید.
:::

## ریشهٔ $m$-ام یک عدد مختلط

$$w=\sqrt[m]{z}=z^{1/m},\qquad z=|z|(\cos\theta+i\sin\theta)$$

$$z=w^m,\qquad w=|w|(\cos\varphi+i\sin\varphi)$$

$$z=|z|(\cos\theta+i\sin\theta)=|w|^m(\cos m\varphi+i\sin m\varphi)$$

$$|w|^m=|z|\;\Longrightarrow\;|w|=\sqrt[m]{|z|}$$

$$m\varphi=\theta+2k\pi\;\Longrightarrow\;\varphi=\frac{\theta+2k\pi}{m},\qquad k=0,1,2,\dots,m-1$$

::: {.important}
$$w=\sqrt[m]{z}=\sqrt[m]{|z|}\left[\cos\!\left(\frac{\theta+2k\pi}{m}\right)+i\sin\!\left(\frac{\theta+2k\pi}{m}\right)\right],\qquad k=0,1,2,\dots,m-1$$
:::

::: {.example}
ریشه‌های معادلهٔ $z^n=1$ چیست؟

::: {.solution}
$$z=\sqrt[n]{1},\qquad 1=1\measuredangle0\;\Longrightarrow\; z=\cos\!\left(\frac{2k\pi}{n}\right)+i\sin\!\left(\frac{2k\pi}{n}\right),\qquad k=0,1,\dots,n-1$$
با تعریف $\omega=1\measuredangle\dfrac{2\pi}{n}$ ریشه‌ها عبارت‌اند از
$$z=1,\ \omega,\ \omega^2,\ \dots,\ \omega^{n-1}$$
:::
:::

```{.figure #m08-roots-of-unity caption="ریشه‌های $z=\\sqrt[3]{1}$، $z=\\sqrt[4]{1}$ و $z=\\sqrt[5]{1}$ روی دایرهٔ واحد"}
```

::: {.exercise}
- ریشه‌های معادلهٔ $z^6+6+8i=0$ را به دست آورده در صفحهٔ اعداد مختلط رسم کنید.
- درستی اتحاد $1+z+z^2+\cdots+z^n=\dfrac{1-z^{n+1}}{1-z}$ را تحقیق کنید و سپس اتحاد زیر (اتحاد لاگرانژ) را نتیجه بگیرید.
$$1+\cos\theta+\cos2\theta+\cdots+\cos n\theta=\frac12+\frac{\sin\!\left[\left(n+\frac12\right)\theta\right]}{2\sin(\theta/2)}$$
:::
