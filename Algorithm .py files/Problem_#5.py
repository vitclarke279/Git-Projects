# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:45:34 2020

@author: vlopa
"""

def cons(a, b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    return pair(lambda a,b: a)

def cds(pair):
    return pair(lambda a,b: b)


    

print (car(cons(3,4)))

