# -*- coding: utf-8 -*-

import pandas as pd

fname = '../../../../data/score.csv'
scores = pd.read_csv(fname)

X = scores.iloc[:,2:]
y = scores.score

X_data = X.values
y_data = y.values

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression().fit(X_data, y_data)
print('LR평가(R2) : ', lr_model.score(X_data, y_data))


# 선형 모델에 L1 제약 조건을 추가한 Lasso 클래스
# L1 제약 조건 : 모든 특성 데이터 중 특정 특성에 
# 대해서만 기울기(가중치)의 값을 할당하는 제약조건
# (대다수 특성의 가중치 값은 0으로 제약)
# L1 제약 조건은 특성 데이터가 많은 데이터를 학습하는 경우 
# 빠르게 학습을 할 수 있는 장점을 가짐
# 모든 특성 데이터 중 중요도가 높은 특성을 구분할 수 있음
from sklearn.linear_model import Lasso

# Lasso 클래스의 하이퍼 파라메터 alpha
# alpha의 값이 커질수록 제약을 크게 설정
# (alpha의 값이 커질수돌 대다수의 특성에 대한 
# 가중치의 값이 0으로 수렴)
# alpha의 값이 작아질수록 제약이 약해짐
# (alpha의 값이 작아질수록 적은 수의 특성에 대한 
# 가중치의 값은 0으로 수혐)
# alpha의 값이 작아질수록 LinearRegression 클래스와 동일해짐
lasso_model = Lasso(alpha=10).fit(X_data, y_data)
print('Lasso평가(R2) : ', lasso_model.score(X_data, y_data))

import numpy as np
from matplotlib import pyplot as plt

# X데이터의 특성(컬럼) 개수 확인
print(X_data.shape[1])
# LinearRegression 객체의 가중치 변수 확인
print(lr_model.coef_)

# X축의 데이터
coef_range = np.arange(1, lr_model.coef_.shape[0] + 1)

plt.plot(coef_range, lr_model.coef_, 'ro')
plt.plot(coef_range, lasso_model.coef_, 'b^')

plt.axhline(0, color='y', linestyle='--')
plt.show()
























