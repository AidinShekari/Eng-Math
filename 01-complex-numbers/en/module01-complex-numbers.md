# Complex Numbers

## The Set of Complex Numbers

::: {.definition title="Complex numbers"}
The set of complex numbers generalizes the real numbers on the real line to a plane of numbers having two components, a real one and an imaginary one.
$$\mathbb{R}\to\mathbb{C}$$
:::

$$\mathbb{C}=\{(x,y)\mid x,y\in\mathbb{R}\},\qquad z=(x,y),\qquad x=\operatorname{Re}\{z\},\qquad y=\operatorname{Im}\{z\}$$

```{.figure #m01-complex-plane caption="The complex number $z=(x,y)$ in the complex plane; its modulus $|z|$ and argument $\\theta$"}
```

Magnitude or norm of a complex number:
$$|z|=\sqrt{x^2+y^2}$$

Phase or argument:
$$\theta=\measuredangle z=\tan^{-1}\!\left(\frac{y}{x}\right),\qquad z=|z|\measuredangle\theta$$
$$x=|z|\cos\theta,\qquad y=|z|\sin\theta$$

$$z=x\times(1,0)+y\times(0,1)=x+iy$$

::: {.important}
$$i^2=-1$$
:::

## The Four Basic Operations

Let $z_1=(a_1,b_1)=a_1+ib_1$ and $z_2=(a_2,b_2)=a_2+ib_2$.

**(I) Addition:**
$$z_1+z_2=(a_1+a_2,\,b_1+b_2)=a_1+a_2+i(b_1+b_2)$$

**(II) Subtraction:**
$$z_1-z_2=(a_1-a_2,\,b_1-b_2)=a_1-a_2+i(b_1-b_2)$$

**(III) Multiplication:**
$$\begin{aligned}
z_1\times z_2&=(a_1+ib_1)\times(a_2+ib_2)\\
&=a_1\times a_2+a_1\times ib_2+ib_1\times a_2+ib_1\times ib_2\\
&=(a_1a_2-b_1b_2)+i(a_1b_2+b_1a_2)
\end{aligned}$$

Multiplication by a real number:
$$\forall\alpha\in\mathbb{R}:\quad \alpha z_1=\alpha a_1+i\alpha b_1$$

**(IV) Division:**
$$\begin{aligned}
z_1\div z_2&=(a_1+ib_1)\div(a_2+ib_2)=\frac{a_1+ib_1}{a_2+ib_2}=\frac{(a_1+ib_1)(a_2-ib_2)}{(a_2+ib_2)(a_2-ib_2)}\\
&=\frac{(a_1a_2+b_1b_2)+i(b_1a_2-a_1b_2)}{a_2^2+b_2^2}
=\frac{a_1a_2+b_1b_2}{a_2^2+b_2^2}+i\,\frac{b_1a_2-a_1b_2}{a_2^2+b_2^2}
\end{aligned}$$

## Properties of Addition and Multiplication

::: {.theorem title="The complex numbers form a field"}
The set of complex numbers, together with addition and multiplication, forms a field that cannot be ordered.
:::

For $z_1,z_2,z_3\in\mathbb{C}$:

$$z_1+z_2\in\mathbb{C},\qquad z_1\times z_2\in\mathbb{C}$$
$$z_1+z_2=z_2+z_1,\qquad z_1\times z_2=z_2\times z_1$$
$$(z_1+z_2)+z_3=z_1+(z_2+z_3),\qquad (z_1z_2)z_3=z_1(z_2z_3)$$
$$z_1(z_2+z_3)=z_1z_2+z_1z_3$$
$$z_1+(0,0)=z_1+0=z_1,\qquad z_1+(-z_1)=(0,0)=0$$
$$-z_1=-(a_1,b_1)=(-a_1,-b_1)=-a_1-ib_1$$
$$z_1\times(1,0)=z_1\times1=z_1,\qquad z_1\times z_1^{-1}=(1,0)=1$$
$$z_1^{-1}=\left(\frac{a_1}{a_1^2+b_1^2},\frac{-b_1}{a_1^2+b_1^2}\right)=\frac{a_1}{a_1^2+b_1^2}-i\,\frac{b_1}{a_1^2+b_1^2}$$

::: {.remark title="No ordering"}
An order relation $z_1<z_2$ cannot be defined on the set of complex numbers.
:::

## The Complex Conjugate

::: {.definition title="Complex conjugate of a number"}
$$z=x+iy\quad\Longrightarrow\quad \bar z\triangleq x-iy$$
:::

::: {.example}
Plot the conjugate of the complex number $z=5+2i$ in the complex plane.
:::

```{.figure #m01-conjugate caption="The complex number $z=5+2i$ and its conjugate $\\bar z=5-2i$"}
```

::: {.exercise}
Prove the following statements.
$$\operatorname{Re}\{z\}=\frac12\,(z+\bar z),\qquad \operatorname{Im}\{z\}=\frac{1}{2i}\,(z-\bar z),\qquad |z|^2=z\cdot\bar z$$
$$\overline{z_1+z_2}=\bar z_1+\bar z_2,\qquad \overline{z_1\cdot z_2}=\bar z_1\cdot\bar z_2,\qquad \overline{\left(\frac{z_1}{z_2}\right)}=\frac{\bar z_1}{\bar z_2}$$
$$|z|=|\bar z|,\qquad |\operatorname{Re}\{z\}|\le|z|,\qquad |\operatorname{Im}\{z\}|\le|z|$$
:::

## The Triangle Inequality

```{.figure #m01-triangle caption="The triangle inequality: a triangle with vertices $0$, $z_1$ and $z_1+z_2$"}
```

::: {.exercise}
- Prove the triangle inequality for any two complex numbers: $|z_1+z_2|\le|z_1|+|z_2|$.
- Prove the general form of the triangle inequality for $n$ arbitrary complex numbers:
$$|z_1+z_2+\cdots+z_n|\le|z_1|+|z_2|+\cdots+|z_n|$$
- Prove that $|z_1+z_2|\ge|z_1|-|z_2|$.
:::

## The Polar Form of Complex Numbers

$$z=x+iy,\qquad \left.\begin{aligned}x&=|z|\cos\theta\\ y&=|z|\sin\theta\end{aligned}\right\}\;\Longrightarrow\; z=|z|\,(\cos\theta+i\sin\theta)$$

$$\theta=\operatorname{Arg}(z)=\tan^{-1}(y/x),\qquad -\pi<\theta\le\pi$$
$$\arg(z)=\operatorname{Arg}(z)+2k\pi,\qquad k\in\mathbb{Z}$$

## Multiplying Two Complex Numbers in Polar Form

$$z_1=|z_1|(\cos\theta_1+i\sin\theta_1),\qquad z_2=|z_2|(\cos\theta_2+i\sin\theta_2)$$

$$\begin{aligned}
z_1\cdot z_2&=|z_1||z_2|(\cos\theta_1+i\sin\theta_1)(\cos\theta_2+i\sin\theta_2)\\
&=|z_1||z_2|\big[(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)\\
&\qquad\qquad+\,i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)\big]
\end{aligned}$$

::: {.important}
$$z_1\cdot z_2=|z_1||z_2|\big[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\big]$$
:::

::: {.remark title="Consequence 1"}
When two complex numbers are multiplied, their magnitudes are multiplied and their phases are added.
:::

::: {.remark title="Consequence 2"}
If a complex number is raised to a natural power, its magnitude is raised to that power and its argument (phase) is multiplied by it (prove by induction). In other words:
$$z^k=|z|^k(\cos k\theta+i\sin k\theta)$$
:::

$$z^k=\big[|z|(\cos\theta+i\sin\theta)\big]^k=|z|^k(\cos\theta+i\sin\theta)^k=|z|^k(\cos k\theta+i\sin k\theta)$$

::: {.important title="De Moivre's formula"}
$$(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta$$
:::

::: {.exercise}
Using De Moivre's formula, express $\cos3\theta$ and $\cos4\theta$ in terms of $\cos\theta$ and $\sin\theta$.
:::

## The $m$-th Root of a Complex Number

$$w=\sqrt[m]{z}=z^{1/m},\qquad z=|z|(\cos\theta+i\sin\theta)$$

$$z=w^m,\qquad w=|w|(\cos\varphi+i\sin\varphi)$$

$$z=|z|(\cos\theta+i\sin\theta)=|w|^m(\cos m\varphi+i\sin m\varphi)$$

$$|w|^m=|z|\;\Longrightarrow\;|w|=\sqrt[m]{|z|}$$

$$m\varphi=\theta+2k\pi\;\Longrightarrow\;\varphi=\frac{\theta+2k\pi}{m},\qquad k=0,1,2,\dots,m-1$$

::: {.important}
$$w=\sqrt[m]{z}=\sqrt[m]{|z|}\left[\cos\!\left(\frac{\theta+2k\pi}{m}\right)+i\sin\!\left(\frac{\theta+2k\pi}{m}\right)\right],\qquad k=0,1,2,\dots,m-1$$
:::

::: {.example}
What are the roots of the equation $z^n=1$?

::: {.solution}
$$z=\sqrt[n]{1},\qquad 1=1\measuredangle0\;\Longrightarrow\; z=\cos\!\left(\frac{2k\pi}{n}\right)+i\sin\!\left(\frac{2k\pi}{n}\right),\qquad k=0,1,\dots,n-1$$
Defining $\omega=1\measuredangle\dfrac{2\pi}{n}$, the roots are
$$z=1,\ \omega,\ \omega^2,\ \dots,\ \omega^{n-1}$$
:::
:::

```{.figure #m01-roots-of-unity caption="The roots $z=\\sqrt[3]{1}$, $z=\\sqrt[4]{1}$ and $z=\\sqrt[5]{1}$ on the unit circle"}
```

::: {.exercise}
- Find the roots of the equation $z^6+6+8i=0$ and plot them in the complex plane.
- Verify the identity $1+z+z^2+\cdots+z^n=\dfrac{1-z^{n+1}}{1-z}$ and then derive the following identity (Lagrange's identity).
$$1+\cos\theta+\cos2\theta+\cdots+\cos n\theta=\frac12+\frac{\sin\!\left[\left(n+\frac12\right)\theta\right]}{2\sin(\theta/2)}$$
:::
