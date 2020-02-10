# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

# KNN 알고리즘 (K-Nearest Neighbor)
# K-최근접 이웃 
# 데이터 간 거리를 측정하여 가장 가까운 K개의 이웃의 
# 결과 데이터 중 빈도수가 높은 결과로 추론하는 알고리즘
# 단순하지만 여러 응용 분야에서 활용되고 있으며,
# 검색 및 추천 시스템에서도 활용됨
# 검색할 이웃의 개수(k)의 값을 매개변수로 지정하며
# 동률인 경우를 제거하기 위해서 일반적으로 홀수로 지정함

# 게으른 학습 방법을 지향하는 KNN
# 일반적인 머신러닝 알고리즘과는 달리 
# 사전에 데이터를 학습하지 않고, 저장만 함
# 실제 예측을 하는 시점(predict 메소드 실행)에
# 각 데이터들을 순회하며 예측을 생성함

# 신장과 몸무게의 데이터를 저장하는 X 데이터
X_train = np.array([
        [158, 64],
        [170, 86],
        [183, 84],
        [191, 81],
        [155, 49],
        [163, 59],
        [180, 67],
        [158, 54],
        [170, 67]])

y_train = np.array(['male', 'male', 'male', 'male',
                    'female', 'female', 'female', 
                    'female', 'female'])

#plt.figure(figsize=(10,7))
#plt.title('Heights & Weights')
#plt.xlabel('Height (cm)')
#plt.ylabel('Weight (kg)')
#
#for i, x in enumerate(X_train) :
#    plt.scatter(x[0], x[1], c='k',
#                marker='x' if y_train[i] == 'male' else 'D')
#    
#plt.grid(True)
#plt.show()

# 예측에 사용할 테스트 데이터 생성
X_test = np.array([[155,70]])

# KNN 알고리즘을 구현하고 있는 분류를 위한 클래스의 로딩
from sklearn.neighbors import KNeighborsClassifier

# 탐색을 위한 이웃의 개수를 변수로 지정
K = 3

# KNeighborsClassifier의 객체(모델)을 생성 시
# 최근접 이웃의 개수를 생성자로 전달
# (기본값은 5)
model = KNeighborsClassifier(n_neighbors=K)

# fit 메소드를 사용하여 학습 데이터를 학습
# 별도의 학습을 진행하지 않고 저장함(게으른 학습 방법)
model.fit(X_train, y_train)

# predict 메소드를 사용하여 예측 결과를 반환받음
predicted = model.predict(X_test)
print(predicted)

plt.figure(figsize=(10,7))
plt.title('Heights & Weights')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

for i, x in enumerate(X_train) :
    plt.scatter(x[0], x[1], c='k',
                marker='x' if y_train[i] == 'male' else 'D')

plt.scatter(X_test[0,0], X_test[0,1], 
            c='r', marker='v')

plt.grid(True)
plt.show()

# 각 클래스 별 예측 확률을 확인
predicted_proba = model.predict_proba(X_test)
print(predicted_proba)

# 사이킷 런의 모든 분류를 위한 예측기 클래스들은
# 분류할 클래스의 정보를 classes_ 변수에 저장함
# predict 메소드는 predict_proba 메소드의 실행 결과에서
# 가장 높은 확률 값의 인덱스를 classes_ 변수에 적용하여
# 값을 반환하는 메소드
print(model.classes_)

















