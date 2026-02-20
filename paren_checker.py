#!/usr/bin/env python3
"""
paren_checker.py
Checks if a statement has the right number/order of parantheses
"""

__author__ = "Kelly Zhang"
__version__ = "2026-02-12"

import atds

def is_valid(expr):
    stack = atds.Stack()
    for i in expr:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

def main(): 
    pass

if __name__ == "__main__": 
    main()


