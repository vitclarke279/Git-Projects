# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:53:41 2020

@author: vlopa
"""
import ctypes

class Node(object):
    def __init__(self, data):
        self.data = data
        self.both = 0
        
class XorLinkedLists(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] #to prevent garbage collection
        
    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node
        #Without thil line, Python thinks there is no way to reach nodes
        #between head and tail.
        self.__nodes.append(node)
        
    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range (index):
            next_id = prev_id ^ node.both
            
            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node
def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).Value

