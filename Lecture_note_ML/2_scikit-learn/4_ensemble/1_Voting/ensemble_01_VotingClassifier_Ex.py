# -*- coding: utf-8 -*-

# winequality-red.csv 데이터를 LogisticRegression, KNeighborsClassifier, 
# DecisionTreeClassifier를 조합한 VotingClassifier로 분석한 후, 
# 결과를 확인하세요.

import pandas as pd

fname='../../../data/winequality-red.csv'
data = pd.read_csv(fname, sep=';')

X = data.iloc[:, :-1]
y = data.iloc[:,  -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X.values, y.values, 
                     stratify=y, random_state=1)
    
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

lr_model = LogisticRegression(
        solver='lbfgs', multi_class='multinomial',
        max_iter=10000)
knn_model = KNeighborsClassifier(n_neighbors=3)
tree_model = DecisionTreeClassifier()
ensemble_model = VotingClassifier(
        estimators=[('lr', lr_model), ('knn', knn_model), ('tree', tree_model)])

lr_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
ensemble_model.fit(X_train, y_train)

print("LogisticRegression 평가(train) : ", lr_model.score(X_train, y_train))
print("KNeighborsClassifier 평가(train) : ", knn_model.score(X_train, y_train))
print("DecisionTreeClassifier 평가(train) : ", tree_model.score(X_train, y_train))
print("VotingClassifier 평가(train) : ", ensemble_model.score(X_train, y_train))

print("=" * 35)

print("LogisticRegression 평가(test) : ", lr_model.score(X_test, y_test))
print("KNeighborsClassifier 평가(test) : ", knn_model.score(X_test, y_test))
print("DecisionTreeClassifier 평가(test) : ", tree_model.score(X_test, y_test))
print("VotingClassifier 평가(test) : ", ensemble_model.score(X_test, y_test))

















