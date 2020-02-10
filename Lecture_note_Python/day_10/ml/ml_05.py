# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/iris.csv'
iris = pd.read_csv(input_fname)

X = iris.iloc[:,:-1]
y = iris.iloc[:, -1]

print(y.value_counts())
print(y.value_counts() / len(y))

# 다항분류를 위한 머신클래스 import
# - 앙상블 기반으로 분류작업을 수행할 수 있는
#   RandomForestClassifier 클래스
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=150,
                               max_depth=1)

model.fit(X, y)

predicted = model.predict(X.iloc[:5])

print('예측 : \n', predicted)
print('정답 : \n', y.values[:5])

print('평가 : ', model.score(X, y))





















