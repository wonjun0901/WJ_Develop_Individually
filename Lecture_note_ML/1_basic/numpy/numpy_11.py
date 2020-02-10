# -*- coding: utf-8 -*-

import numpy as np

numpy_array = np.array([[1,2],[3,4]])
print(numpy_array)

# numpy 배열의 함계 값을 반환하는 sum 메소드
result = np.sum(numpy_array)
print('numpy_array 의 전체 합계 : ', result)

# numpy 배열의 합계값은 각 행, 각 열에 대해서 
# 계산할 수 있습니다.
# axis = 0, 열
# axis = 1, 행
result = np.sum(numpy_array, axis=0)
print('numpy_array의 각 열의 합계 : ', result)

result = np.sum(numpy_array, axis=1)
print('numpy_array의 각 행의 합계 : ', result)

result = np.prod(numpy_array)
print('numpy_array 의 전체 곱의 결과 : ', result)

result = np.prod(numpy_array, axis=0)
print('numpy_array의 각 열의 곱의 결과 : ', result)

result = np.prod(numpy_array, axis=1)
print('numpy_array의 각 행의 곱의 결과 : ', result)












