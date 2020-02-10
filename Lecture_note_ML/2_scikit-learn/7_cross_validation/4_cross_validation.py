# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)

print('IRIS 데이터의 라벨 : \n', y)

model = LogisticRegression(solver='lbfgs', 
                           multi_class='multinomial')

from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=3)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())

from sklearn.model_selection import KFold

# KFold 클래스의 객체를 생성할 때, shuffle 매개변수의 값을
# True 로 지정하는 경우 정답 데이터(y)의 비율을 균등하게
# 포함하는 폴드들을 생성할 수 있습니다.
kfold = KFold(n_splits=3, shuffle=True, random_state=1)

scores = cross_val_score(model, X, y, cv=kfold)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())

kfold = KFold(n_splits=7, shuffle=True, random_state=1)

scores = cross_val_score(model, X, y, cv=kfold)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())






















