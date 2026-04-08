#!/usr/bin/env python3
"""
stack_comparison.py
The purpose of this project is to compare the time efficiency of a list-based Stack and an unordered 
list based stack. To do this, I first created separate methods to get the run times of the pushes and pops
for the two different stacks. To do so, I used the Python built in time function. For testing pop times,
I first had to use the push function to build the stack that would then be popped. In the main function I 
called the functions for the four tests and printed the times in intervals of 10000 from 10000 to 100000. 
Then, I used numpy and matplotlib to create graphs for the push and pop comparisons. For each of the graphs, 
I plotted the results of the list-based stack in red and the UL stack in blue. I also created trendlines
for each by using numpy's polyfit and polyval functions. The results showed that the list-based stack
was more time efficient than the UL stack for both pushes and pops. For the push runtime, the list-based
Stack had a trendline of 4.097e-08x and the UL Stack had a trendline of 3.404e^-07. Dividing the UL Stack
trendline value by the list-based Stack value shows that the list-based stack was around 8.3 times faster
than the UL Stack. As for the pop runtime, the list-based Stack had a trendline of 4.69e-08x and the UL
Stack had a trendline of 1.746e-07. Dividing again shows that the list-based stack was around 3.7 times
faster than the UL Stack for pops.  
"""
__author__ = "Kelly Zhang"
__version__ = "2026-03-10"

from atds import *
import time
import matplotlib.pyplot as plt 
import numpy as np

def testStackPush(s: Stack, n: int) -> float:
    """Returns the time to run the push operation on a Stack"""
    start = time.time()
    for i in range(n): 
        s.push(i)
    stop = time.time()
    return stop - start

def testStackPop(s: Stack, n: int) -> float: 
    """Returns the time to run the pop operation on a Stack"""
    for i in range(n): 
        s.push(i)
    start = time.time()
    for i in range(n): 
        s.pop()
    stop = time.time()
    return stop - start

def testULSPush(uls: ULStack, n: int) -> float: 
    """Returns the time to run the push operation on an Unordered List Stack"""
    start = time.time()
    for i in range(n): 
        uls.push(i)
    stop = time.time()
    return stop - start

def testULSPop(uls: ULStack, n: int) -> float: 
    """Returns the time to run the pop operation on an Unordered List Stack"""
    for i in range(n): 
        uls.push(i)
    start = time.time()
    for i in range(n): 
        uls.pop()
    stop = time.time()
    return stop - start

def main(): 
    START = 10000
    END = 110000
    STEP = (END - START) // 10
    x = []
    stack_push_times = []
    uls_push_times = []
    stack_pop_times = []
    uls_pop_times = []

    """Print runtime values for pushes and pops of list-based stacks and UL stack"""
    for test_size in range(START, END, STEP): 
        x.append(test_size)
        s_push = Stack()
        stack_push_times.append(testStackPush(s_push, test_size))
        uls_push = ULStack()
        uls_push_times.append(testULSPush(uls_push, test_size))
        s_pop = Stack()
        stack_pop_times.append(testStackPop(s_pop, test_size))
        uls_pop = ULStack()
        uls_pop_times.append(testULSPop(uls_pop, test_size))
    print('x values:', x)
    print('Stack push times:', stack_push_times)
    print('ULStack push times:', uls_push_times)
    print('Stack pop times:', stack_pop_times)
    print('ULStack pop times:', uls_pop_times)
    sizes = np.array(x)

    """Push comparison graph"""
    stack_push_array = np.array(stack_push_times)
    uls_push_array = np.array(uls_push_times)
    stack_push_coefficients = np.polyfit(sizes, stack_push_array, 1)
    uls_push_coefficients = np.polyfit(sizes, uls_push_array, 1)
    stack_push_fit = np.polyval(stack_push_coefficients, sizes)
    uls_push_fit = np.polyval(uls_push_coefficients, sizes)
    plt.plot(x, stack_push_times, 'ro', label='Stack pushes')
    plt.plot(x, uls_push_times, 'bo', label='ULStack pushes')
    stack_push_label = 'Stack fit: y = {0:.8e}x + {1:.8f}'.format(*stack_push_coefficients)
    uls_push_label = 'ULStack fit: y = {0:.8e}x + {1:.8f}'.format(*uls_push_coefficients)
    plt.plot(sizes, stack_push_fit, 'r-', label=stack_push_label)
    plt.plot(sizes, uls_push_fit, 'b-', label=uls_push_label)
    plt.title('Push Runtime Comparison')
    plt.xlabel('Number of pushes')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.show()

    """Pop comparison graph"""
    stack_pop_array = np.array(stack_pop_times)
    uls_pop_array = np.array(uls_pop_times)
    stack_pop_coefficients = np.polyfit(sizes, stack_pop_array, 1)
    uls_pop_coefficients = np.polyfit(sizes, uls_pop_array, 1)
    stack_pop_fit = np.polyval(stack_pop_coefficients, sizes)
    uls_pop_fit = np.polyval(uls_pop_coefficients, sizes)
    plt.plot(x, stack_pop_times, 'ro', label='Stack pops')
    plt.plot(x, uls_pop_times, 'bo', label='ULStack pops')
    stack_pop_label = 'Stack fit: y = {0:.8e}x + {1:.8f}'.format(*stack_pop_coefficients)
    uls_pop_label = 'ULStack fit: y = {0:.8e}x + {1:.8f}'.format(*uls_pop_coefficients)
    plt.plot(sizes, stack_pop_fit, 'r-', label=stack_pop_label)
    plt.plot(sizes, uls_pop_fit, 'b-', label=uls_pop_label)
    plt.title('Pop Runtime Comparison')
    plt.xlabel('Number of pops')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.show()

if __name__ == "__main__": 
    main()




