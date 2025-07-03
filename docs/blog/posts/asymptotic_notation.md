---
title: 점근 표기법 (asymptotic notation)
tags:
  - 수치해석
  - 미적분학
  - 계산복잡도
categories:
  - 수학
  - 컴퓨터
---
# 점근 표기법

## 정의

위상공간 ${ X }$ 위의 점 ${ x_{0} }$가 고립점이 아니고 ${ \mathbb{K} }$가 실수 혹은 복소수라고 하자. 함수 ${ f,g : X \to \mathbb{K} }$에 대해 다음과 같은 점근 표기법들이 정의된다.

### Little-o

$$ f(x) = o(g(x)) \text{ as } x \to x_{0} $$

는 ${ g(x) }$가 ${ x_{0} }$ 근방에서 영이 아니고 다음을 만족하는 경우이다:

$$ \lim_{x \to x_{0}} \frac{f(x)}{g(x)} = 0 $$

### Big-O

$$ f(x) = O(g(x)) \text{ as } x \to x_{0} $$

는 ${ g(x) }$가 ${ x_{0} }$ 근방에서 영이 아니고 다음을 만족하는 경우이다:

$$ \limsup_{x \to x_{0}} \left\lvert \frac{f(x)}{g(x)} \right\rvert < \infty $$

### Big-${ \Theta }$

$$ f(x) = \Theta(g(x)) \text{ or } f(x) \asymp g(x) $$

는 다음을 만족하는 경우이다:

$$ f(x) = O\left( g(x) \right) \text{ and } g(x) = O\left( f(x) \right)  $$

### 점근 동등성 (asymptotic equivalence)

$$ f(x) \sim g(x) \text{ as } x\to x_{0} $$

는 다음을 만족하는 경우이다:

$$ \lim_{x \to x_{0}} \frac{f(x)}{g(x)} = 1 $$

### Big-${ \Omega }$

#### Hardy-Littlewood의 정의 (수론)

$$ f(x) = \Omega(g(x)) \text{ as } x \to x_{0} $$

는

$$ f(x) = o(g(x)) $$

의 부정이다. 즉, ${ g(x) }$가 ${ x_{0} }$ 근방에서 영이 아니고 다음을 만족하는 경우이다:

$$ \limsup_{x \to x_{0}} \left\lvert \frac{f(x)}{g(x)} \right\rvert > 0 $$

부호에 따라 다음과 같이 표현하기도 한다:

$$ f(x) = \Omega_{+} (g(x)) \text{ as } x \to x_{0}  \iff \limsup_{x \to x_{0}} \frac{f(x)}{g(x)} >0 $$

$$ f(x) = \Omega_{-}(g(x)) \text{ as } x \to x_{0} \iff \liminf_{x\to x_{0}} \frac{f(x)}{g(x)}<0 $$

#### Knuth의 정의 (복잡도 이론)

$$ f(x) = \Omega(g(x)) \text{ as } x\to x_{0} $$

는 다음을 만족하는 경우이다:

$$ g(x) = O(f(x)) $$

다시 말해서,

$$ \limsup_{x \to x_{0}} \left\lvert \frac{g(x)}{f(x)} \right\rvert < \infty \iff \liminf_{x \to x_{0}} \left\lvert \frac{f(x)}{g(x)} \right\rvert  = \infty $$

### Little-${ \omega }$

$$ f(x) = \omega(g(x)) \text{ as } x \to x_{0} $$

는 다음을 만족하는 경우이다:

$$ \lim_{x \to x_{0}} \left\lvert \frac{f(x)}{g(x)} \right\rvert = \infty $$

## 참고

1. [Big O notation - Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation#Family_of_Bachmann%E2%80%93Landau_notations)
2. [Big Omicron and big Omega and big Theta | ACM SIGACT News](https://dl.acm.org/doi/10.1145/1008328.1008329)
3. [A Distributional Approach to Asymptotics: Theory and Applications | SpringerLink](https://link.springer.com/book/10.1007/978-0-8176-8130-2) (주의: big-${ \Omega }$가 little-o의 부정이 아니라 big-O의 부정으로 나와있음)