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

# 사이킷 런을 사용하지 않고 최근접 이웃알고리즘을 구현하는 예제

# 예측에 사용할 테스트 데이터 생성
X_test = np.array([[155,70]])

# 최근접 이웃 알고리즘이 거리를 계산할 때 사용하는 방법
# - 유클리드 거리 계산법을 적용함
# - 테스트 데이터와 학습 데이터 사이의 유클리드 거리 계산
# - (T1, T2)와 (R1, R2) 사이의 유클리드 거리 계산법
# - A = ((T1 - R1)의 제곱 + (T2 - R2)의 제곱) 
# - 유클리드 거리 = A의 제곱근
distances_step1 = X_train - X_test
print(distances_step1)

distances_step2 = distances_step1 ** 2
print(distances_step2)

# np.sum 함수 : 매개변수의 총 합계를 구하는 함수
# axis 매개변수의 값을 지정하지 않으면 전체 함계가 반환
# axis = 0 인경우 열의 함계를 반환
# axis = 1 인경우 행의 함계를 반환
distances_step3 = np.sum(distances_step2, axis=1)
print(distances_step3)

# np.sqrt 함수 : 매개변수의 제곱근 값을 반환
distances = np.sqrt(distances_step3)
print('테스트 데이터에 대한 거리 계산 결과\n', distances)

# 테스트 데이터와 가장 가까운 학습 데이터 3개의 인덱스 추출
# numpy 배열의 argsort 메소드
# 배열 내부를 오름차순으로 정렬했을때의 인덱스 값을 반환
# 내림차순의 경우 argsort()[::-1][:3]
nearest_indices = distances.argsort()[:3]
print('가장 가까운 데이터의 인덱스(3개)\n', nearest_indices)

# 테스트 데이터와 가장 가까운 학습 데이터 3개의 
# 인덱스를 활용하여 각 학습 데이터의 정답 데이터를 추출
# np.take 함수는 1번째 매개변수로 전달된 배열로부터
# 2번째 매개변수로 전달된 인덱스에 해당되는 요소를 반환
nearest_genders = np.take(y_train, nearest_indices)
print('가장 가까운 데이터의 라벨(3개)\n', nearest_genders)

# 내부 데이터의 개수를 확인할 수 있는 Counter 클래스
# (중복을 제거시킨 각 값의 개수를 확인할 수 있음)
from collections import Counter
counter = Counter(nearest_genders)
print(counter)
print(counter.most_common())
print(counter.most_common()[0][0])

# 예측 확률 값을 출력
K = 3
print(counter.most_common()[0][1] / K)
print(counter.most_common()[1][1] / K)













