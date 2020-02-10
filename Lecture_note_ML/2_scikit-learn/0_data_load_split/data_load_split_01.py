# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_iris

# 사이킷 런에서 제공하는 훈련데이터 로딩
iris = load_iris()

print(iris.keys())

# 분류 데이터인 경우 예측한 결과의
# 이름을 확인할 수 있도록 target_names
# 키가 제공됨
print(iris.get("target_names"))

# 입력(특성) 데이터
X = pd.DataFrame(iris["data"])
# X = pd.DataFrame(iris.data) 도 가능함. but, vscode에서 특히 linting과정에서 오류를 보여주고 있음.
print(X.head())
# 정답(라벨) 데이터
y = pd.Series(iris["target"])

# 입력(특성) 데이터의 개수 및 타입,
# 결측 데이터 확인
print(X.info())

# 입력(특성) 데이터의 통계 수치
print(X.describe())

# 정답(라벨) 데이터의 편향 정도 확인
# (분류용 데이터의 경우 반드시 확인)
# (회귀용 데이터의 경우 X)
print(y.value_counts())
print(y.value_counts() / len(y))

# 학습 전 단계
# 1. 데이터의 분할
# - 학습 데이터, 테스트 데이터, 검증 데이터
# - 학습 데이터 : 머신러닝 모델이 학습할 데이터
# - 테스트 데이터 : 학습이 종료된 머신러닝 모델이
#  정답을 예측하기 위한 데이터
#  (머신러닝 모델의 일반화 정도를 판단하는 기준이 됨)
# - 검증 데이터 : 딥러닝 모델과 같이 단계별로 학습을
#   진행하는 경우 일정 단계에서 검증을 위한 목적으로
#   사용되는 데이터
#   학습데이터의 정확도와 검증데이터 정확도의 추이를
#   비교하여 학습 도중 과적합 여부를 판단
# - 학습(70%), 테스트(20%), 검증(10%)

# 일반적인 데이터 분할
# - 순차적으로 데이터를 분할하는 방법
size = len(X)
X_train = X.iloc[:int(size * 0.7)]
X_test = X.iloc[int(size * 0.7):int(size * 0.9)]
X_valid = X.iloc[int(size * 0.9):]

print(f'{len(X_train)}, {len(X_test)}, {len(X_valid)}')

y_train = y.iloc[:int(size * 0.7)]
y_test = y.iloc[int(size * 0.7):int(size * 0.9)]
y_valid = y.iloc[int(size * 0.9):]

print(f'{len(y_train)}, {len(y_test)}, {len(y_valid)}')

# 순차적으로 데이터를 분할하는 경우의 문제점
# - 라벨 데이터의 편향 현상이 발생할 수 있음
print('테스트 라벨 데이터 : \n', y_test)
print('검증 라벨 데이터 : \n', y_valid)

# 사이킷 런의 데이터 분할을 위해서 제공되는
# train_test_split 함수

# train_test_split 함수의 사용법
# train_test_split(X, y, 추가적인 파라메터정보...)

# test_size : 테스트 데이터 셋의 비율(실수의 값 사용)
# - 0.3이 입력되는 경우, 학습데이터 70%.
#   테스트데이터 30%가 반환
# - test_size 를 지정하지 않은 경우
#   학습데이터 75%. 테스트데이터 25%가 반환

# random_state : 난수 발생의 seed 값을 의미
# - 동일한 데이터와 동일한 random_state 정보가 대입되면
#   항상 동일한 데이터 셋이 반환되도록 보장할 수 있음
#   (다수번의 학습 시 비교를 수월하게 진행할 수 있음)

# stratify : 데이터 셋이 분류 데이터인 경우에만 사용
# - 라벨 데이터의 비율을 전체 데이터 셋에 근사하여 반환

# train_test_split 함수의 반환 값
# X_train(학습할 입력데이터), X_test(테스트할 입력데이터),
# y_train(학습할 라벨데이터), y_test(테스트할 라벨데이터)
# = train_test_split(...)

# 실제 사용 예
# - pandas 데이터 프레임에서 numpy 배열을 반환받는 방법
# - values 속성을 사용하여 numpy 배열을 반환받을 수 있음
# 주의 사항
# - 사이킷런의 모든 학습을 위한 클래스들은
#  입력 데이터는 2차원 배열, 라벨 데이터는 1차원으로 가정
X_train, X_test, y_train, y_test = train_test_split(
    X.values, y.values,
    test_size=0.3,
    random_state=1,
    stratify=y)

# 입력 데이터의 분할 비율을 확인
print(f'{len(X_train)}, {len(X_test)}')
print(f'{len(y_train)}, {len(y_test)}')

# 라벨 데이터의 분할 정보 확인
print('테스트 라벨 데이터 : \n', y_test)
