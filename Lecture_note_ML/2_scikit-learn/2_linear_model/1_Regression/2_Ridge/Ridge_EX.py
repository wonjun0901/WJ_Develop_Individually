# -*- coding: utf-8 -*-

# 사이킷 런의 load_diabetes 함수를 사용하여 
# 당뇨병 수치를 예측할 수 있는 모델을
# 작성한 후 테스트하세요.(LinearRegression, Ridge 클래스를 활용)
# - Ridge 클래스의 alpha 값을 조절하여 값의 변화를 확인하세요

import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

X = pd.DataFrame(diabetes.data)
y = pd.Series(diabetes.target)

print(X.info())
print(X.describe())

print(y.head())
print(y.describe())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     random_state=1)
    
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Ridge

K=3
knn_model=KNeighborsRegressor(n_neighbors=K).fit(X_train, y_train)
lr_model=LinearRegression().fit(X_train, y_train)
alpha=0.01
ridge_model=Ridge(alpha=alpha).fit(X_train, y_train)

print('KNN 학습 결과 : ', knn_model.score(X_train, y_train))
print('LR 학습 결과 : ', lr_model.score(X_train, y_train))
print('Ridge 학습 결과 : ', ridge_model.score(X_train, y_train))

print('KNN 테스트 결과 : ', knn_model.score(X_test, y_test))
print('LR 테스트 결과 : ', lr_model.score(X_test, y_test))
print('Ridge 테스트 결과 : ', ridge_model.score(X_test, y_test))
















