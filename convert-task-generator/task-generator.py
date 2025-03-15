import sys
import random

"""
Notes
Now I have to make a binary to decimal quiz 

"""

def binary_to_decimal(): 
    """Convert a binary to a decimal number"""

    binary_number = input("Give a binary")
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

def exit_app(): 
    return sys.exit()

def generate_task():
    bin_number = []
    i = 0
    while i <= 4: 
        bin_digit = random.randint(0,1) 
        bin_number.append(bin_digit)

def start_menu():
    """Display the start menu and handle user input."""
    input_option = input("===== \n"+
                        "What do you want to do? \n"+
                        "1. Convert binary to decimal \n"+
                        "e. Quit programm \n"+
                        "===== \n") 
    input_options = {
            '1': binaryto_to_decimal(),
            'e': exit_app()
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")

while True: 
    start_menu()
