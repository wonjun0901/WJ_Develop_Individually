# -*- coding: utf-8 -*-

# 데이터 전처리
# 데이터 분석을 위한 데이터 처리 과정
# - 전체 데이터 셋에서 데이터 분석에 사용될 열 선정
#   (pandas의 iloc, loc 연산을 사용하여 처리)
# - 특정 열에 존재하는 빈 값을 제거하거나
#   또는 특정 열에 존재하는 빈 값을 임의의 값으로 변경
#   (결측데이터에 대한 처리)
# - 데이터의 스케일(값의 범위) 조정
# - 범주형 변수의 값 변경
#   (문자열 값의 수치 데이터화)
#   (원핫인코딩 처리)
# - 학습, 테스트 데이터 분할

# 결측 데이터
# 각각의 샘플내에 포함된 특성의 값이 존재하지 않은 경우를 의미
# 결측 데이터가 존재하는 경우 학습이 원활하게 진행되지 않기 때문에
# 머신러닝 모델의 학습 전에 반드시 결측 데이터를 해결해야함

import pandas as pd

fname = "../../data/diabetes.csv"
diabetes = pd.read_csv(fname, header=None)
diabetes.columns = ['A','B','C','D','E','F','G','H','I']

# 데이터의 특성개수 및 결측 데이터 여부 확인
print(diabetes.info())

# 1행 1열과 2행 1열에 None(np.NaN)값을 대입
diabetes.iloc[[0,1], 0] = None
# 결측데이터가 존재하는 경우 데이터 샘플의 수가 
# 전체 데이터 샘플의 수와 다름을 확인할 수 있음
print(diabetes.info())
# 결측데이터는 NaN 값으로 확인됨
print(diabetes.head())

# 결측데이터를 삭제하는 방법은 많은 모듈에서 제공하고 있음
# - pandas를 사용하여 결측 데이터가 포함된 샘플을 
#  삭제하는 방법

# 결측데이터를 제거하기 위한 pandas 메소드
# dropna 메소드를 사용하여 NaN 데이터 삭제
# dropna 메소드의 axis 값을 0 또는 1로 지정
# 0 : 결측데이터가 포함된 행을 제거
# 1 : 결측데이터가 포함된 열을 제거
diabetes.dropna(axis=0)

# pandas의 dropna 메소드는 결측데이터가 포함된
# 행 또는 열을 제거한 새로운 DataFrame을 반환
# (원본 데이터는 수정되지 않음)
print(diabetes.head())

# inplace 매개변수를 True 로 지정하면
# 실제 삭제된 결과를 해당 데이터프레임에 
# 적용하고 어떤값도 반환하지 않습니다.
diabetes.dropna(axis=0, inplace=True)

# 결측데이터가 삭제된 것을 확인할 수 있음
print(diabetes.info())
print(diabetes.head(3))



























