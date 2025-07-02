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

'''
The provided code stub reads an integer, n , from STDIN. 
For all non-negative integers i < n , print i ^ 2.
'''
def fifth_task():
    n = int(input())
    for i in range(0, n): 
        print(i * i)

'''
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 
'''
def sixth_task(): 
    def is_leap(year):
        leap = False
        if year % 4 == 0: 
            leap = True
            if year % 100 == 0: 
                leap = False
                if year % 400 == 0: 
                    leap = True 
        
        return leap
    year = int(input())
    print(is_leap(year))

'''
The included code stub will read an integer, n , from STDIN.

Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
'''
def seventh_task(): 
    n = int(input())
    for i in range(n):
        print(i + 1, end='')     

'''
Let's learn about list comprehensions!
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
Please use list comprehensions rather than multiple loops, as a learning exercise.
'''
def eighth_task(): 
    x, y, z, n = (int(input()) for _ in range(4))
    print([(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n])



