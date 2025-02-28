import random

show_menu = True

def start_menu(): 
    print("=====")
    input_option = input("Which operation do you want to practice? \n"+
                         "1. Addition \n") 
    input_options = {
            '1': start_addition_tasks,
            'e': quit_program
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")

def start_addition_tasks(): 
    task_count = int(input("How many tasks do you wanna get? ")) 
    while task_count>=1: 
        get_addition_task()
        task_count-=1
    return start_menu()
    
def get_addition_task():
    input_min_a = int(input("Smallest number a: "))
    input_max_a = int(input("Biggest number a: "))
    input_min_b = int(input("Smallest number b: "))
    input_max_b = int(input("Biggest number b: "))
    a = random.randint(input_min_a, input_max_a)
    b = random.randint(input_min_b, input_max_b)

    answer = input(f"How much is {a} + {b}: ")
    if int(answer) == a + b: 
        print("Answer is true") 
    else: 
        print("Answer is wrongX") 

def quit_program(): 
    global show_menu
    show_menu = False
    return show_menu

while show_menu: 
    start_menu()


    
