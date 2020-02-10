# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

X = pd.DataFrame(cancer.data)
y = pd.Series(cancer.target)

print(X.info())
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

from sklearn.svm import LinearSVC

svm_model = LinearSVC(C=1).fit(X_train, y_train)

print('훈련평가(SVM) : ', 
      svm_model.score(X_train,y_train))

print('테스트평가(SVM) : ', 
      svm_model.score(X_test,y_test))

predicted = svm_model.predict(X_test[:3])
print('예측 결과 : ', predicted)

# LinearSVC 클래스는 확률 값을 반환하는 
# predict_proba 메소드가 제공되지 않음

# decision_function 메소드를 사용하여 
# 예측 결과의 과정을 이해할 수 있음
# 0을 기준으로 작다면 음성, 크다면 양성으로 예측함
predicted = svm_model.decision_function(X_test[:3])
print('decision_function : \n', predicted)

# decision_function 메소드의 결과를 사용하여
# 확률 값을 반환하는 예제
import numpy as np

def sigmoid(x) :
    x_transform = np.array(
            [data * -1 if data < 0 else data for data in x])
    return 1 / (1 + np.exp(-x_transform))

predict_proba = sigmoid(predicted)
print('predict_proba : \n', predict_proba)
























