# -*- coding: utf-8 -*-

# winequality-white.csv 데이터를 AdaBoostClassifier, 
# GradientBoostingClassifier로 분석한 후, 결과를 확인하세요.

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

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

ada_model = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3, 
                               max_features=0.2, 
                               random_state=0), 
                               n_estimators=10000, 
                               random_state=0).fit(X_train, y_train)

from sklearn.ensemble import GradientBoostingClassifier

gb_model = GradientBoostingClassifier(
        n_estimators=10000, 
        max_depth=3, max_features=0.2, 
        subsample=0.5, random_state=0).fit(X_train, y_train)

print("훈련 세트 정확도(ADA): {:.3f}".format(ada_model.score(X_train, y_train)))
print("훈련 세트 정확도(GB): {:.3f}".format(gb_model.score(X_train, y_train)))

print("테스트 세트 정확도(ADA): {:.3f}".format(ada_model.score(X_test, y_test)))
print("테스트 세트 정확도(GB): {:.3f}".format(gb_model.score(X_test, y_test)))






























