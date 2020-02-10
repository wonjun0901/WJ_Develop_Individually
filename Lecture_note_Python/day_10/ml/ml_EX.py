# -*- coding: utf-8 -*-

"""
data 디렉토리에 저장된 diabetes.csv 파일을 사용하여
이진 분류를 위한 머신러닝 모델을 생성하세요.
생성된 모델의 평가점수(정확도)를 체크하세요.
"""

import pandas as pd

input_fname = './data/diabetes.csv'
diabetes = pd.read_csv(input_fname, header=None)

# pandas 옵션을 수정하여 
# 출력할 컬럼의 개수를 수정
pd.options.display.max_columns = 100
print(diabetes)

X = diabetes.iloc[:,:-1]
y = diabetes.iloc[:, -1]

# info 메소드
# - 전체 데이터의 개수, 각 데이터를 구성하는 컬럼의 개수
#   각 컬럼의 결측 데이터 유무, 각 컬럼의 데이터 타입을
#   확인할 수 있는 메소드
print(X.info())
# describe 메소드
# - 데이터프레임의 각 컬럼들에 대해서
#   간단한 통계정보를 확인할 수 있는 메소드
print(X.describe())

print(y.value_counts())
print(y.value_counts() / len(y))

# 데이터 분할(학습 / 테스트)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        test_size=0.3, stratify=y.values,
        random_state=10)

print(X_train.shape, X_test.shape)

# 트리구조를 기반으로 데이터를 분류할 수 있는
# DecisionTreeClassifier 클래스
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

# 학습 데이터를 사용하여 머신러닝 모델을 학습
model.fit(X_train, y_train)

# 모델의 성능 평가
# - 학습 데이터에 대한 평가
print('학습 평가 : ', model.score(X_train, y_train))

# - 테스트 데이터에 대한 평가
print('테스트 평가 : ', model.score(X_test, y_test))

















