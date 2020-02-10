# -*- coding: utf-8 -*-

from sklearn.datasets import make_blobs

X, y = make_blobs(random_state=42)

# 2개의 특성으로 구성된 X 데이터
print(X[:10])

# (0,1,2) 클래스로 구성된 y 데이터
print(y[:10])

from sklearn.svm import LinearSVC

# LinearSVC 클래스는 다항 분류를 지원하며, 
# 다항 분류를 위해서 일대다 방식을 적용
# - 각 클래스 별로 이진분류 모델을 생성하여
#   특성 데이터에 대한 각 이진분류 모델의 결과에서 
#   가장 큰 값을 취함
# - 아래의 계수 배열과 같은 경우 3개의 클래스를 예측하기 위해서
#   2개의 특성을 사용하므로 3 X 2 열의 배열이 생성되며,
#   절편의 값 또한 각 클래스 별로 계산되므로 
#   3 의 크기를 갖는 일차원 배열이 반환

model = LinearSVC(C=1, multi_class='ovr')
model.fit(X, y)

# 사이킷 런의 분류를 위해서 사용되는 예측기들은 
# 다항 분류를 지원하며, 다항 분류를 위해서 
# 일대다 방식을 적용
# - 각 클래스 별로 이진분류 모델을 생성하여
#   특성 데이터에 대한 각 이진분류 모델의 결과에서 
#   가장 큰 값을 취함
# - 아래의 계수 배열과 같은 경우 3개의 클래스를 
#   예측하기 위해서 2개의 특성을 사용하므로 
#   3 X 2 열의 배열이 생성되며,
#   절편의 값 또한 각 클래스 별로 계산되므로 
#   3 의 크기를 갖는 일차원 배열이 반환
print('가중치 배열의 크기 : ')
print(model.coef_.shape)

print('절편 배열의 크기 : ')
print(model.intercept_.shape)

print('학습 결과 : ', model.score(X, y))
print('예측 결과 : ', model.predict(X[:3]))

# 다항 분류의 경우 decision_function 메소드의 결과는
# 각 클래스를 구분하기 위한 방정식의 결과에서
# 양수/음수의 값을 반환함
# (양수인 경우 해당 클래스일 확률이 존재)
print(model.decision_function(X[:3]))



















