# -*- coding: utf-8 -*-

# 사이킷 런의 load_diabetes 함수를 사용하여 
# 당료병 수치를 예측할 수 있는 모델을
# 작성한 후 테스트하세요.(LinearRegression, Lasso 클래스를 활용)
# - Lasso 클래스의 alpha 값을 조절하여 값의 변화를 확인하세요.

import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

X = pd.DataFrame(diabetes.data)
y = pd.Series(diabetes.target)

print(X.info())
print(X.describe())

print(y.describe())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        random_state=1)

print(X_train.shape[0], X_test.shape[0])

from sklearn.linear_model import LinearRegression, Lasso

lr_model = LinearRegression().fit(X_train, y_train)

alpha = 0.01
lasso_model = Lasso(alpha=alpha).fit(X_train, y_train)

print('LR 학습 결과 : ', 
      lr_model.score(X_train, y_train))
print('Lasso 학습 결과 : ', 
      lasso_model.score(X_train, y_train))

print('LR 테스트 결과 : ', 
      lr_model.score(X_test, y_test))
print('Lasso 테스트 결과 : ', 
      lasso_model.score(X_test, y_test))















































