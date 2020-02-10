# -*- coding: utf-8 -*-
"""
Given an array of integers, find the first missing positive integer 
in linear time and constant space. 

In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
# My Solution # 1
def find_min_pos_int(array):

    array = list(set(array))

    output = 1
    
    for num in array:
        
        if num == 0 :
        
            continue
        
        if num == output:
        
            output += 1
        
        elif num != output:
        
            return output
    
    return output

