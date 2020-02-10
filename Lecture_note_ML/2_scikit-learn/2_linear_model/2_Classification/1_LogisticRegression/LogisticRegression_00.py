# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

X = np.arange(1, 11).reshape(-1, 1)
y = np.r_[np.zeros(5), np.ones(5)]

print(X)
print(y)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='lbfgs').fit(X, y)

print('기울기(가중치) : ', model.coef_)
print('편향(절편) : ', model.intercept_)

plt.figure(figsize=(10, 7))

plt.axhline(0, color='y', linestyle='--')

plt.scatter(X[:5], X[:5], c='r')
plt.scatter(X[5:], X[5:], c='b')
plt.plot(X, X * model.coef_ + model.intercept_)

plt.show()












