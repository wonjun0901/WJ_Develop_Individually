# -*- coding: utf-8 -*-

import numpy as np

python_list = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

numpy_array = np.array(python_list)
print(numpy_array)

# numpy 배열에 대한 연산의 결과를 사용한 
# bool 인덱싱 처리 방법
bool_indexing_array = numpy_array % 2 == 0
print(bool_indexing_array)

# numpy bool 인덱싱 방법
# 배열 각 요소의 선택 여부를 True, False로 표현하는 방식

# boolean의 값이 True인 경우에 해당되는 
# 값 만을 반환하는 코드
# (주의사항 - 반환되는 타입은 1차원으로 반환됨)
#bool_indexing_result = numpy_array[bool_indexing_array]

# numpy 배열의 인덱스에 bool 인덱싱 처리 방법
bool_indexing_result = numpy_array[numpy_array % 2 == 0]
print(bool_indexing_result)





















