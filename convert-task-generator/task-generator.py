"""
Notes
Now I have to make a binary to decimal quiz 

"""

def binary_to_decimal(): 
    """Convert a binary to a decimal number"""

    binary_to_decimal(input("Give a binary"))
    res = 0
    elements = list(binary_number)
    elements.reverse()
    elements_val = []
    
    i = 0

    while i <= len(elements) - 1: 
        for element in elements: 
            if element == '1': 
                res += 2 ** i
                i+=1
            elif element == '0': 
                res += 0 
                i+=1
    return print(res) 



def start_menu(): 
    """Start menu function""" 
    input_start_menu() = input("What do you want to do: 1. Convert binary to decimal 2. Exit")
    if input_start_menu() == "1": 
        binary_to_decimal()
while True: 
    start_menu()
