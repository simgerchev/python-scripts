import sys
import random

"""
Notes
Now I have to make a binary to decimal quiz 

"""

def binary_to_decimal(bin_number): 
    """Convert a binary to a decimal number"""

    binary_number = input("Give a binary")
    converted_number = 0
    elements = list(binary_number)
    elements.reverse()
    elements_val = []
    
    i = 0

    while i <= len(elements) - 1: 
        for element in elements: 
            if element == '1': 
                converted_number += 2 ** i
                i+=1
            elif element == '0': 
                converted_number += 0 
                i+=1
    return converted_number

def start_quiz():
    """To Do"""
    return True

def exit_app(): 
    return sys.exit()

def generate_binary_number():
    """Generate a binary number"""

    bin_number = []
    bin_number_length = input("Type the length of the binary number: ")
    bin_number_length = int(bin_number_length) - 1
    i = 0
    while i <= bin_number_length: 
        bin_digit = random.randint(0,1) 
        bin_number.append(bin_digit)
        i+=1 
        print(i)
    return print(bin_number)

def start_menu():
    """Display the start menu and handle user input."""

    input_option = input("===== \n"+
                        "What do you want to do? \n"+
                        "1. Convert binary to decimal \n"+
                        "2. Generate binary number \n"+
                        "e. Quit programm \n"+
                        "===== \n") 
    input_options = {
            '1': binary_to_decimal,
            '2': generate_binary_number,
            'e': exit_app
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")

while True: 
    start_menu()

