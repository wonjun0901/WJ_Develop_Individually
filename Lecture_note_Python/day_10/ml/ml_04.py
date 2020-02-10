# -*- coding: utf-8 -*-
"""
data 디렉토리에 저장된 ucla.csv 파일을 사용하여
이진분류를 위한 머신러닝 모델을 생성하세요.
"""

# csv 파일을 읽어들이기 위한 pandas 모듈 import
import pandas as pd

# csv 파일명
input_fname = './data/ucla.csv'

# pandas를 사용하여 파일의 내용을 DataFrame으로 저장
ucla = pd.read_csv(input_fname, header=None)

# DataFrame에서 입력데이터(X)를 추출
# - 모든 행의 데이터 중, 
#   두번째 컬럼부터 마지막 컬럼까지 추출
X = ucla.iloc[:, 1:]
# DataFrame에서 정답데이터(y)를 추출
# - 모든 행의 데이터 중, 
#   첫번째 컬럼만 추출
y = ucla.iloc[:, 0]

# 정답데이터의 편향 정보 확인
print(y.value_counts())
print(y.value_counts() / len(y))

# 머신러닝 클래스 import
# - 선형모델을 기반으로 분류 작업을 수행할 수 있는
#   LogisticRegression 클래스
from sklearn.linear_model import LogisticRegression

# 머신러닝 모델 객체 생성
model = LogisticRegression(solver='lbfgs')

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














