#!/usr/bin/env python3
__author__ = "Kelly Zhang"
__version__ = "03-16-2026"
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
    current_task = None 
    next_task = 0 
    while clock < WORKDAY_MINUTES:
        print("-------")
        print("Current time is " + str(clock) + " and current task is " + str(current_task))
        print("Items on stack are: " + str(s))
        print("[Enter] to continue...")
        if next_task < len(tasks) and random.randrange(10) == 0:
            print("New task coming in...!")
            if current_task is not None:
                # save what we are currently working on on the stack 
                s.push(current_task)
            # proceed with the incoming task 
            current_task = tasks[next_task]
            next_task += 1
        if current_task is not None:
            # work on the task for one minute 
            current_task[1] -= 1
            if current_task[1] == 0:
                current_task = None
                if not s.is_empty():
                    # if interrupted tasks then start on most recent one 
                    current_task = s.pop()
        clock += 1

if __name__ == "__main__":
    main()