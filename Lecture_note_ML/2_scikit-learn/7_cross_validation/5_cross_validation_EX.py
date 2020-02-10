# -*- coding: utf-8 -*-

# winequality-red.csv 데이터의 교차 검증 점수를 확인하세요
# 머신러닝 모델은 분류 모델을 사용합니다.

import pandas as pd

fname = '../../data/winequality-red.csv'
data = pd.read_csv(fname, sep=';')
X = data.iloc[:, :-1]
y = data.iloc[:,  -1]

print(X.info())

pd.options.display.max_columns=100
# 스케일 조정이 필요함을 인지
print(X.describe())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values,
                     stratify=y.values,
                     random_state=2)

# 데이터 전처리
from sklearn.preprocessing import MinMaxScaler
# 데이터 전처리 시 반드시 학습 데이터에 대해서만
# fit 메소드를 사용합니다.
# (테스트 데이터는 transform 메소드만 사용)
scaler = MinMaxScaler().fit(X_train)

# 학습데이터의 크기를 기준으로 0 ~ 1 사이로 스케일 조정
X_train_scale = scaler.transform(X_train)
X_test_scale = scaler.transform(X_test)

from sklearn.svm import SVC
model = SVC(gamma=100, random_state=43)

model.fit(X_train_scale, y_train)

print("학습 결과 : ", model.score(X_train_scale, y_train))
print("테스트 결과 : ", model.score(X_test_scale, y_test))

from sklearn.model_selection import cross_val_score, KFold
kfold = KFold(n_splits=3, shuffle=True, random_state=1)

#scaler_all = MinMaxScaler().fit(X.values)
#X_scale = scaler_all.transform(X.values)

X_scale = MinMaxScaler().fit_transform(X.values)

scores = cross_val_score(model, X_scale, y.values, cv=kfold)

print("교차검증 점수(KFold 3) : {}".format(scores))
print("교차검증 평균 점수(KFold 3) : {}".format(scores.mean()))


















