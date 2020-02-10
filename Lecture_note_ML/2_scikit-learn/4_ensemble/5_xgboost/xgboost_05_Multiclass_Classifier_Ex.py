# -*- coding: utf-8 -*-

# winequality-white.csv 데이터를 XGBClassifier 클래스를 활용하여
# 분석한 후, 분석 결과를 확인하세요.

import pandas as pd

fname = '../../../data/winequality-white.csv'
wine = pd.read_csv(fname, sep=';')

print(wine.head())

X = wine.iloc[:,:-1]
y = wine.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(\
     X.values, y.values, 
     stratify=y.values, random_state=0)

print(X_train.shape[0], X_test.shape[0])

import xgboost as xgb
from sklearn.metrics import confusion_matrix, classification_report

model = xgb.XGBClassifier(objective="multi:softmax", 
                          n_estimators=10000,
                          subsample=0.5,
                          random_state=42)
model.fit(X_train, y_train)

print("학습 결과 : ", model.score(X_train, y_train))
print("테스트 결과 : ", model.score(X_test, y_test))

y_pred = model.predict(X_train)
print("confusion_matrix - 학습 데이터")
print(confusion_matrix(y_train, y_pred))

y_pred = model.predict(X_test)
print("confusion_matrix - 테스트 데이터")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))




