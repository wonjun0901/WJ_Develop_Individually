# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

X = pd.DataFrame(cancer.data)
y = pd.Series(cancer.target)

print(X.info())
# 머신러닝 모델의 학습 결과에 따라
# 성능이 나쁜경우 데이터 전처리의 
# 필요성이 있는 샘플 데이터임을 확인할 수 있음
print(X.describe())

print(y.value_counts())
print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        stratify=y.values, random_state=1)

print(X_train.shape[0], X_test.shape[0])

# X 데이터의 스케일을 조정하는 전처리 코드
# - 모든 특성 데이터를 0 ~ 1 사이의 값으로 조정
# - 각 특성 데이터의 최소값, 최대값을 사용
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(
        solver='lbfgs', max_iter=10000).fit(X_train, y_train)

from sklearn.svm import LinearSVC
# Linear Support Vector Machine 알고리즘으로 구현된 분류 클래스
# Support Vector Machine을 구현하고 있는 SVC에 비해서
# 선형 계산에 특화되어 있어 선형 데이터를 분류하는 경우 더 효율적
# (LinearSVC 클래스의 학습 이후, the number of iterations 메세지가
# 출력되는 경우 학습이 완료되지 않은 상태이므로 max_iter 매개변수를
# 조정하여 성능을 높일 수 있습니다.)
svm_model = LinearSVC(max_iter=10000).fit(X_train, y_train)

print('훈련평가(LR) : ', lr_model.score(X_train,y_train))
print('훈련평가(SVM) : ', svm_model.score(X_train,y_train))

print('테스트평가(LR) : ', lr_model.score(X_test,y_test))
print('테스트평가(SVM) : ', svm_model.score(X_test,y_test))






































