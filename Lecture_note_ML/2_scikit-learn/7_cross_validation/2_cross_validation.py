# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 교차 검증
# - 데이터을 분석하기 위한 알고리즘을 테스트하는 역할
# - 전체 데이터 셋을 폴드라는 단위로 나눈 후,
#   각 폴드를 테스트 셋으로 사용하여 단위테스를 수행한 후
#   각 폴드에 대한 평가점수를 사용하여 검증하는 방법
# - 특정 알고리즘을 사용하여 데이터를 분석했을 떄
#   얻을 수 있는 평균적인 성능을 유추할 수 있음

# 1. 전체 데이터 셋 로딩
X, y = load_iris(return_X_y=True)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(X)
X = scaler.transform(X)

# 2. 데이터를 분석하기 위한 알고리즘(모델) 객체를 생성
model = LogisticRegression(solver='lbfgs', 
                           multi_class='multinomial')

# 교차검증 기능을 제공하는 cross_val_score 함수
# 하이퍼 파라메터
# cross_val_score(예측기 객체, X 데이터, y 데이터, 교차검증개수)
# 반환되는 값
# - 교차검증 개수에 정의된 크기의 예측기 객체가 생성되며
#   각 예측기의 평가 점수가 반환됨
#   (회귀 모델의 경우 R2 스코어가 반환
#   분류 모델의 경우 정확도가 반환됨)
from sklearn.model_selection import cross_val_score

# 3. 교차 검증의 수행
scores = cross_val_score(model, X, y, cv=10)

# 4. 교차 검증의 결과 확인
print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", 
      scores.mean())

















