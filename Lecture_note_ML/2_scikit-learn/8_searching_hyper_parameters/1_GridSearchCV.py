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

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, stratify=y,
                     random_state=1)

# 각 하이퍼 파라메터의 조합에 따른 최적의 평가 점수를
# 저장하기 위한 변수
best_score = 0

for gamma in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
    for C in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000] :
        
        # 각 매개변수의 조합에 대해서 
        # SVC 모델 객체를 생성하여 훈련
        model = SVC(gamma=gamma, C=C).fit(X_train, y_train)
        
        # 학습 세트를 사용하여 SVC 모델을 평가
        score = model.score(X_train, y_train)
        
        # 테스트 세트를 사용하여 SVC 모델을 평가
        # - 테스트 세트를 사용하여 모델을 평가하는 경우
        #   최종적인 결과를 미리보고 모델을 선택하게 되므로
        #   테스트 세트는 최종적인 확인을 위해서만 사용해야함
        # score = model.score(X_test, y_test)
        
        if score > best_score :
            best_score = score
            best_parameters = {'gamma':gamma, 'C':C}
            
print("최고 점수: {:.2f}".format(best_score))
print("최적 파라미터: {}".format(best_parameters))

best_model = SVC(C=best_parameters['C'], 
                 gamma=best_parameters['gamma']).fit(X_train, y_train)
print("테스트 점수: {:.2f}".format(best_model.score(X_test, y_test)))































