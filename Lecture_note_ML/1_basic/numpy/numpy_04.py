# -*- coding: utf-8 -*-

import numpy as np

python_list = list(range(1, 11))

numpy_array_1 = np.array(python_list)
print(f'numpy_array_1.shape : {numpy_array_1.shape}')
print(f'numpy_array_1 : \n{numpy_array_1}')

# numpy_array_1 배열의 형태를 10 X 1열로 수정하여
# numpy_array_1_reshape 변수에 대입하세요
numpy_array_1_reshape = numpy_array_1.reshape(-1, 1)
print(f'numpy_array_1_reshape.shape : {numpy_array_1_reshape.shape}')
print(f'numpy_array_1_reshape : \n{numpy_array_1_reshape}')

# 배열의 전치 연산을 수행할 수 있는 np.transpose 함수
# - 2차원 배열의 경우 행과 열이 변환
# - 전치행열의 경우 차원의 수는 유지됨
# 10 X 1 형태의 배열 -> (1, 10)
numpy_array_2 = np.transpose(numpy_array_1_reshape)
print(f'numpy_array_2.shape : {numpy_array_2.shape}')
print(f'numpy_array_2 : \n{numpy_array_2}')























