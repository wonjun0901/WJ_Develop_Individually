# -*- coding: utf-8 -*-

# 데이터전처리
# 데이터 분석을 위한 데이터 처리 과정
# - 전체 데이터 셋에서 데이터 분석에 사용될 열 선정
# - 특정 열에 존재하는 빈 값을 제거하거나
#   또는 특정 열에 존재하는 빈 값을 임의의 값으로 변경
# - 데이터의 스케일(값의 범위) 조정
# - 범주형 변수의 값 변경
#   (문자열 값의 수치 데이터화)
#   (원핫인코딩 처리)
# - 학습, 테스트 데이터 분할

# 특성 데이터의 확장 - 다항식 변환
# - PolynomialFeatures 클래스
# - 입력값  x 를 다항식으로 변환하는 기능을 제공

# 파라메터 정보
# degree : 다항식의 차수
# include_bias : 상수항(절편) 생성 여부

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.arange(1, 6).reshape(-1, 1)
print(X)

#pf = PolynomialFeatures(degree=2)
pf = PolynomialFeatures(degree=2, include_bias=False)
print(pf.fit_transform(X))

# X * w + b -> 1차방정식
X = np.arange(1, 11).reshape(-1, 1)
y = np.array([3, 7, 9, 8, 6, 2, 3, 5, 9, 12])

from sklearn.linear_model import LinearRegression

# 원본 데이터를 활용한 1차방적식 기반의 예측
model = LinearRegression().fit(X, y)
print(model.score(X, y))

from matplotlib import pyplot as plt

plt.plot(X, y, 'ro')
plt.plot(X, model.predict(X), 'b--')
plt.show()

# 특성데이터를 추가하여 분석하는 예제
pf = PolynomialFeatures(degree=2, include_bias=False)
X_poly = pf.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
print(model.score(X_poly, y))

plt.plot(X, y, 'ro')
plt.plot(X, model.predict(X_poly), 'b--')
plt.show()

pf = PolynomialFeatures(degree=3, include_bias=False)
X_poly = pf.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
print(model.score(X_poly, y))

plt.plot(X, y, 'ro')
plt.plot(X, model.predict(X_poly), 'b--')
plt.show()































