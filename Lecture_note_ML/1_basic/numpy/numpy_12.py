# -*- coding: utf-8 -*-

import numpy as np

numpy_array_1 = np.array([1,2,3])
numpy_array_2 = np.array([4,5,6])
numpy_array_3 = np.array([7,8,9])
#numpy_array_1 = np.array([[1],[2],[3]])
#numpy_array_2 = np.array([[4],[5],[6]])

# numpy 배열을 결합
# - 앞의 배열의 내용에 뒤의 배열을 결합
# - 1차원 배열인 경우 왼쪽에서 오른쪽으로 결합
# - 2차원 배열인 경우 앞의 배열의 결합되어 
#   하나의 2차원 배열이 반환됨
r = np.r_[numpy_array_1, numpy_array_2, numpy_array_3]
print(r)

r = np.hstack([numpy_array_1, numpy_array_2, numpy_array_3])
print(r)

# 2개의 1차원 numpy 배열을 
# 세로로 결합하여 2차원 배열 생성
# (각 열의 결합하여 2차원 배열을 생성)
c = np.c_[numpy_array_1, numpy_array_2, numpy_array_3]
print(c)

c = np.column_stack([numpy_array_1, numpy_array_2, numpy_array_3])
print(c)


















