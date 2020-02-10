# -*- coding: utf-8 -*-

import numpy as np

# 파이썬 리스트 생성
# - range 함수를 응용하여 간편하게 생성할 수 있음
# - 1 ~ 10 까지의 정수를 갖는 리스트 생성
python_list = list(range(1, 11))

# numpy 배열 생성
numpy_array_1 = np.array(python_list)
print(f'numpy_array_1.shape : {numpy_array_1.shape}')
print(f'numpy_array_1 : \n{numpy_array_1}')

# 배열의 형태를 수정할 수 있는 reshape() 메소드
# numpy배열변수.reshape(변경할 배열의 shape)
numpy_array_2 = numpy_array_1.reshape(2, 5)
print(f'numpy_array_2.shape : {numpy_array_2.shape}')
print(f'numpy_array_2 : \n{numpy_array_2}')

# reshape() 메소드 사용시 주의사항
# - 원본 배열의 요소의 수는
#  변경할 형태의 shape의 요소 개수를 
#  만족해야합니다.
numpy_array_3 = numpy_array_1.reshape(3, 5)
print(f'numpy_array_3.shape : {numpy_array_3.shape}')
print(f'numpy_array_3 : \n{numpy_array_3}')

# -1 매개변수가 사용되는 경우 나머지 매개변수 값에의해서
# 자동으로 계산된 값이 적용됩니다.
# (아래의 예의 경우 행의 수를 2로 고정하여 열의 수는
#  5로 처리됩니다.)
numpy_array_4 = numpy_array_1.reshape(2, -1)
print(f'numpy_array_4.shape : {numpy_array_4.shape}')
print(f'numpy_array_4 : \n{numpy_array_4}')

# (아래의 예의 경우 열의 수를 2로 고정하여 행의 수는
#  5로 처리됩니다.)
numpy_array_5 = numpy_array_1.reshape(-1, 2)
print(f'numpy_array_5.shape : {numpy_array_5.shape}')
print(f'numpy_array_5 : \n{numpy_array_5}')

# 다차원 배열의 형태를 1차원 배열로 변경
numpy_array_6 = numpy_array_5.reshape(10)
print(f'numpy_array_6.shape : {numpy_array_6.shape}')
print(f'numpy_array_6 : \n{numpy_array_6}')

numpy_array_7 = numpy_array_5.reshape(-1)
print(f'numpy_array_7.shape : {numpy_array_7.shape}')
print(f'numpy_array_7 : \n{numpy_array_7}')

















