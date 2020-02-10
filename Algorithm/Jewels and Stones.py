# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:46:09 2019

@author: wonju
"""

class Solution:
    
    def numJewelsInStones(self, J, S):
        type_num = 0
        for J_type in J:
            if J_type in S:
                type_num = type_num + S.count(J_type)
        return type_num        



class Solution1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        dicc = {}
        for j in J:
            dicc[j] = 1
        for s in S:
            try:
                num += dicc[s]
            except:
                pass
        return num
    
    
class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        c = 0
        for i in J:
            d[i] = 0
        
        for i in S:
            if i in d:
                c += 1
        
        return c