#!/usr/bin/env python3
"""
parse_tree.py
"""
__author__ = "Kelly Zhang"
__version__ = "2026-04-15"

from atds import BinaryTree, Stack

def build_parse_tree(expr): 
    bt = BinaryTree(None)
    st = Stack()
    current = bt # current references the current BinaryTree
    st.push(current) # push current empty tree on the stack 
    for i in range(len(expr)): 
        if expr[i] == "(": 
            current.insert_left(None)
            st.push(current)
            current = current.get_left_child()
        elif expr[i] in '+-*/':
            current.set_root_val(expr[i])
            current.insert_right(None)
            st.push(current)
            current = current.get_right_child()
        elif expr[i] == ")": 
            current = st.pop()
        else: 
            current.set_root_val(int(expr[i]))
            current = st.pop()
    return bt

def evaluate(parse_tree):
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()
    root_val = parse_tree.get_root_val()
    if left_child is None and right_child is None: # base case, account for leaf nodes
        return root_val
    # recursive component
    left_val = evaluate(left_child) 
    right_val = evaluate(right_child)
    if root_val == "+":
        return left_val + right_val
    elif root_val == "-":
        return left_val - right_val
    elif root_val == "*":
        return left_val * right_val
    elif root_val == "/":
        return left_val / right_val

def main(): 
    fpe = "( 2 + ( 3 * 8 ) )"
    tokens = fpe.split(" ")
    bt = build_parse_tree(tokens)
    print(bt)
    print(evaluate(bt))

if __name__ == "__main__": 
    main()