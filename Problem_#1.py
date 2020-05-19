# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:03:41 2020

@author: vlopa

Given a list of nembers and number k, return whether two numbers from the list add up to k.
"""



def two_sum1 (N,k):
    "Function taking inputs of array N and a number k. Returns whether two"
    "numbers from the array add up to to K "
    
    for i in range (len(N)):
        for j in range (len(N)):
            if i != j and N[i] + N[j] == k:
                return True
            else:
                return False
        
        
    
def two_sum2 (N,k):
    
    seen = set()    #empty set
    for num in N:
        if k - num in seen:
            return True
        seen.add(num)
    return False
    

