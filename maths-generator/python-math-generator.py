import random
import operator

score = 0
show_menu = True

#Define operations
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}


def start_menu():
    """Display the start menu and handle user input."""
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

def manage_score(is_correct):
    """Adds 1 point to the score if user has a right question""" 
    global score
    if is_correct: 
        score += 1 
        return score

def get_input(): 
    """Gets task count input and task type input"""
    input_task_count = get_task_count()
    input_task_type = get_task_type()

    return input_task_count, input_task_type

def get_task_count():
    """Ask the user how many tasks they want to solve."""
    while True:
        try: 
            input_task_count = input("How many tasks do you wanna get? ")
            if input_task_count.isdigit():
                input_task_count = int(input_task_count)
                if input_task_count > 0: 
                    return input_task_count
                else: 
                    print("Invalid input: Input is equal or less than zero.")
        except ValueError: 
            print("Invalid input: Please enter a valid digital number. ")

def get_input_min_max(value): 
    """Ask the user for min and max values of operands."""
    while True:
        try: 
            input_min = input(f"Enter your value for {value} min")
            input_max = input(f"Enter your value for {value} max")
            if input_min.isdigit() and input_max.isdigit(): 
                input_min = int(input_min)
                input_max = int(input_max)
                if input_min<input_max: 
                    return input_min, input_max
                else: 
                    print("Min is bigger than max")
        except ValueError: 
            print("Invalid number")

def get_task_type():
    """Ask the user for the operation type they want to practice."""
    while True:
        try: 
            input_task_type = input("What kind of tasks do you want? + | - | * | / ").strip()
            if ops[input_task_type]: 
                return input_task_type
        except KeyError: 
            print("Enter a valid operator") 

def start_tasks():
    """It starts to give the tasks"""
    global score
    score = 0
    input_task_count, input_task_type = get_input() 
    question_count = input_task_count
    min_a, max_a = get_input_min_max("a")
    min_b, max_b = get_input_min_max("b")
    while input_task_count>=1:
        get_task(input_task_type, min_a, max_a, min_b, max_b)
        input_task_count-=1
    print(f"{score} right questions out of {question_count}")
    return start_menu()
    
def get_task(input_task_type, min_a, max_a, min_b, max_b):
    """Gets a task"""
    is_correct = False
    a = random.randint(min_a, max_a)
    b = random.randint(min_b, max_b)
    if ops[input_task_type]: 
        operator_function = ops[input_task_type]
        input_answer = input(f"How much is {a} {input_task_type} {b}: ")
        if int(input_answer) == operator_function(a, b): 
            print("Answer is true") 
            is_correct = True
            manage_score(is_correct)
        else: 
            print("Answer is wrongX")
            is_correct = False
    else: 
        print("Invalid operator")
        start_menu()

def quit_program(): 
    """Quits the program"""
    global show_menu
    show_menu = False
    return show_menu

while show_menu: 
    """Infinite loop to show the start menu""" 
    start_menu()


    
