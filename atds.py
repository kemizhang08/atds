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

class Node(): 
    def __init__(self, data): 
        self.data = data
        self.next = None

    def get_data(self): 
        return self.data
    
    def set_data(self, new_data): 
        self.data = new_data
    
    def get_next(self): 
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next 
    
    def __repr__(self): 
        return "Node[data=" + str(self.data) + ", next=" + str(self.next) + "]"

class UnorderedList(): 
    def __init__(self): 
        self.head = None
    
    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def length(self): 
        node_count = 0
        current = self.head
        while current != None: 
            node_count += 1
            current = current.get_next()
        return node_count
    
    def is_empty(self): 
        return self.head == None
    
    def remove(self, item): 
        previous = None
        current = self.head 
        while current != None: 
            if current.get_data() == item: 
                if previous == None:
                    self.head = current.get_next()
                else: 
                    previous.set_next(current.get_next())
                return
            else: 
                previous = current
                current = current.get_next()
        return 
    
    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging"""
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
     
def main(): 
    pass

if __name__ == "__main__": 
    main()

    


