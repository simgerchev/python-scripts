import random
import operator

show_menu = True
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}


def start_menu(): 
    input_option = input("===== \n"+
                        "Which operation do you want to practice? \n"+
                        "1. Start tasks \n"+
                        "e. Quit programm \n"+
                        "===== \n") 
    input_options = {
            '1': start_tasks,
            'e': quit_program
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")

def get_input(): 
    task_count = int(input("How many tasks do you wanna get? "))
    input_task_type = input("What kind of tasks do you want? + | - | * | / ") 
    input_min_a = int(input("Smallest number a: "))
    input_max_a = int(input("Biggest number a: "))
    input_min_b = int(input("Smallest number b: "))
    input_max_b = int(input("Biggest number b: "))

    return task_count, input_task_type, input_min_a, input_max_a, input_min_b, input_max_b

def start_tasks():
    task_count, input_task_type, input_min_a, input_max_a, input_min_b, input_max_b = get_input() 
    while task_count>=1:
        get_task(input_task_type, input_min_a, input_max_a, input_min_b, input_max_b)
        task_count-=1
    return start_menu()
    
def get_task(input_task_type, input_min_a, input_max_a, input_min_b, input_max_b):
    a = random.randint(input_min_a, input_max_a)
    b = random.randint(input_min_b, input_max_b)
    if ops[input_task_type]: 
        operator_function = ops[input_task_type]
        input_answer = input(f"How much is {a} {input_task_type} {b}: ")
        if int(input_answer) == operator_function(a, b): 
            print("Answer is true") 
        else: 
            print("Answer is wrongX")
    else: 
        print("Invalid operator")
        start_menu()

def quit_program(): 
    global show_menu
    show_menu = False
    return show_menu

while show_menu: 
    start_menu()


    
