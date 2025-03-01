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


def find_prime_numbers(input_number): 
            
    def find_division_numbers(init_number):
        i = 2 
        division_numbers = []
        while i < init_number - 1: 
            division_numbers.append(i)
            i+=1 
        for num in division_numbers: 
            if init_number % num == 0: 
                print(f"prime number is: {num}")




