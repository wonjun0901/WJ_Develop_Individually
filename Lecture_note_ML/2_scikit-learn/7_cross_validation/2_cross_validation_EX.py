# -*- coding: utf-8 -*-

# winequality-white.csv 데이터를 교차검증을 수행하여
# 'GradientBoostingClassifier'의 평가점수를 확인하세요.

import pandas as pd

fname = '../../data/winequality-white.csv'
wine = pd.read_csv(fname, sep=';')

X, y = wine.iloc[:,:-1], wine.iloc[:,-1]

# GradientBoostingClassifier 모델의 교차검증
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=1000,
                                   subsample=0.7,
                                   max_features=0.5,
                                   max_depth=3,
                                   random_state=1)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())

# RandomForestClassifier 모델의 교차검증
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=1000,
                                   n_jobs=-1,
                                   max_features=0.5,
                                   max_depth=3,
                                   random_state=1)

scores = cross_val_score(model, X, y, cv=5)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())










