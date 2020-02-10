# -*- coding: utf-8 -*-
"""

Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 
when the reversed integer overflows.


Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of x and "push" it to the back of the 'rev'. 
In the end, 'rev' will be the reverse of the x.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.
"""



class Solution:
    def reverse_num(self, x):
        
        # 반환할 값 0으로 초기화
        result = 0
        
        # 정수의 절대값화 to 간단히 만들기 위해
        y = abs(x)
        
        
        while y > 0:
        # 10으로 나눠서 나머지를 구함.    
            remainder = y % 10
            result = result + remainder
            y = int(y / 10)
        
        if result > 2**31-1:
            return 0
        
        if x > 0:
            return result
        else:
            return -result