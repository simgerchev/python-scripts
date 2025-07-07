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
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if (i + j + k) != n]

    print(result)
    
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. 
Store them in a list and find the score of the runner-up.
'''
def ninth_task(): 
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])

'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
def tenth_task():
    python_students = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    
    grades = sorted(set([grade for name, grade in python_students]))
    second_lowest = grades[1]

    second_lowest_students = [name for name, grade in python_students if grade == second_lowest]

    for name in sorted(second_lowest_students):
        print(name)

'''
The provided code stub will read in a dictionary containing key/value pairs of name:
[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example:

Sample Input 0
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

Sample Output 0
    56.00
'''
def eleventh_task():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_marks_query = student_marks[query_name]
    student_mark_avg = sum(student_marks_query)/len(student_marks_query)
    print(f"{student_mark_avg:.2f}")