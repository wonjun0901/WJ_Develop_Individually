# -*- coding: utf-8 -*-

# 최근접 이웃 알고리즘의 단점
# - 학습 데이터의 범위를 벗어나는 데이터의 분석이 불가능

import numpy as np

# [1,2,3,4,5,6,7,8,9,10]
X = np.array(list(range(1,11)))
# [[1],[2],[3], ... ,[10]]
X = X.reshape(-1, 1)

# [1,2,3,4,5,6,7,8,9,10]
y = np.array(list(range(1,11)))
# [10,20,30,40,50,60,70,80,90,100]
y = np.multiply(y, 10)

print('X : ', X)
print('y : ', y)

from sklearn.neighbors import KNeighborsRegressor
K = 1
model = KNeighborsRegressor(n_neighbors=K).fit(X, y)

print('5.3의 예측 값 : ', model.predict([[5.3]]))

print('7.8의 예측 값 : ', model.predict([[7.8]]))

# 학습 데이터 X의 최대 값이 10 이므로 
# 항상 10의 라벨 데이터인 100으로 예측
print('150의 예측 값 : ', model.predict([[150]]))
print('15000의 예측 값 : ', model.predict([[15000]]))

# 선형방정식을 기반으로 예측할 수 있는 클래스
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression().fit(X, y)

print('5.3의 예측 값 : ', lr_model.predict([[5.3]]))
print('7.8의 예측 값 : ', lr_model.predict([[7.8]]))
print('150의 예측 값 : ', lr_model.predict([[150]]))
print('15000의 예측 값 : ', lr_model.predict([[15000]]))





















