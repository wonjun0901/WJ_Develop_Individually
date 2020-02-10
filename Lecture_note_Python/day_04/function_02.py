# -*- coding: utf-8 -*-

# 매개변수가 사용되는 함수의 선언
# - 매개변수 : 함수의 실행에 필요한 값을 의미함
#   (기존의 변수와 동일한 개념)
# - def 함수명( 매개변수명1, 매개변수명2, ... )

# 매개변수를 1개 전달받아 실행될 수 있는
# showNumber 함수의 선언
def showNumber(number) :
    # 함수가 호출될 때 값이 전달되는 매개변수는
    # 변수와 동일한 방법으로 사용할 수 있습니다.
    # 매개변수는 함수가 실행(호출)될 때 생성되며
    # 함수의 호출 시 전달되는 값으로 초기화됩니다.
    print(f"매개변수의 값 : {number}")

# 매개변수가 정의된 함수를 호출할 때는
# 반드시 매개변수를 포함하여 호출해야 합니다.
#showNumber()
    
showNumber(11)

# 두개의 매개변수가 선언된 plus 함수의 선언
def plus(n1, n2) :
    r = n1 + n2
    print(f"{n1} + {n2} = {r}")

# 매개변수를 전달하여 함수를 실행하는 코드
# 매개변수는 전달하는 위치에 맞게 대입됩니다.
# 10은 첫번째 매개변수인 n1, 20은 두번째 매개변수인
# n2로 대입되어 실행됩니다.
plus(10, 20)
























