# -*- coding: utf-8 -*-

# 파이썬 언어는 대소문자를 구분합니다.
# - 동일한 변수명이라도 대소문자가 다르면
#   서로 다른 변수가 됩니다.
msg = "Hello"
Msg = "Python"

print(f"msg -> {msg}")
print(f"Msg -> {Msg}")

# n1, n2, n3, n4, n5 변수를 선언한 후
# 10, 20, 30, 40, 50으로 값을 할당하세요.

# 일반적인 변수의 선언과 값의 대입 방법
n1 = 10
n2 = 20
n3 = 30
n4 = 40
n5 = 50

# 파이썬의 특징을 활용한 다수개의 변수를
# 하나의 실행문으로 처리하는 예제
n1, n2, n3, n4, n5 = 10, 20, 30, 40, 50
print(f"n1 : {n1}, n2 : {n2}, n3 : {n3}, n4 : {n4}, n5 : {n5}")

# SWAP 처리
# 서로 다른 두 변수의 값을 교환하는 방법

# 아래의 n1 변수와 n2 변수의 값을 서로 교환하세요
n1 = 10
n2 = 5
print(f"BEFORE SWAP (n1->{n1}, n2->{n2})")

# 일반적인 처리 방식
# - 임시공간(변수)에 첫번째 또는 두번째 변수 값을 대입
temp = n1
# - 임시공간에 값을 저장한 변수에 다른 변수의 값을 대입
n1 = n2
# - 임시공간에 값을 두번째 변수에 대입
n2 = temp
print(f"AFTER SWAP (n1->{n1}, n2->{n2})")

# 파이썬 언어의 특징을 활용한 SWAP 처리
n1 = 10
n2 = 5
print(f"BEFORE SWAP (n1->{n1}, n2->{n2})")

n1, n2 = n2, n1
print(f"AFTER SWAP (n1->{n1}, n2->{n2})")












