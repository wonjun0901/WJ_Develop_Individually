# -*- coding: utf-8 -*-

# data 폴데에 있는 score.csv 파일을 읽어오세요.
# iq,academy,game,tv 점수를 X 데이터로 활용하여
# score 점수(y)를 예측할 수 있는 회귀 모델을 테스트하세요
# (r2-score, 평균제곱오차, 평균절대오차 값을 출력하세요)

import pandas as pd

fname = '../../../../data/score.csv'
scores = pd.read_csv(fname)

X = scores.iloc[:,2:]
y = scores.score

# pandas 타입의 데이터를 numpy 타입으로 변환
# pandas의 DataFrame과 Series 타입은 
# values 속성을 제공하여 numpy 타입으로 데이터를
# 반환할 수 있습니다.
# pd.DataFrame.values -> 2차원 numpy 배열이 반환
# pd.Series.values -> 1차원 numpy 배열이 반환
X_data = X.values
y_data = y.values

# 예측기 클래스의 import
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

# - 최근접 이웃 알고리즘을 사용한 예측기 모델의 
#   생성 및 학습
K=2
kr_model = KNeighborsRegressor(
        n_neighbors=K).fit(X_data, y_data)

# - 선형 방정식을 사용한 예측기 모델의 생성 및 학습
lr_model = LinearRegression().fit(X_data, y_data)

# 모델 평가
# - 결정계수를 사용하여 평가
# - score 메소드(R2스코어 - 결정계수)
print('KNN평가(R2) : ', kr_model.score(X_data, y_data))
print('LR평가(R2) : ', lr_model.score(X_data, y_data))

# - 평균제곱오차를 사용하여 평가
from sklearn.metrics import mean_squared_error
knn_pred = kr_model.predict(X_data)
lr_pred = lr_model.predict(X_data)

print('KNN평가(squared) : ', 
      mean_squared_error(y_data, knn_pred))
print('LR평가(squared) : ', 
      mean_squared_error(y_data, lr_pred))

# - 평균절대오차를 사용하여 평가
from sklearn.metrics import mean_absolute_error
knn_pred = kr_model.predict(X_data)
lr_pred = lr_model.predict(X_data)

print('KNN평가(absolute) : ', 
      mean_absolute_error(y_data, knn_pred))
print('LR평가(absolute) : ', 
      mean_absolute_error(y_data, lr_pred))














