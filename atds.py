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
                    current = self.head           
                else:
                    previous.set_next(current.get_next())
                    current = previous.get_next()
            else:
                previous = current
                current = current.get_next()
    
    def search(self, item): 
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def append(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)
    
    def index(self, item): 
        count = 0
        current = self.head
        while current != None:
            if current.get_data() == item:
                return count
            current = current.get_next()
            count += 1
        return 

    def insert(self, pos, item): 
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return
        else: 
            count = 0
            current = self.head
            while count < pos - 1: 
                current = current.get_next()
                count += 1
                new_node.set_next(current.get_next())
                current.set_next(new_node)

    def pop(self, pos = None):
        if self.head == None:
            return None
        if pos == None:
            previous = None
            current = self.head
            if current.get_next() == None:
                data = current.get_data()
                self.head = None
                return data
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            data = current.get_data()
            previous.set_next(None)
            return data
        if pos == 0:
            data = self.head.get_data()
            self.head = self.head.get_next()
            return data
        index = 0
        previous = None
        current = self.head
        while index < pos and current != None:
            previous = current
            current = current.get_next()
            index += 1
        if current == None:
            return None
        data = current.get_data()
        previous.set_next(current.get_next())
        return data
    
    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging"""
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
    
class ULStack(object): 
    def __init__(self): 
        self.stack = UnorderedList()
    def pop(self): 
        return self.stack.pop()
    def push(self, item): 
        self.stack.append(item)
    def peek(self): 
        current = self.stack.pop()
        current = self.stack.append(current)
        return current
    def size(self): 
        return self.stack.length()
    def is_empty(self): 
        return self.stack.length() == 0
    
    
def main(): 
    pass

if __name__ == "__main__": 
    main()

    


