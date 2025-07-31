---
title: sesquilinear = linear + conjugate
date: 2025-07-31
categories:
  - 수학
tags:
  - 선형대수
  - 함수해석
---
# sesquilinear = linear + conjugate

## 정의

복소수 체 ${ \mathbb{C} }$ 위의 벡터공간 ${ X }$에서 정의된 linear functional ${ f : X \times X\to \mathbb{C} }$가 다음 두 조건을 만족할 때 ${ f }$는 *sesquilinear form*이라고 한다.

임의의 두 스칼라 ${ \alpha,\beta \in \mathbb{C} }$와 임의의 세 벡터 ${ x,y,z \in X }$에 대해,
1. (linearity) ${ f(\alpha x + \beta y,z) = \alpha f(x,z) + \beta f(y,z) }$
2. (antilinearity) ${ f(x,\alpha y + \beta z) = \overline{\alpha} f(x,y) + \overline{\beta}f(x,z)}$

## 명제

**Proposition** 고정된 ${ y \in X }$에 대해 ${ f_{y} : X \to \mathbb{C} }$를 ${ f_{y}(x) = f(x,y) }$로 정의하자. 그러면,

$$ f\text{는 sesquilinear form} \iff (\forall y\in X)\ f_{y} \text{는 linear functional 이고 } f(y,x) = \overline{f(x,y)} $$

**Proof)** (${ \implies }$) sesqulinear이므로 ${ f_{y} }$는 linear functional. 복소켤레에 관한 성질을 증명하기 위해서 polarization identity을 이용하면,

$$ \begin{eqnarray}
f(y,x) & = & \frac{1}{4} \left[ f(y+x,y+x) - f(y-x,y-x) \right] + \frac{i}{4}\left[ f(y+ix,y+ix) - f(y-ix,y-ix) \right] \\
& = & \frac{1}{4}\left[ f(x+y,x+y)-f(x-y,x-y) \right] +\frac{i}{4}\left[f(i(x-iy),i(x-iy)) - f(i(x+iy),i(x+iy)) \right] \\
& = & \frac{1}{4}\left[ f(x+y,x+y)-f(x-y,x-y) \right] -\frac{i}{4}\left[f(x+iy,x+iy)-f(x-iy,x-iy) \right] \\
& = & \overline{f(x,y)}
\end{eqnarray} $$

${ (\impliedby) }$ antilinearity만 증명하면 충분하다.

$$ \begin{eqnarray}
f(x,\alpha y + \beta z) & = & \overline{f(\alpha y + \beta z , x)} \\
& = & \overline{\alpha f(y,x) + \beta f(z,x)} \\
& = & \overline{\alpha} \overline{f(y,x)} + \overline{\beta}\overline{f(z,x)} \\
& = & \overline{\alpha} f(x,y) + \overline{\beta}f(x,z)
\end{eqnarray} $$