# Linear Mappings

This chapter examines some simple mappings from the domain plane ($z$) to the range plane ($w$).

## Translation

$$\begin{aligned}
w=z+b&=(x+iy)+\operatorname{Re}\{b\}+i\operatorname{Im}\{b\}\\
&=\big(x+\operatorname{Re}\{b\}\big)+i\big(y+\operatorname{Im}\{b\}\big)
\end{aligned}$$

```{.figure #m11-translation caption="Translation $w=z+b$: a region of the $z$-plane is shifted by $b$ without changing its shape"}
```

## Rotation

$$w=az,\qquad |a|=1,\qquad a=e^{i\varphi},\qquad \varphi=\arg\{a\}$$
$$z=|z|e^{i\theta}\;\Longrightarrow\;w=|z|e^{i(\theta+\varphi)}$$

```{.figure #m11-rotation caption="Rotation $w=az$ with $|a|=1$: a region of the $z$-plane is rotated about the origin by $\\varphi=\\arg a$"}
```

## Dilation or Contraction

$$w=az,\qquad a\in\mathbb{R}^+$$
$$z=|z|e^{i\theta}\;\Longrightarrow\;w=a|z|e^{i\theta}$$

```{.figure #m11-dilation caption="Contraction $w=az$ with $0<a<1$; for $a>1$ the mapping is a dilation"}
```

## The General Linear Mapping

$$w=az+b,\qquad a,b\in\mathbb{C}$$

(a) a rotation by $\arg a$
(b) a dilation or contraction by $|a|$
(c) a translation by $b$

::: {.example}
For $w=(1+i)z+(1-i)$, find the image of the unit square.

::: {.solution}
$$w(0)=1-i,\qquad w(1)=2,\qquad w(i)=0,\qquad w(1+i)=1+i$$
:::
:::

```{.figure #m11-linear-example caption="The image of the unit square under the mapping $w=(1+i)z+(1-i)$"}
```
