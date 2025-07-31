---
title: 라그랑주 승수법
categories:
  - 수학
tags:
  - 최적화
  - 미적분
date: 2025-06-29
---
# 라그랑주 승수법

## 발견적 설명

${ f,g: X \subseteq \mathbb{R}^{n} \to \mathbb{R} }$ 이고 ${ S = \left\{x: g(x) = 0 \right\} }$이며 ${ 0 }$이 ${ g }$의 정칙점이라고 하자, 그러면 ${ f }$의 ${ S }$ 위의 제한 ${ \left. f \right\rvert_{S} }$의 극값을 찾으려면 어떻게 해야할까?

정칙곡선 ${ \alpha : (-\epsilon,\epsilon) \to S }$에 대해서,

$$ \left. \frac{d}{dt} \right\vert_{t=0} f(\alpha(t)) = \nabla f(\alpha(0)) \cdot \alpha'(0)$$

따라서 ${ \left. f \right\rvert_{S} }$가 ${ x \in S }$에서 극값을 가지면 ${ x }$에서 접하는 ${ S }$의 접벡터 ${ v }$에 대해,

$$ \nabla f (x) \cdot v = 0  $$

한편,

$$ g(\alpha(t)) = c \implies \left. \frac{d}{dt} \right\rvert_{t=0} g(\alpha(t)) = \nabla g(\alpha(0)) \cdot \alpha'(0) = 0 $$

따라서 ${ \nabla g }$는 ${ S }$의 임의의 접벡터 ${ v }$와 직교한다. 즉, ${ \nabla f }$와 ${ \nabla g }$가 평행한다는 것이고 적당한 실수 ${ \lambda \neq 0 }$이 존재해,

$$ \nabla f = \lambda \nabla g $$

이때 ${ \lambda }$를 라그랑주 승수라고 부른다.

정리하자면 ${ \left. f \right\rvert_{S} }$의 극값을 찾는 것은 다음 연립방정식을 푸는 것과 같다.

$$ \begin{dcases}
\nabla f(x) - \lambda \nabla g(x) = 0 & \text{(critical equation)} \\
\hfil g(x) = 0 & \text{(constraint euqation)}
\end{dcases} $$

## 라그랑지언 함수

주어진 두 함수 ${ f,g : X \subseteq \mathbb{R}^{n} \to \mathbb{R} }$에 대해, 라그랑지언 ${ L : X \times \mathbb{R} \to \mathbb{R} }$를 다음과 같이 정의해보자

$$ L(x,\lambda) = f(x) -\lambda g(x) $$

그러면,

$$ L'(x,\lambda) = \left(\nabla f(x) - \lambda \nabla g(x),\, -g(x)\right) $$

따라서 방정식

$$ L'(x,\lambda) = (0,0) $$

은 라그랑주 승수법과 동등하다.