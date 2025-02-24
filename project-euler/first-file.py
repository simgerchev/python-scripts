def problem_one(): 
    result = 0 
    for x in range(1, 1000): 
        if x % 3 == 0 or x % 5 == 0: 
            result += x 
    print(result) 
    
#Fibonacci numbers basic
a = 1
b = 2
res = 0
while res < 40: 
    res = a + b
    print(f"{a} + {b} = {res}")
    a, b = b, res 


