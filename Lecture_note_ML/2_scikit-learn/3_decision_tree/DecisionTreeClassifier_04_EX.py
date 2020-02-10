# -*- coding: utf-8 -*-

# Data 디렉토리에 저장된 winequality-white.csv 파일의 데이터를
# DecisionTreeClassifier 를 사용하여 분석한 후
# 정확도 및 정밀도, 재현율을 출력하세요.
# (그래프의 정보를 시각화하여 확인하세요.)

import pandas as pd

fname = '../../data/winequality-white.csv'
wine = pd.read_csv(fname, sep=';')

print(wine.head())

X = wine.iloc[:,:-1]
y = wine.quality

print(X.info())

pd.options.display.max_columns=100
# 데이터의 스케일 조정이 필요한 모습을 확인할 수
# 있지만, 트리 기반의 알고리즘을 사용하기 때문에
# 전처리를 할 필요가 없음.
print(X.describe())

print(y.value_counts())
print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X.values, y.values,
        stratify=y.values, random_state=1)

print(X_train.shape[0], X_test.shape[0])

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
        max_depth=20, random_state=1).fit(
                X_train, y_train)

print('학습 평가 : ', model.score(X_train, y_train))
print('테스트 평가 : ', model.score(X_test, y_test))

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report
print('confusion_matrix : 학습\n')
print(confusion_matrix(y_train, pred_train))

print('confusion_matrix : 테스트\n')
print(confusion_matrix(y_test, pred_test))

print('classification_report : 학습\n')
print(classification_report(y_train, pred_train))

print('classification_report : 테스트\n')
print(classification_report(y_test, pred_test))

from sklearn.tree import export_graphviz

export_graphviz(model, out_file='wine_tree.dot',
                class_names=['3','4','5','6','7','8','9'],
                feature_names=wine.columns[:-1],
                filled=True)

import graphviz
from IPython.display import display

with open('wine_tree.dot', encoding='utf-8') as f :
    dot_graph = f.read()

display(graphviz.Source(dot_graph))



























