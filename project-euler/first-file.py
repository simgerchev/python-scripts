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


