# -*- coding: utf-8 -*-

# eval 함수
# 문자열로 저장된 실행문의 처리 결과를
# 반환하는 함수
exStr = "10 + 3"
print(f"exStr -> {exStr}")
print(f"exStr -> {eval(exStr)}")
print(f"{exStr} -> {eval(exStr)}")

numbers = [1,3,5,7,9]
exStr = "len(numbers)"
print(f"exStr -> {exStr}")
print(f"exStr -> {eval(exStr)}")

exStr = "numbers[0] + numbers[2]"
print(f"exStr -> {eval(exStr)}")


