# -*- coding: utf-8 -*-

from joblib import load
# 학습된 모델 객체를 복원
model = load("../../save/save_model_using_joblib_iris.joblib")
# 라벨 데이터의 인코딩 객체를 복원
encoder = load("../../save/save_model_using_joblib_iris_encoder.joblib")

import pandas as pd

fname = '../../data/iris.csv'
iris = pd.read_csv(fname)

X = iris.iloc[:,:-1]
y = iris.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y.values, random_state=1)

print("훈련 세트 정확도: {:.3f}".format(
        model.score(X_train, encoder.transform(y_train))))
print("테스트 세트 정확도: {:.3f}".format(
        model.score(X_test, encoder.transform(y_test))))







https://tensorflow.org

















