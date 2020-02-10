# -*- coding: utf-8 -*-

# 최적의 하이퍼 파라메터를 검색하기 위한 예제
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cancer = load_breast_cancer()

X, y = cancer.data, cancer.target
X = MinMaxScaler().fit_transform(X)

modelCV = SVC(C=1.0, gamma='auto')

kfold = KFold(n_splits=5, shuffle=True, 
              random_state=1)
scores = cross_val_score(modelCV, X, y, cv=kfold)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())

# 최적의 하이퍼 파라메터를 검색하기 위해서
# 검증 데이터를 사용하여 평가를 실행하는 경우
# 데이터의 분할이 모델의 성능에 큰 영향을 끼치기 때문에
# 일반화 성능을 측정하기에 어려움이 있습니다.
# (데이터 분할의 형태에 따라 성능이 달라짐)
# 이러한 문제를 해결하기 위해서 교차검증을 사용할 수 있습니다.

# 데이터를 훈련 테스트 세트로 분할
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, stratify=y,
                     test_size=0.2,
                     random_state=1)
    
param_grid = {
            'kernel' : ['rbf', 'linear', 'poly', 'sigmoid']
            ,'gamma' : [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            ,'C' : [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
            ,'coef0' : [0.0, 0.1, 0.2]
        }

# 조건부 매개변수를 사용하기 위한 매개변수 그리드 선언
# 사용 방식 
# - [{조건부 매개변수 1}, {조건부 매개변수 2} ... ]
param_grid = [{'kernel': ['rbf'],
               'C': [0.001, 0.01, 0.1, 1, 10, 100],
               'gamma': [0.001, 0.01, 0.1, 1, 10, 100]},
              {'kernel': ['linear'],
               'C': [0.001, 0.01, 0.1, 1, 10, 100]}]

print('매개변수 그리드 : ', param_grid)

from sklearn.model_selection import GridSearchCV

kfold = KFold(n_splits=5, shuffle=True, random_state=1)

grid_search = GridSearchCV(SVC(), param_grid, 
                           cv=kfold, iid=True, n_jobs=-1)

grid_search.fit(X_train, y_train)

print('테스트 평가 : ', grid_search.score(X_test, y_test))

print('최적의 하이퍼 파라메터 : \n', 
      grid_search.best_params_)

print('최고의 교차 검증 점수 : \n', 
      grid_search.best_score_)

print('최고의 성능 모델 : \n', 
      grid_search.best_estimator_)
























