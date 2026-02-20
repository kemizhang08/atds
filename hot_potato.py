#!/usr/bin/env python3
"""
hot_potato.py
"""

__author__ = "Kelly Zhang"
__version__ = "2026-02-19"

from atds import Queue

def main():
    q = Queue()
    players = ["Bob", "Barly", "Ann", "Anna"]
    for person in players:
        q.enqueue(person)
    while q.size() > 1:
        print("Here's the queue:")
        print(q)
        for i in range(4):
            person = q.dequeue()
            print(person + " has the potato!")
            q.enqueue(person)
        eliminated = q.dequeue()
        print(eliminated + " is out!")
        input("([Enter] to see the next round!) ")
    print(q.dequeue() + " is the winner!")

if __name__ == "__main__":
    main()





    

    

