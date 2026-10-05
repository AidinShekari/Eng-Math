# نگاشت‌های خطی

در این فصل برخی نگاشت‌های ساده از صفحهٔ دامنه ($z$) به صفحهٔ برد ($w$) بررسی می‌شوند.

## انتقال

$$\begin{aligned}
w=z+b&=(x+iy)+\operatorname{Re}\{b\}+i\operatorname{Im}\{b\}\\
&=\big(x+\operatorname{Re}\{b\}\big)+i\big(y+\operatorname{Im}\{b\}\big)
\end{aligned}$$

```{.figure #m04-translation caption="انتقال $w=z+b$: ناحیه‌ای از صفحهٔ $z$ بدون تغییر شکل به اندازهٔ $b$ جابه‌جا می‌شود"}
```

## دوران

$$w=az,\qquad |a|=1,\qquad a=e^{i\varphi},\qquad \varphi=\arg\{a\}$$
$$z=|z|e^{i\theta}\;\Longrightarrow\;w=|z|e^{i(\theta+\varphi)}$$

```{.figure #m04-rotation caption="دوران $w=az$ با $|a|=1$: ناحیه‌ای از صفحهٔ $z$ به اندازهٔ $\\varphi=\\arg a$ حول مبدأ می‌چرخد"}
```

## انبساط یا انقباض

$$w=az,\qquad a\in\mathbb{R}^+$$
$$z=|z|e^{i\theta}\;\Longrightarrow\;w=a|z|e^{i\theta}$$

```{.figure #m04-dilation caption="انقباض $w=az$ با $0<a<1$؛ برای $a>1$ نگاشت یک انبساط است"}
```

## نگاشت خطی کلی

$$w=az+b,\qquad a,b\in\mathbb{C}$$

الف) دوران به اندازهٔ $\arg a$
ب) انبساط یا انقباض به اندازهٔ $|a|$
ج) انتقال به اندازهٔ $b$

::: {.example}
اگر $w=(1+i)z+(1-i)$ مطلوب است تصویر مربع واحد.

::: {.solution}
$$w(0)=1-i,\qquad w(1)=2,\qquad w(i)=0,\qquad w(1+i)=1+i$$
:::
:::

```{.figure #m04-linear-example caption="تصویر مربع واحد تحت نگاشت $w=(1+i)z+(1-i)$"}
```
