# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:50:03 2020

@author: vlopa

Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest 
positive integer that does not exist in the array. The array can 
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

def missing_num(N):
    
    N.sort()
    
    print(N)
    
    for i in range(len(N)):
        if N[i] == (-1) and N[i+1] != 0 and N[i+1] != 1:
            print (1)
        elif N[i] >= 0 and N[i+1] != (N[i]+1):
            print (N[i]+1)
        elif N[len(N)]:
            print (N[i]+1)
            
    
            
    
list1 = [1,2,0]

missing_num(list1)
