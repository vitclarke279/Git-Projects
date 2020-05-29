# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:43:39 2020

@author: vlopa

Given an array of integers, return a new array such that each element at index
	i of the new array is the product of all the numbers in the original array 
	except the one at i.

	For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
	[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
	[2, 3, 6].

	Follow-up: what if you can't use division?
"""
import numpy as np

def List_Product(N): #input list N 
    Product_list = np.zeros(len(N)) #Making list to input the products in.
    for i in range(len(N)): #using len(N) gives the number of element in list N
        v = 1 #so first multiplication isn't 0
        for k in range(len(N)):
            if k != i:
                v = v * N[k]
        Product_list[i] = v
    print (Product_list)

def List_Product2(N):
    P = 1
    for n in N:
        P = P * n
    s = np.zeros(len(N))
    for i in range (len(N)):
        s[i] = P * (N[i])**-1
    print (s)

def List_Product3(N):
    s = np.zeros(len(N))
    for i in range(len(N)):
        del N[i]
        s[i] = np.prod(N) #takes product of all elements in array
    print (s)


#Given solution
def products(nums):
    
    prefix_products = []
    
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    print(prefix_products)
    
    suffix_products = []
    
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
            
    print(suffix_products)
    
    suffix_products = list(reversed(suffix_products))
    
    print(suffix_products)
    
    result = []
    for i in range(len(nums)):
        if i==0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    print (result)
    
    
    

            




