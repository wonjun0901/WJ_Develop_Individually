# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

X = pd.DataFrame(cancer.data)
y = pd.Series(cancer.target)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        stratify=y.values, random_state=1)

from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(C=1, 
                              solver='lbfgs', 
                              max_iter=10000).fit(
                                      X_train, y_train)

print('훈련평가(LR) : ', lr_model.score(X_train,y_train))
print('테스트평가(LR) : ', lr_model.score(X_test,y_test))

# 분류를 위한 예측기 클래스의 모델 평가

# 1. 정확도 - accruracy
# 분류 모델인 경우 score 메소드는 정확도의 값을 반환
print("훈련 평가(LR) : ", lr_model.score(X_train, y_train))
print("테스트 평가(LR) : ", lr_model.score(X_test, y_test))

# 데이터의 편향 정도를 확인
print(y.value_counts() / len(y))

# 라벨 데이터의 편향이 발생된 경우
# 정확도의 신뢰성이 떨어질 수 있음

# 정밀도(precision) : 특정 클래스로 예측한 결과에서 
# 실제 정답의 비율
# EX) 1로 예측한 전체 개수 100개 중 85개가 정답이었을 경우
# 정밀도는 85%

# 재현율(recall) : 특정 클래스의 전체 개수 중 실제로 
# 예측할 비율
# EX) 라벨이 1인 데이터의 개수가 100개, 
# 실제 정답으로 예측한 개수 87개인 경우 재현율은 87%

from sklearn.metrics import confusion_matrix
# 학습 데이터에 대한 예측 결과
pred_train = lr_model.predict(X_train)
# 테스트 데이터에 대한 예측 결과
pred_test = lr_model.predict(X_test)

print('confusion_matrix - 학습')
print(confusion_matrix(y_train, pred_train))

print('confusion_matrix - 테스트')
print(confusion_matrix(y_test, pred_test))

from sklearn.metrics import classification_report

print('classification_report - 학습')
print(classification_report(y_train, pred_train))

print('classification_report - 테스트')
print(classification_report(y_test, pred_test))

















