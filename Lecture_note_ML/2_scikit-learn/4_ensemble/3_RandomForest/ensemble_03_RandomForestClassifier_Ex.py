# -*- coding: utf-8 -*-

# winequality-white.csv 데이터를 
# RandomForestClassifier 클래스를 이용하여 
# 분석한 후, 결과를 확인하세요.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

fname='../../../data/winequality-white.csv'
data = pd.read_csv(fname, sep=';')

X = data.iloc[:, :-1]
y = data.iloc[:,  -1]

print(y.value_counts() / len(y))

X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y.values, 
                     random_state=1)
    
model_1 = DecisionTreeClassifier(
        max_depth=20, random_state=0).fit(
                X_train, y_train)

model_2 = RandomForestClassifier(
        n_jobs=-1, max_depth=3, 
        max_features=0.1,
        n_estimators=100000, 
        random_state=0).fit(X_train, y_train)

print("model_1 정확도(학습 데이터) :", model_1.score(X_train, y_train))
print("model_2 정확도(학습 데이터) :", model_2.score(X_train, y_train))

print("model_1 정확도(테스트 데이터) :", model_1.score(X_test, y_test))
print("model_2 정확도(테스트 데이터) :", model_2.score(X_test, y_test))

predicted_1 = model_1.predict(X_test)

print('Confusion Matrix - 1:')
print(confusion_matrix(y_test, predicted_1))

print('Classification Report - 1 :')
print(classification_report(y_test, predicted_1))

predicted_2 = model_2.predict(X_test)

print('Confusion Matrix - 1:')
print(confusion_matrix(y_test, predicted_2))

print('Classification Report - 1 :')
print(classification_report(y_test, predicted_2))

import numpy as np
from matplotlib import pyplot as plt

# 각 독립 변수의 중요도(feature importance)를 계산
importances = model_2.feature_importances_

std = np.std([tree.feature_importances_ for tree in model_2.estimators_], axis=0)
indices = np.argsort(importances)[::-1]

plt.title("feature_importances_")
plt.bar(range(X.shape[1]), importances[indices],
        color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()






































