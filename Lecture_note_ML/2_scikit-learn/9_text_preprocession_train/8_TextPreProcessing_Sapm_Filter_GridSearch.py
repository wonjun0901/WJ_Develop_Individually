# -*- coding: utf-8 -*-

# GridSearchCV 클래스를 사용하여
# SMSSpamCollection 파일을 분석할 수 있는 
# 최적의 모델을 검색하여 분석 결과를 출력하세요.

import pandas as pd

fname = '../../data/SMSSpamCollection'
sms = pd.read_csv(fname, header=None, sep='\t')

X_raw = sms.iloc[:,-1]
y = sms.iloc[:,0]

print(X_raw[:5])
print(y[:5])

print(y.value_counts())
print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train_raw, X_test_raw, y_train, y_test = \
    train_test_split(X_raw.values, y.values, 
                     stratify=y.values, random_state=0)
    
print(X_train_raw.shape[0], X_test_raw.shape[0])

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
        stop_words='english', min_df=2).fit(X_train_raw)

print("토큰 개수 : ", len(vectorizer.vocabulary_))
print("변환 결과(희소행렬) : ", vectorizer.transform(X_train_raw))
print("변환 결과(밀집행렬) : ", vectorizer.transform(X_train_raw).toarray())

X_train = vectorizer.transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

# 스팸(0), 햄(1) 데이터를 분류하기 위한 예측기 객체 생성
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

# 교차 검증을 통해서 사전 평가
from sklearn.model_selection import KFold, cross_val_score
kfold = KFold(n_splits=10, shuffle=True, random_state=1)
score = cross_val_score(model, X_train, y_train, 
                        cv=kfold, n_jobs=-1).mean()

print('교차검증 결과 : ', score)

# 하이퍼 파라메터 검색을 통한 최적의 모델 검색
from sklearn.model_selection import GridSearchCV

param_grid = {'n_estimators':[100, 200, 300, 400, 500],
              'max_depth':[2,3,4,5],
              'max_features':[0.1,0.2,0.3,0.4,0.5]}

kfold = KFold(n_splits=10, shuffle=True, random_state=1)

model = RandomForestClassifier(n_jobs=-1)

grid_model = GridSearchCV(model, param_grid,
                          cv=kfold, iid=True, n_jobs=-1)

grid_model.fit(X_train, y_train)

# 모델 평가
print('학습 평가 : ', grid_model.score(X_train, y_train))
print('테스트 평가 : ', grid_model.score(X_test, y_test))

# 라벨 데이터의 편향이 심하므로
# 정밀도, 재현율을 확인해야함
from sklearn.metrics import classification_report
pred_train = grid_model.predict(X_train)
pred_test = grid_model.predict(X_test)

print('학습 결과 보고서')
print(classification_report(y_train, pred_train))

print('테스트 결과 보고서')
print(classification_report(y_test, pred_test))















