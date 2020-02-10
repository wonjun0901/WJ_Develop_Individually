# -*- coding: utf-8 -*-

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(\
     cancer.data, cancer.target, 
     stratify=cancer.target, random_state=0)

clf = GradientBoostingClassifier(random_state=0, 
                                 n_estimators=1500,
                                 max_depth=3, 
                                 learning_rate=0.01, 
                                 subsample=0.5)
clf.fit(X_train, y_train)

print("훈련 세트 정확도: {:.3f}".format(clf.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(clf.score(X_test, y_test)))

import os
import pickle

try:
    if not(os.path.isdir("../../save")):
        os.makedirs(os.path.join("../../save"))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise
        
with open("../../save/save_model_using_pickle.bin", "wb") as f :
    pickle.dump(clf, f)















