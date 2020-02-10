# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 머신러닝을 사용하여 데이터를 분석하는 과정

# 1. 데이터 셋의 로딩
# - iris 데이터 셋 로딩
X, y = load_iris(return_X_y=True)

# 1-1. 데이터 셋의 확인
# - 결측 데이터 유무
# - 특성 데이터의 스케일 확인
# - 라벨 데이터의 편향

# 2. 데이터의 분할
# - 훈련 데이터 / 테스트 데이터 분할
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, stratify=y, 
                     random_state=0)
    
# 3. 머신러닝 모델의 객체 생성 및 학습
model = LogisticRegression(solver='lbfgs', 
                           multi_class='multinomial')
model.fit(X_train, y_train)

# 4. 머신러닝 모델의 평가
# - 테스트 데이터를 사용하여 모델을 평가
print("테스트 세트 평가 점수 : ",
      model.score(X_test, y_test))















