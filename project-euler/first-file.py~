def problem_one(): 
    result = 0 
    for x in range(1, 1000): 
        if x % 3 == 0 or x % 5 == 0: 
            result += x 
    print(result) 

def problem_two(): 
    a = 0
    b = 1
    total = 0
    while total < 4000000:
        if a%2==0: 
            total += a
        a, b = b, b+a
    print(total)

def find_division_numbers(init_number):
    i = 2 
    numbers = []
    division_numbers = []
    while i < init_number - 1: 
        numbers.append(i)
        i+=1 
    for num in numbers: 
        if init_number % num == 0: 
            division_numbers.append(num)
    return division_numbers

def find_prime_number(input_number):
    prime_numbers_list = []
    prime_number = input_number
    while prime_number:
        numbers_list = find_division_numbers(prime_number)
        prime_number = numbers_list[0]
        prime_numbers_list.append(prime_number)
        find_division_numbers(prime_number)
    return print(prime_numbers_list)

find_prime_number(100)  

