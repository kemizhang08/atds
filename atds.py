#!/usr/bin/env python3
"""
atds.py
A collection of data types for the Advanced Topics class 
"""
__author__ = "Kelly Zhang"
__version__ = "2026-02-12"

class Stack(): 
    def __init__(self): 
        self.stack = []

    def push(self, item): 
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self): 
        if len(self.stack) > 0: 
            return self.stack[-1]

    def size(self): 
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0 

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
   
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
       
    def size(self):
        return len(self.queue)
   
    def is_empty(self):
        return self.size() == 0
   
    def __str__(self):
        return str(self.queue)

class Deque(): 
    def __init__(self): 
        self.deque = []
    
    def add_front(self, item): 
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)
    
    def remove_front(self): 
        if len(self.deque) > 0: 
            return self.deque.pop(0)
    
    def remove_rear(self): 
        if len(self.deque) > 0: 
            return self.deque.pop()
    
    def size(self): 
        return len(self.deque)
    
    def is_empty(self): 
        return self.size() == 0
    
    def peek_front(self): 
        if len(self.deque) > 0: 
            return self.deque[0]
    
    def peek_rear(self): 
        if len(self.deque) > 0: 
            return self.deque[-1]
    

def main(): 
    pass

if __name__ == "__main__": 
    main()

    


