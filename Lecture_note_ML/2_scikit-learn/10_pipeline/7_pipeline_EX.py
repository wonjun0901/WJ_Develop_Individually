# -*- coding: utf-8 -*-

# Pipeline 클래스와 GridSearchCV 클래스를 활용하여
# winequality-red.csv 파일을 분석한 후 결과를 확인하세요.

# 1. 데이터의 적재 및 분할
import pandas as pd

fname = '../../data/winequality-red.csv'
wine = pd.read_csv(fname, sep=';')

X = wine.iloc[:,:-1]
y = wine.iloc[:, -1]

print(X[:3])
pd.options.display.max_columns=100
print(X.describe())

print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y.values, 
                     random_state=1)
    
# 2. 데이터의 전처리와 모델의 학습을 자동화할 수 있는
#   파이프라인 객체 생성
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier

pipe = Pipeline([('scaler', StandardScaler()), 
                   ('gbc', GradientBoostingClassifier(n_estimators=10000))])

from sklearn.model_selection import GridSearchCV

param_grid = {'gbc__max_depth' : 
    [1,2,3,4,5],
              'gbc__max_features' : 
    [0.1,0.2,0.3,0.4,0.5],
              'gbc__subsample' : 
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7]}

grid = GridSearchCV(pipe, param_grid=param_grid, 
                    cv=3, iid=True, n_jobs=-1)
grid.fit(X_train, y_train)

print("Best 교차 검증 점수 : ", grid.best_score_)
print("최적의 하이퍼 파라메터 : ", grid.best_params_)

# 4. 학습된 머신러닝 모델의 평가
print("학습 결과 : ", grid.score(X_train, y_train))
print("테스트 결과 : ", grid.score(X_test, y_test))

from sklearn.metrics import classification_report
print("학습 데이터의 정밀도, 재현율, F1")
print(classification_report(y_train, 
                            grid.predict(X_train)))
print("테스트 데이터의 정밀도, 재현율, F1")
print(classification_report(y_test, 
                            grid.predict(X_test)))


















