# -*- coding: utf-8 -*-

# Data 디렉토리에 저장된 diabetes.csv 파일의 데이터를
# 분석하여 정확도 및 정밀도, 재현율을 출력하세요.
# (LogisticRegression 클래스를 활용하되, C의 값과 penalty를
# 제어하여 결과를 확인)

import pandas as pd

fname = '../../../../data/diabetes.csv'
diabetes = pd.read_csv(fname, header=None)

# X : DataFrame
X = diabetes.iloc[:,:-1]
# y : Series
y = diabetes.iloc[:, -1]

print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        test_size=0.3, stratify=y.values,
        random_state=1)

print(X_train.shape[0] / len(X))
print(X_test.shape[0] / len(X))

from sklearn.linear_model import LogisticRegression

best_model = None
best_C = None
best_f1_score = None

# f1-score 의 값을 반환할 수 있는 함수
from sklearn.metrics import f1_score

C = 0.01
while C <= 100 :
    
    model = LogisticRegression(C=C, solver='lbfgs',
                               max_iter=10000).fit(
                                       X_train, y_train)

    pred = model.predict(X_train)
    f1 = f1_score(y_train, pred)
    
    if best_f1_score == None or best_f1_score < f1 :
        best_f1_score = f1
        best_C = C
        best_model = model
    
    C += 0.01

print('최적 모델의 파라메터 정보 : \n', best_model.get_params())

print('훈련평가(LR) : ', 
      best_model.score(X_train,y_train))
print('테스트평가(LR) : ', 
      best_model.score(X_test,y_test))

from sklearn.metrics import confusion_matrix
pred_train = best_model.predict(X_train)
pred_test = best_model.predict(X_test)

print('confusion_matrix - 학습')
print(confusion_matrix(y_train, pred_train))

print('confusion_matrix - 테스트')
print(confusion_matrix(y_test, pred_test))

from sklearn.metrics import classification_report

print('classification_report - 학습')
print(classification_report(y_train, pred_train))

print('classification_report - 테스트')
print(classification_report(y_test, pred_test))














