# -*- coding: utf-8 -*-

# data 디렉토리에 저장된 winequality-red.csv 파일의 
# 데이터를 로딩한 후, 학습을 위해서 분할하세요.

import pandas as pd

fname = '../../data/winequality-red.csv'
wine = pd.read_csv(fname, sep=';')

# X와 y데이터가 하나의 데이터프레임에 저장된 상태
print(wine.head())

# wine 데이터프레임에서 모든 행의 데이터 중
# 마지막 열을 제외한 데이터를 추출
# X -> DataFrame 타입
X = wine.iloc[:,:-1]
print(type(X))

# wine 데이터프레임에서 모든 행의 데이터 중
# 마지막 열만 추출
# y -> Series 타입
y = wine.iloc[:, -1]
print(type(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        test_size=0.3,
        random_state=10,
        stratify=y.values)

print('len(X_train) : ', len(X_train))
print('len(X_test) : ', len(X_test))












