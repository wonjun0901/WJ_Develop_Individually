# -*- coding: utf-8 -*-

# DecisionTreeClassifier 클래스를 사용하여 load_wine 데이터를 분석하고
# 정확도 및 정밀도, 재현율을 확인하세요.
# (DecisionTree의 그래프, 특성 중요도를 시각화하여 확인하세요)       

import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

X = pd.DataFrame(wine.data)
y = pd.Series(wine.target)

print(X.info())
print(X.describe())

print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y, random_state=1)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

best_model = None
best_max_depth = None
best_f1_score = None

max_depth = 3

while max_depth <= 10 :
    model = DecisionTreeClassifier(
            max_depth=max_depth, 
            random_state=1).fit(X_train, y_train)
    
    f1 = f1_score(y_test, 
                  model.predict(X_test), 
                  average='weighted')
    
    if best_f1_score == None or (best_f1_score != None and best_f1_score < f1) :
        best_model = model
        best_max_depth = max_depth
        best_f1_score = f1
        
    max_depth += 1

print('best_max_depth : ', best_max_depth)
print('best_f1_score : ', best_f1_score)
print("학습 평가 : ", best_model.score(X_train, y_train))
print("테스트 평가 : ", best_model.score(X_test, y_test))

print("특성 중요도 : ", model.feature_importances_)

import numpy as np
from matplotlib import pyplot as plt

def plot_feature_importances(model):
    n_features = wine.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), wine.feature_names)
    plt.xlabel("feature_importances")
    plt.ylabel("feature")
    plt.ylim(-1, n_features)

plot_feature_importances(model)

from sklearn.tree import export_graphviz
wine.target_names
# export_graphviz 함수를 사용하여
# 결정 트리의 학습된 결과를 파일로 출력
# - graphviz 의 파일 포맷으로 출력
export_graphviz(model, out_file='load_wine_tree.dot',
                class_names=wine.target_names,
                feature_names=wine.feature_names,
                filled=True)

import graphviz
from IPython.display import display

with open('load_wine_tree.dot', encoding='utf-8') as f :
    dot_graph = f.read()

display(graphviz.Source(dot_graph))


















