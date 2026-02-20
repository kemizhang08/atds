#!/usr/bin/env python3
"""
palindrome_checker.py
Checks if a phrase is a palindrome
"""

__author__ = "Kelly Zhang"
__version__ = "2026-02-19"

from atds import Deque

class PalindromeChecker:

    def __init__(self): 
        self.strict_mode = False

    def set_strict_mode(self, decision):
        self.strict_mode = decision

    def sanitize(self, phrase):
        cleaned = []
        for i in phrase:
            if i.isalpha():
                cleaned.append(i.lower())
        return cleaned

    def is_palindrome(self, phrase):
        has_letter = False
        for i in phrase:
            if i.isalpha():
                has_letter = True
        if has_letter == False:
            return False
        if self.strict_mode:
            check = phrase
        else:
            check = self.sanitize(phrase)
        if len(check) == 0:
            return False
        d = Deque()
        for i in check:
            d.add_rear(i)
        while d.size() > 1:
            if d.remove_front() != d.remove_rear():
                return False
        return True

def main():
    checker = PalindromeChecker()
    print("Palindrome Checker!")
    decision = int(input("Do you want strict mode 1) on, or 2) off?"))
    if decision == 1: 
        decision = True
    else: 
        decision = False
    checker.set_strict_mode(decision)
    phrase = input("Enter a phrase: ")
    if checker.is_palindrome(phrase):
        print("Is a palindrome.")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()