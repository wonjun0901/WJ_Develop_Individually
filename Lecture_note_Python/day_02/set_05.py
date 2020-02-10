﻿# -*- coding: utf-8 -*-

# 2의 배수를 저장하고 있는 set_2 변수
set_2 = set([2,4,6,8])
# 3의 배수를 저장하고 있는 set_3 변수
set_3 = set([3,6,9])

# set_2와 set_3의 교집합을 출력하는 예제
# (두 Set 변수에서 동일하게 저장하고 있는 값)
# & 연산자를 사용하여 처리할 수 있음
print(set_2 & set_3)

# set_2와 set_3의 합집합을 출력하는 예제
# | 연산자를 사용하여 처리할 수 있음
# (두 Set 변수의 데이터를 합치는 기능)
# (중복 데이터는 하나만 출력)
print(set_2 | set_3)

# set_2와 set_3의 차집합을 출력하는 예제
# - 연산자를 사용하여 처리할 수 있음
# 좌측에 위치한 Set에서 
# 우측에 위치한 Set의 데이터를 제거한 결과가 반환됨
# 위치에 따라 서로 다른 결과가 반환
print(set_2 - set_3)
print(set_3 - set_2)

# 파이썬에서 제공하는 컬렉션 타입
# 컬렉션 - 다수개의 저장할 수 있는 타입을 통칭하는 단어
#          (데이터 저장 개수의 제한이 없는 타입)
# 1. List
#  - 값의 저장 순서를 유지
#  - 값의 중복을 허용
#  - 인덱스를 활용하여 각 데이터에 접근
# 2. Dictionary
#  - Key, Value 형태로 데이터를 저장
#  - 값의 저장 순서를 유지하지 않음
#  - Key 값의 중복을 허용하지 않음(Value 중복은 허용)
#  - 동일한 Key 값으로 입력되는 경우
#    해당 Key 값으로 연결된 Value를 수정
#  - keys(), values(), items() 메소드를 활용하여
#    Dictionary 내부를 순회할 수 있음
# 3. Set
#  - 값의 저장 순서를 유지하지 않음
#  - 값의 중복을 허용하지 않음
#  - List 타입으로 변환한 후, 인덱스를 활용하여 
#    각 데이터에 접근
#  - 교집합(&), 합집합(|), 차집합(-)을 연산할 수 있음







