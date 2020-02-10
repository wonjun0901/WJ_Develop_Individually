# -*- coding: utf-8 -*-

import pandas as pd

fname = '../../data/score.csv'
data = pd.read_csv(fname)

X = data.iloc[:, [0,2,3,4,5]]
y = data.iloc[:, 1]

print(X)
print(y)

# 데이터 샘플의 수가 적으므로 분할 과정을 생략

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector (BaseEstimator, TransformerMixin) :
    def __init__(self, attr_names) :
        # 데이터프레임에서 추출할 컬럼명의 리스트
        self.attr_names = attr_names
        
    def fit(self, X, y=None) :
        return self
    
    def transform(self, X) :        
        # 데이터프레임에서 생성자로 전달받은
        # 컬럼명의 데이터들을 numpy 배열로 반환
        return X[self.attr_names].values
    
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

pipe = Pipeline(
        [('selector', 
          DataFrameSelector(
                  attr_names=['iq', 'academy', 'game', 'tv'])), 
        ('scaler', MinMaxScaler()), 
        ('lr', LinearRegression())])

pipe.fit(X, y.values)
    
print("평가 : ", pipe.score(X, y.values))
    
    
    
    






    
    
    
    