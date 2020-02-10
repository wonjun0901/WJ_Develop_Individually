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
# 검증 데이터를 사용하여 평가를 실행하는 경우
# 데이터의 분할이 모델의 성능에 큰 영향을 끼치기 때문에
# 일반화 성능을 측정하기에 어려움이 있습니다.
# (데이터 분할의 형태에 따라 성능이 달라짐)
# 이러한 문제를 해결하기 위해서 교차검증을 사용할 수 있습니다.

# 데이터를 훈련 테스트 세트로 분할
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, stratify=y,
                     test_size=0.2,
                     random_state=1)
    
# 각 하이퍼 파라메터의 조합에 따른 최적의 평가 점수를
# 저장하기 위한 변수
best_score = 0

for gamma in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
    for C in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
        
        # 각 매개변수의 조합에 대해서 
        # SVC 모델 객체를 생성하여 훈련
        model = SVC(gamma=gamma, C=C)
        
        # 교차검증을 사용하여 SVC 모델을 평가        
        kfold = KFold(n_splits=5, shuffle=True, random_state=1)
        score = cross_val_score(model, X_train, 
                                y_train, cv=kfold).mean()
        
        if score > best_score :
            best_score = score
            best_parameters = {'gamma':gamma, 'C':C}
            
print("최고 점수: {:.2f}".format(best_score))
print("최적 파라미터: {}".format(best_parameters))

best_model = SVC(C=best_parameters['C'], 
                 gamma=best_parameters['gamma']).fit(X_train, y_train)
print("테스트 점수: {:.2f}".format(best_model.score(X_test, y_test)))































