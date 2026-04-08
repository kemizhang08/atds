#!/usr/bin/env python3
__author__ = "Kelly Zhang"
__version__ = "04-16-2026"
from atds import Stack
import random 

def main(): 
    tasks = [ ['read work emails',10], \
          ['respond to emails', 10], \
          ['attend meeting', 15], \
          ['coffee break', 15], \
          ['talk to boss', 10], \
          ['read work emails',10], \
          ['respond to emails', 10], \
          ['conference call', 15], \
          ['conversation with colleague', 15], \
          ['coffee break', 15], \
          ['meet with student', 15] ]
    clock = 0 
    WORKDAY_MINUTES = 180 
    s = Stack()
    current_task = 0 
    while clock < WORKDAY_MINUTES: 
        print("Current time is " + clock + " and current task is " + current_task)
        print("[Enter] to continue...")
        print("Items on stack are " + s)

        if (random.randrange(10)) == 0: 
            if len(tasks) == 0: 
                s.push(tasks.pop(random.range(len(tasks))))
        if not s:
            print("Working on", current_task[0])
            current_task[1] -= 1
            if current_task[1] == 0: 
                s.pop()
            else: 
                print("Still have", current_task[1, "minutes to work on this task"])

        clock += 1

if __name__ == "__main__": 
    main()