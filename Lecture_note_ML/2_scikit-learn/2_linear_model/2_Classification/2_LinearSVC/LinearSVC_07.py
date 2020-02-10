# -*- coding: utf-8 -*-

# LinearSVC 클래스를 사용하여 load_wine 데이터를 분석하고
# 정확도 및 정밀도, 재현율을 확인하세요.

import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

X = pd.DataFrame(wine.data)
y = pd.Series(wine.target)

print(X.info())
pd.options.display.max_columns=100
print(X.describe())

print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        stratify=y.values, random_state=1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import LinearSVC

C=0.1
model = LinearSVC(C=C, random_state=1).fit(X_train, y_train)

print('학습 결과 : ', 
      model.score(X_train, y_train))
print('테스트 결과 : ', 
      model.score(X_test, y_test))



























