---
title: hom-set이 연산에 닫혀있을 조건
date: 2025-06-22
tags:
  - 범주론
  - 보편대수
categories:
  - 수학
---
# hom-set이 연산에 닫혀있을 조건
## 관찰
magma ${ X,Y }$가 주워졌을 때 morphism ${ f,g:X \to Y }$에 대해서

$$ (fg)(x_{1}x_{2})=f(x_{1}x_{2})g(x_{1}x_{2})=f(x_{1})f(x_{2})g(x_{1})g(x_{2}) $$

이고

$$ (fg)(x_{1})(fg)(x_{2})=f(x_{1})g(x_{1})f(x_{2})g(x_{2}) $$

이므로 ${ fg }$가 morphism이려면 임의의 ${ x_{1}, x_{2} \in X}$에 대해 다음 등식을 만족해야 한다.

$$ f(x_{1})f(x_{2})g(x_{1})g(x_{2})=f(x_{1})g(x_{1})f(x_{2})g(x_{2}) $$

위 관계식

$$ (ab)(cd)=(ac)(bd) $$

를 *mediality* 혹은 *entropicity*라고 부른다. 따라서 ${ \text{Hom}(X,Y) }$가 ${ Y }$의 연산에서 유도된 연산에 닫혀있을 충분조건은 ${ Y }$가 *medial magma*인 것이다.

## 참고
1. [Why is $\operatorname{Hom}(A, B)$ an abelian group? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/643588/why-is-operatornamehoma-b-an-abelian-group)
2. [Medial magma - Wikipedia](https://en.wikipedia.org/wiki/Medial_magma)