# -*- coding: utf-8 -*-

from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, random_state=1)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
        random_state=1, max_depth=3).fit(X_train, y_train)

print('학습 결과 : ', 
      model.score(X_train, y_train))
print('테스트 결과 : ', 
      model.score(X_test, y_test))

# 결정트리 모델의 학습 결과를 시각화하기 위한 설정
# 1. 현재 운영체제에 맞는 graphviz 설치 
# - http://www.graphviz.org/
# 2. PATH 등록
# - graphviz 설치된 디렉토리의 bin 경로
# - C:\Program Files (x86)\Graphviz2.38\bin
# - 사용자 변수, 시스템 변수 모두의 Path 변수에 경로 추가
# 3. graphviz 파이썬 모듈 설치
# - pip install graphviz

from sklearn.tree import export_graphviz

cancer = load_breast_cancer()
# export_graphviz 함수를 사용하여
# 결정 트리의 학습된 결과를 파일로 출력
# - graphviz 의 파일 포맷으로 출력
export_graphviz(model, out_file='cancer_tree.dot',
                class_names=['악성', '양성'],
                feature_names=cancer.feature_names,
                filled=True)

import graphviz
from IPython.display import display

with open('cancer_tree.dot', encoding='utf-8') as f :
    dot_graph = f.read()

display(graphviz.Source(dot_graph))
































