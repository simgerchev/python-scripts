"""
Multiples of 3 or 5
"""
def problem_one(): 
    result = 0 
    for x in range(1, 1000): 
        if x % 3 == 0 or x % 5 == 0: 
            result += x 
    print(result) 

"""
Even Fibonacci Numbers
"""
def problem_two(): 
    a = 0
    b = 1
    total = 0
    while total < 4000000:
        if a%2==0: 
            total += a
        a, b = b, b+a
    print(total)

"""
Largest Prime Factor 
Prime Numbers are numbers that can be divided only by 1 or themselves
n is a parameter for the number we want the prime numbers of
"""
def problem_three(n): 
    prime_numbers_list = []
    div = 2
    while n > 1: 
        while n % div == 0: 
            prime_numbers_list.append(div)
            n //= div
        div += 1
    print(max(prime_numbers_list))


