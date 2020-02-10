# -*- coding: utf-8 -*-

import pandas as pd
# 유방암 데이터 셋(이진분률용 데이터 셋 - 악성/양성)
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

X = pd.DataFrame(cancer.data)
y = pd.Series(cancer.target)

# 결측데이터 유무를 확인
print(X.info())
# 머신러닝 모델의 학습 결과에 따라
# 성능이 나쁜경우 데이터 전처리의 
# 필요성이 있는 샘플 데이터임을 확인할 수 있음
print(X.describe())

# 이진 분류 데이티 셋으로 0과 1로 
# 라벨데이터가 구성되어 있음
print(y.value_counts())
print(y.value_counts() / len(y))

# 데이터 분할(학습/테스트)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        stratify=y.values, random_state=1)

# 분할된 데이터의 개수 확인
print(X_train.shape[0], X_test.shape[0])

# 최근접 이웃 알고리즘을 사용하여 
# 데이터를 분류할 수 있는 클래스
from sklearn.neighbors import KNeighborsClassifier

# 선형 방정식을 기반으로 데이터를 분류할 수 있는 
# LogisticRegression 클래스
# - 클래스의 이름이 Regression 으로 종료되지만
#   회귀분석이 아닌 분류용 클래스임
from sklearn.linear_model import LogisticRegression

K=3
knn_model = KNeighborsClassifier(
        n_neighbors=K).fit(X_train, y_train)

# LogisticRegression 클래스의 하이퍼 파라메터 solver
# 학습을 위해서 사용되는 알고리즘을 선택할 수 있는 파라메터
# 기본 값은 liblinear
# - 작은 데이터 셋에 잘 동작하는 알고리즘으로 L1, L2 정규화를 지원
# sag, saga
# - 대용량의 데이터를 빠르게 학습할 수 있는 알고리즘
# - 확률적 경사하강법을 기반으로 분류할 수 있는 알고리즘
# 다중 클래스의 분류 모델은 newton-cg, sag, saga 과 lbfgs 를 
# 사용해야함
# newton-cg, lbfgs, sag 알고리즘은 L2 정규화만 지원
# liblinear, saga 알고리즘은 L1 정규화도 지원함
lr_model = LogisticRegression(solver='lbfgs', max_iter=10000).fit(X_train, y_train)

# 분류를 위한 예측기 클래스의 score 메소드는 정확도의 값을 반환
print('훈련평가(KNN) : ', knn_model.score(X_train,y_train))
print('훈련평가(LR) : ', lr_model.score(X_train,y_train))

print('테스트평가(KNN) : ', knn_model.score(X_test,y_test))
print('테스트평가(LR) : ', lr_model.score(X_test,y_test))

# 최근접 이웃 알고리즘의 predict_proba 의 결과
# - 입력된 데이터의 최근접 이웃을 검색한 후,
#   검색된 이웃의 라벨(정답)의 개수를 사용하여
#   비율을 반환하는 값
print('최근접 이웃 알고리즘을 사용한 예측 확률')

# 분류 모델의 classes_ 멤버는 분류해야할 
# 클래스(값)을 저장하는 멤버 변수입니다.
print(knn_model.classes_)
print(knn_model.predict_proba(X_train[:5]))

# LogisticRegression을의 decision_function의 결과
# - 학습에 의해서 찾은 기울기(가중치)와 편향(절편)을 
#   사용하여 예측된 값을 반환
# - 음성 데이터인 경우 음수의 값, 
#   양성 데이터인 경우 양수의 값
# - decision_function의 결과 값을 이해하는 방법
#   음수의 값이 커질수록 음성데이터일 확률이 높아짐
#   양수의 값이 커질수록 양성데이터일 확률이 높아짐
# - 분류를 위한 선으로부터 이동된 거리를 의미
print('LogisticRegression을 사용한 결정함수의 결과')

# 분류 모델의 classes_ 멤버는 분류해야할 
# 클래스(값)을 저장하는 멤버 변수입니다.
print(lr_model.classes_)
print(lr_model.decision_function(X_train[:5]))

# LogisticRegression을의 predict_proba의 결과
# - decision_function의 결과를 sigmoid 함수에 대입하여
#   확률 값을 반환하는 함수
# - decision_function의 값이 음수가 나온경우
#   0.5 미만의 값이 반환
# - decision_function의 값이 양수가 나온경우
#   0.5 이상의 값이 반환
# - 강하게 양성으로 예측하는 경우(양수) 1에 근접한 값이 반환
# - 강하게 음성으로 예측하는 경우(음수) 0에 근접한 값이 반환
print('LogisticRegression을 사용한 예측 확률')
print(lr_model.classes_)
print(lr_model.predict_proba(X_train[:5]))

# sigmoid 함수를 그래프로 출력하는 예제
# - 활성화 함수의 일종
# - 입력데이터가 음수인 경우 0.5 미만의 값이 반환
# - 입력데이터가 양수인 경우 0.5 이상의 값이 반환
# - sigmoid 함수는 확률 값을 의미
# - sigmoid 함수는 딥러닝에서 학습의 
#   오차값을 반환하는 것에 활용되는 함수입니다.
import numpy as np
from matplotlib import pyplot as plt

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

x = np.arange(-10, 10.1, 0.1)

plt.figure(figsize=(10,7))
plt.axhline(0.5, color='y', linestyle='--')
plt.plot(x, sigmoid(x), 'b--')
plt.show()

print('LogisticRegression을 사용한 결정함수의 sigmoid결과')
print(sigmoid(lr_model.decision_function(X_train[:5])))

print('LogisticRegression을 사용한 예측 확률')
print(lr_model.predict_proba(X_train[:5]))









































