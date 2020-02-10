# -*- coding: utf-8 -*-

import pandas as pd

# 손글씨 이미지 데이터 셋
# - 각 샘플은 8 * 8 크기의 이미지를 나타냄
from sklearn.datasets import load_digits

digits = load_digits()

print(digits.keys())
print(digits.target_names)
print(digits.images[0])

from matplotlib import pyplot as plt

plt.gray()
plt.matshow(digits.images[50])
plt.show()

print(digits.target[50])

X = pd.DataFrame(digits.data)
y = pd.Series(digits.target)

print(X.describe())
print(y.value_counts() / len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y, random_state=1)

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

best_model = None
best_max_depth = None
best_f1_score = None

max_depth = 3

while max_depth <= 10 :
    model = RandomForestClassifier(
            n_estimators=1000,
            max_features=8,
            max_depth=max_depth, 
            random_state=1,
            n_jobs=-1).fit(X_train, y_train)
    
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
    n_features = digits.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')    
    plt.xlabel("feature_importances")
    plt.ylabel("feature")
    plt.ylim(-1, n_features)

plot_feature_importances(model)






















