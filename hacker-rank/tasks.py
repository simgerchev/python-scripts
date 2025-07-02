import math
import os
import random
import re
import sys

'''
Input Format
    You do not need to read any input in this challenge.
Output Format
    Print Hello, World! to stdout.
'''
def first_task(): 
    print("Hello, World!")

'''
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''
def second_task(): 
    n = int(input().strip())
    if n % 2 > 0: 
        print("Weird")
    elif n % 2 == 0:     
        if n >= 2 and n <= 5: 
            print("Not Weird")
        elif n >= 6 and n <= 20: 
            print("Weird")
        elif n > 20: 
            print("Not Weird")

'''
Task
The provided code stub reads two integers from STDIN, a and b . Add code to print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.
'''
def third_task(): 
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

'''
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. 
    The first line should contain the result of integer division,  // . 
    The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
'''
def fourth_task(): 
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)



