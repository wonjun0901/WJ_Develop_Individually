# -*- coding: utf-8 -*-

import numpy as np

python_list = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

numpy_array = np.array(python_list)
print(numpy_array)

# boolean 값을 사용하여 numpy 배열을 생성
bool_indexing_array = np.array([
            [False, True, False],
            [True, False, True],
            [False, True, False]
        ])

# numpy bool 인덱싱 방법
# 배열 각 요소의 선택 여부를 True, False로 표현하는 방식

# boolean의 값이 True인 경우에 해당되는 
# 값 만을 반환하는 코드
# (주의사항 - 반환되는 타입은 1차원으로 반환됨)
bool_indexing_result = numpy_array[bool_indexing_array]
print(bool_indexing_result)








