#!/usr/bin/env python3
"""
binary_traversal_demo
"""
__author__ = "Kelly Zhang"
__version__ = "2026-04-17"

from atds import BinaryTree

def preorder(tree): 
    if tree is None: 
        return []
    return([tree.get_root_val()] + preorder(tree.get_left_child()) + preorder(tree.get_right_child()))

def inorder(tree): 
    if tree is None: 
        return []
    return(inorder(tree.get_left_child()) + [tree.get_root_val()] + inorder(tree.get_right_child()))

def postorder(tree): 
    if tree is None: 
        return []
    return(postorder(tree.get_left_child()) + postorder(tree.get_right_child()) + [(tree.get_root_val())])

def main(): 
    bt = BinaryTree(1)
    bt.insert_left(3)
    bt.insert_right(5)
    bt.get_left_child().insert_left(7)
    bt.get_right_child().insert_right(9)
    print("Preorder", preorder(bt))
    print("Inorder", inorder(bt))
    print("Postorder", postorder(bt))

if __name__ == "__main__": 
    main()


