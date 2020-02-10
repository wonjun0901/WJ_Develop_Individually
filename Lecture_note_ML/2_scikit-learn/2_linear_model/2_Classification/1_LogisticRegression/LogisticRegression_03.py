# -*- coding: utf-8 -*-

from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, random_state=1)

print(X_train.shape[0], X_test.shape[0])

from sklearn.linear_model import LogisticRegression

# LogisticRegression 클래스는 기본 제약조건으로 
# L2 정규화를 지원
# penalty 하이퍼 파라메터의 값을 'l1'으로 변경하면 
# 모델의 제약조건을 L1 정규화로 변경할 수 있습니다.
# C의 값을 높일수록 제약의 강도가 낮아지며
# (일부 특성 데이터의 가중치의 값만이 0으로 수렴)
# C의 값은 낮출수록 제약의 강도가 높아집니다.
# (대다수 특성 데이터의 가중치의 값이 0으로 수렴)

from matplotlib import pyplot as plt

plt.figure(figsize=(10,7))

for C, marker in zip([0.01, 1, 100],['o', '^', 'v']) :
    model = LogisticRegression(C=C, solver='liblinear',
                               penalty='l1', 
                               max_iter=10000).fit(
                                       X_train, y_train)
    
    print(f'C({C}) - 학습 : {model.score(X_train, y_train)}')
    print(f'C({C}) - 테스트 : {model.score(X_test, y_test)}')
    
    plt.plot(model.coef_.T, marker, label=f'C={C:.2f}')
plt.legend()
plt.show()















