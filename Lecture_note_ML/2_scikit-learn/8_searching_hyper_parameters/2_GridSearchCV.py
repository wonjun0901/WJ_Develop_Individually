# -*- coding: utf-8 -*-

# 최적의 하이퍼 파라메터를 검색하기 위한 예제
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cancer = load_breast_cancer()

X, y = cancer.data, cancer.target
X = MinMaxScaler().fit_transform(X)

modelCV = SVC(C=1.0, gamma='auto')

kfold = KFold(n_splits=5, shuffle=True, 
              random_state=1)
scores = cross_val_score(modelCV, X, y, cv=kfold)

print("교차 검증 점수 : ", scores)
print("교차 검증 점수의 평균 : ", scores.mean())

# 최적의 하이퍼 파라메터를 검색하기 위해서
# 학습 데이터를 사용하여 평가를 실행하는 경우
# 모델의 일반화 성능을 측정할 수 없습니다.
# (새로운 데이터에 대한 평가를 확인할 수 없음)
# 이러한 문제를 해결하기 위해서 일반적으로
# 전체 데이터를 학습/검증/테스트 데이터로 분할합니다.
# 일반적인 데이터의 비율
# 학습(70%), 검증(10%), 테스트(20%)

# 데이터를 훈련 및 검증 세트, 테스트 세트로 분할
X_raw, X_test, y_raw, y_test = \
    train_test_split(X, y, stratify=y,
                     test_size=0.2,
                     random_state=1)
    
# 훈련 및 검증 세트를 훈련 세트와 검증 세트로 분할
X_train, X_valid, y_train, y_valid = \
    train_test_split(X_raw, y_raw, stratify=y_raw,
                     test_size=0.15,
                     random_state=1)    
    
print("훈련 세트의 크기: {}\n검증 세트의 크기: {}\n테스트 세트의 크기:"
      " {}".format(X_train.shape[0], X_valid.shape[0], X_test.shape[0]))
    
# 각 하이퍼 파라메터의 조합에 따른 최적의 평가 점수를
# 저장하기 위한 변수
best_score = 0

for gamma in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
    for C in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
        
        # 각 매개변수의 조합에 대해서 
        # SVC 모델 객체를 생성하여 훈련
        model = SVC(gamma=gamma, C=C).fit(X_train, y_train)
        
        # 검증 세트를 사용하여 SVC 모델을 평가
        score = model.score(X_valid, y_valid)        
        
        if score > best_score :
            best_score = score
            best_parameters = {'gamma':gamma, 'C':C}
            
print("최고 점수: {:.2f}".format(best_score))
print("최적 파라미터: {}".format(best_parameters))

best_model = SVC(C=best_parameters['C'], 
                 gamma=best_parameters['gamma']).fit(X_train, y_train)
print("테스트 점수: {:.2f}".format(best_model.score(X_test, y_test)))































