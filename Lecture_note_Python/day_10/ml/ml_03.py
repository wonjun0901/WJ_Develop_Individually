# -*- coding: utf-8 -*-

# 머신러닝을 사용한 분류
# - 이진분류 : 
#   (0, 1), ('남', '여')로 분리하는 데이터
# - 다항분류 : 
#   예측해야하는 결과가 다수개의 카테고리로 
#   구성되는 경우

import numpy as np

X1 = np.arange(1, 11)
X2 = np.arange(1, 11) * (1 + np.random.rand(10))

# numpy 모듈의 c_ 연산
# - 두개의 배열을 입력받아
#   각 배열의 동일한 위치의 인덱스
#   자리의 데이터를 하나의 데이터 결합하여
#   다차원 배열을 반환하는 연산
X = np.c_[X1, X2]
print(X)

y = np.sum(X, axis=1) >= 10
# astype 메소드
# - 현재 배열의 저장된 각 값의 
#   데이터 타입을 변환하는 메소드
y = y.astype(np.int32)

print(X)
print(y)

# 이진분류를 위한 머신러닝 클래스 import
# - 서포트벡터머신 알고리즘을 구현하고 있는
#   SVC 클래스
from sklearn.svm import SVC

# 머신러닝 모델 객체 생성
model = SVC(gamma='auto')

# 머신러닝 모델 객체의 학습
model.fit(X, y)

# 머신러닝 모델을 활용한 예측
predicted = model.predict(X)

print('예측 : \n', predicted)
print('정답 : \n', y)

# 머신러닝 모델의 평가
# 1. score 메소드를 사용
# - 분류모델의 경우 정확도 값이 반환
# - 0 ~ 1 사이의 값이 반환
print('모델평가 : ', model.score(X, y))











