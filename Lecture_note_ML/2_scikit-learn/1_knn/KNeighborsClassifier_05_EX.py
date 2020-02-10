# -*- coding: utf-8 -*-

# data 디렉토리에 저장된 diabetes.csv 파일의 데이터를
# KNN 알고리즘을 사용하여 분석한 후, 
# 정확도와 각 클래스 별 확률을 출력하세요.

import pandas as pd

fname = '../../data/diabetes.csv'

# csv 파일의 첫번째 행으로 각 컬럼의 제목(헤더)이 
# 존재하지 않는 경우
# 1번째 행의 데이터가 제목으로 지정되기 때문에
# 아래와 같이 header 정보를 None으로 지정합니다.
diabetes = pd.read_csv(fname, header=None)

# 데이터 확인(앞의 5개)
print(diabetes.head())

# 특성 데이터 추출
X = diabetes.iloc[:,:-1]
# 라벨 데이터 추출
y = diabetes.iloc[:, -1]

# 특성 데이터의 확인
# 1. 전체 데이터 개수, 특성(컬럼)의 개수
#    결측 데이터의 유무 확인
print(X.info())
# 2. 특성 데이터의 스케일 확인
pd.options.display.max_columns=100
print(X.describe())

# 라벨 데이터의 확인
# - 정답의 편향(분포)을 확인
print(y.value_counts())
print(y.value_counts() / len(y))

# 데이터 분할(학습/테스트)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        test_size=0.3,
        stratify=y.values,
        random_state=1)

# 학습 및 테스트 데이터의 개수 확인
print(f"TRAIN's SIZE : {len(X_train)}")
print(f"TEST's SIZE : {len(X_test)}")

# 데이터 분석을 위해 사용할 모델의 생성 및 학습
from sklearn.neighbors import KNeighborsClassifier
# 모델의 하이퍼 파라메터 정보를 변수로 선언
K = 3
# 모델 객체의 생성과 학습
#model = KNeighborsClassifier(n_neighbors=K)
#model.fit(X_train, y_train)

# 모델 객체의 생성과 학습을 동시에 진행할 수 있음
# (사이킷 런의 모든 예측기 클래스의 fit 메소드는
# X 데이터의 형태를 2차원으로 
# y 데이터의 형태를 1차원으로 간주함)
model = KNeighborsClassifier(n_neighbors=K).fit(X_train, y_train)

# 모델 평가
# score 메소드
# - 분류 예측기 : 정확도를 반환
# - 회귀 예측기 : R2Score(결정계수)를 반환
print("학습 평가 : ", model.score(X_train, y_train))
print("테스트 평가 : ", model.score(X_test, y_test))

# 사이킷 런의 평가 함수를 사용한 정확도 확인
# - 예측 값에 대한 정확도 확인
# - accuracy_score(실제정답, 예측값)
from sklearn.metrics import accuracy_score

# 학습 데이터의 예측 결과를 사용하여 정확도 확인
pred_train = model.predict(X_train)
print("학습 데이터의 정확도 : ", 
      accuracy_score(y_train, pred_train))

# 테스트 데이터의 예측 결과를 사용하여 정확도 확인
pred_test = model.predict(X_test)
print("테스트 데이터의 정확도 : ", 
      accuracy_score(y_test, pred_test))

# 예측 확률 값 확인
pred_test = model.predict(X_test[:5])
pred_proba = model.predict_proba(X_test[:5])
print("예측 확률\n", pred_proba)
print("예측 정답\n", pred_test)
print("실제 정답\n", y_test[:5])














