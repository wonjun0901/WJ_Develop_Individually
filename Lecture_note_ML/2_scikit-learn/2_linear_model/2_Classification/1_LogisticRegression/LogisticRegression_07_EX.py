# -*- coding: utf-8 -*-

# LogisticRegression 클래스를 사용하여 
# load_iris 데이터를 분석하고
# 정확도 및 정밀도, 재현율을 확인하세요.

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(iris.data)
y = pd.Series(iris.target)

print(X.info())
print(X.describe())

# 라벨 데이터의 편향이 없는 경우
# 정확도가 유의미한 결과를 보일 수 있음
print(y.value_counts())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        test_size=0.3, stratify=y.values,
        random_state=1)

from sklearn.linear_model import LogisticRegression

C=1
model_ovr = LogisticRegression(solver='lbfgs',
                               multi_class='ovr',
                               C=C).fit(X_train, y_train)
model_multi = LogisticRegression(solver='lbfgs',
                               multi_class='multinomial',
                               C=C).fit(X_train, y_train)

print("학습 평가(ovr) : ", 
      model_ovr.score(X_train, y_train))
print("학습 평가(multinomial) : ", 
      model_multi.score(X_train, y_train))

print("테스트 평가(ovr) : ", 
      model_ovr.score(X_test, y_test))
print("테스트 평가(multinomial) : ", 
      model_multi.score(X_test, y_test))

from sklearn.metrics import classification_report

pred_train_ovr = model_ovr.predict(X_train)
pred_train_multi = model_multi.predict(X_train)

print("classification_report 평가(ovr) : \n", 
      classification_report(
              y_train, pred_train_ovr, 
              target_names=iris.target_names))
print("classification_report 평가(multinomial) : \n", 
      classification_report(
              y_train, pred_train_multi, 
              target_names=iris.target_names))

pred_test_ovr = model_ovr.predict(X_test)
pred_test_multi = model_multi.predict(X_test)

print("classification_report 평가(ovr) : \n", 
      classification_report(
              y_test, pred_test_ovr, 
              target_names=iris.target_names))
print("classification_report 평가(multinomial) : \n", 
      classification_report(
              y_test, pred_test_multi, 
              target_names=iris.target_names))





















