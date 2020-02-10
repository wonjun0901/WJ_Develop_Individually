# -*- coding: utf-8 -*-

# 파이썬의 리스트는 + 연산의 경우 결합연산이 실행됨
python_array_1 = [1,2,3]
python_array_2 = [4,5,6]

python_array_sum = python_array_1 + python_array_2
print(python_array_sum)

import numpy as np

# 연속되는 값을 가지는 numpy 배열을 생성하는 코드
# - 파이썬의 기본 함수인 range와 유사한 arange 함수
numpy_array_1 = np.arange(1, 4)
numpy_array_2 = np.arange(4, 7)

# numpy 배열의 경우 +, -, *, / 와 같은 연산을 수행하면
# 앞과 뒤의 배열에 대해서 각 위치에 해당되는 요소끼리
# 연산이 수행된 결과가 반환

# numpy 배열의 각 요소의 합계
numpy_array_r = numpy_array_1 + numpy_array_2
numpy_array_r = np.add(numpy_array_1, numpy_array_2)
print(numpy_array_r)

# numpy 배열의 각 요소의 차
numpy_array_r = numpy_array_1 - numpy_array_2
numpy_array_r = np.subtract(numpy_array_1, numpy_array_2)
print(numpy_array_r)

# numpy 배열의 각 요소의 곱
numpy_array_r = numpy_array_1 * numpy_array_2
numpy_array_r = np.multiply(numpy_array_1, numpy_array_2)
print(numpy_array_r)

# numpy 배열의 각 요소의 나눗셈
numpy_array_r = numpy_array_1 / numpy_array_2
numpy_array_r = np.divide(numpy_array_1, numpy_array_2)
print(numpy_array_r)










