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
    
    if not N:
        print (1)
    
    for i, num in enumerate(N):
        #while the array isn't in order starting from 1
        #and the number is positive and smaller than the number of elements in array 
        while i + 1 != N[i] and 0 < N[i] <= len(N):
            
            v = N[i]
            N[i], N[v - 1] = N[v - 1], N[i]
            
            if N[i]==N[v - 1]:
                break
            
    for i, num in enumerate(N, 1):
        if num != i:
            print (i)
    
    print (len(N)+1)

def missing_num2(N):
    s = set(N)
    print (s)
    i = 1
    
    while i in s:
        i += 1
    print (i)


    


