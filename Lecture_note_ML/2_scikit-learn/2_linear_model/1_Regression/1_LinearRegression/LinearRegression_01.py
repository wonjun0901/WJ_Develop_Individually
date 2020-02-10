# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 피자 크기(X)에 따른 가격 데이터(y)
X = np.array([6, 8, 10, 14, 18])
y = np.array([7, 9, 13, 17.5, 18.7])

# X데이터를 이용하여 y의 값을
# 예측하기 위한 함수
def linear_func(data) :
    # 1차방정식을 사용한 예측
    # -> data * 기울기 + 절편(편향)
    return data * 1.3 + -0.5

plt.figure(figsize=(10,7))
plt.title('Pizza Price(inch)')
plt.xlabel('inches')
plt.ylabel('prices')
plt.plot(X, y, 'ko')

# 가격 예측선(직접 정의한 방정식을 사용)
plt.plot(X, linear_func(X), 'r--')

plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()











