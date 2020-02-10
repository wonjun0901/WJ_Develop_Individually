# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

X = np.array([6, 8, 10, 14, 18]).reshape(-1, 1)
y = np.array([7, 9, 13, 17.5, 18.7])

# 위의 X, y를 학습하여
# X 데이터가 3 ~ 20 인 경우의 y의 값을
# 그래프로 출력하세요(산점도차트로 출력)

# 테스트 데이터 생성
# 3 ~ 20 까지의 정수를 생성하여
# 2차원 배열로 변환
X_test = np.arange(3, 21).reshape(-1, 1)

# 모델의 생성과 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, y)

# 테스트 데이터에 대한 예측 값 반환
predicted = model.predict(X_test)

print('테스트 데이터의 예측 값 : \n', predicted)

plt.figure(figsize=(10,7))
plt.title('Pizza Price(inch)')
plt.xlabel('inches')
plt.ylabel('prices')

plt.scatter(X_test, predicted, c='g', marker='D')

plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()




















