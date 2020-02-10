# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 데이터 생성
class_0 = np.array([[1,2],[3,5],[2,7],[5,5],[4,3]])
class_1 = class_0 + 5

# 라벨 데이터 생성
label = np.r_[np.zeros([len(class_0)]), 
              np.ones([len(class_1)])]

# 테스트 데이터 생성
test = np.array([[8,9]])

# 산점도 차트 출력
# 라벨이 0인 데이터를 파란색으로
# 1인 데이터를 초록색으로 출력
plt.scatter(class_0[:,0], class_0[:,1], c='b')
plt.scatter(class_1[:,0], class_1[:,1], c='g')
plt.scatter(test[:,0], test[:,1], c='r')
plt.show()

# X 데이터의 통합
X_0 = pd.DataFrame(class_0)
X_1 = pd.DataFrame(class_1)
X = pd.concat([X_0,X_1], ignore_index=True)

# 라벨데이터 저장
y = pd.Series(label)

# 최근접 이웃 알고리즘을 구현하고 있는
# 사이킷 런의 예측기 클래스 사용
from sklearn.neighbors import KNeighborsClassifier

# 머신러닝 예측기 객체의 생성
model = KNeighborsClassifier(n_neighbors=7)

# 머신러닝 예측기 객체의 데이터 학습
model.fit(X.values, y.values)

# 머신러닝 예측기 객체의 학습 결과 확인
accuracy = model.score(X.values, y.values)
print("학습 결과 : ", accuracy)

# 머신러닝 예측기를 사용하여 데이터를 예측
predicted = model.predict(test)
print("예측 결과 : ", predicted)
























