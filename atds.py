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
        return self.stack.pop(0)

    def push(self, item): 
        self.stack.add(item)

    def peek(self): 
        if self.stack.head == None:
            return None
        return self.stack.head.get_data()

    def size(self): 
        return self.stack.length()
    
    def is_empty(self): 
        return self.stack.length() == 0

class HashTable: 
    def __init__(self, size): 
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size
    
    def __repr__(self): 
        result = []
        result.append("Slots: " + str(self.slots))
        result.append("Data: " + str(self.data))
        return "\n".join(result)

    def hash_function(self, key): 
        return key % self.size
    
    def put(self, key, value): 
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None: 
            self.slots[hash_value] = key
            self.data[hash_value] = value 
        elif self.slots[hash_value] == key: 
            self.data[hash_value] = value
        else: 
            next_slot = (hash_value + 1) % self.size
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = (next_slot + 1) % self.size  
            if self.slots[next_slot] is None: 
                self.slots[next_slot] = key
                self.data[next_slot] = value 
            else: 
                self.data[next_slot] = value
    
    def get(self, key): 
        starting_pos = self.hash_function(key)
        pos = starting_pos
        while self.slots[pos] is not None: 
            if self.slots[pos] == key: 
                return self.data[pos]
            pos = (pos + 1) % self.size
            if pos == starting_pos: 
                break
        return None

    
def main(): 
    hash = HashTable(5)
    print(hash)
    print()

    hash.put(6, "Sam")
    print(hash)
    print()

    hash.put(12, "Potato")
    print(hash)
    print()

    hash.put(7, "Seaweed")
    print(hash)
    print()

    hash.put(15, "Bean")
    print(hash)
    print()

    hash.put(3, "Taco")
    print(hash)
    print()

    print(hash.get(3))
    print(hash.get(1))

if __name__ == "__main__": 
    main()

    


