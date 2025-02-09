import json
import sys

# json constants 
json_file_const = 'flashcards.json'
short_answer_type_const = 'short-answer'
multiple_choice_type_const = 'multiple-choice'
note_type_const = 'note'
question_type_const = 'question-type'
correct_answer_const = 'correct-answer'



'''
--------- START MENU FUNCTIONS --------- 
'''

'''
Saves a flashcard

:param content:array content of the flashcard
:return: returns nothing
'''
def save_content(content):
    with open(json_file_const, "w") as file:
        json.dump(content, file, indent=4)

'''
Counts and manages points

:param answer:bool answer of the question
:return: returns nothing
'''
def manage_points(answer):
    points = 0
    if answer == True:
        points += 1 
        return points
    else:
        points -= 1
        return points
    if points < 0:
        print('Game Over')
        return points


'''
Adds a flashcard

:return: returns nothing
'''
def add_flashcard(): 
    content = post_topics()
    input_topic = input('Type the name of the topic: ').strip().lower()
    if input_topic not in content:
        print('Topic doesnt exist')
        return start_menu()
        
    post_all_flashcards(input_topic)
    flashcard_type = input('What flashlight do you want to add? multiple-choice / short-answer / note: ').strip().lower() 

    def get_multiple_choice_input():
        options = {}
        for input_option in ["A", "B", "C"]:
            options[input_option] = input(f'Enter the option for {input_option} here: ')
        return {"flashcard": input('Enter your flashcard here: '), "option": options, "correct-answer": input('Enter the correct answer here: '), "flashcard-type": flashcard_type}
    
    def get_short_answer_input():
        return {"flashcard": input('Enter your flashcard here: '), "correct-answer": input('Enter the correct answer here: '), "flashcard-type": flashcard_type}

    def get_note_input():
        note_input = True
        notes = []
        while note_input:
            note_input = input('Enter note')
            notes.append(note_input)
            note_input = input('Enter yes/y if you want to add another note: ')
            if note_input == 'yes' or note_input == 'y': 
                note_input = True
            else: 
                note_input = False
        return {"flashcard": input('Enter your flashcard here: '), "notes": notes, "flashcard-type": flashcard_type}

    flashcard_types = {
        multiple_choice_type_const: get_multiple_choice_input,
        short_answer_type_const: get_short_answer_input,
        note_type_const: get_note_input
    }
    
    if flashcard_type in flashcard_types: 
        content[input_topic].append(flashcard_types[flashcard_type]())
        save_content(content)
        print('Flashcard added successfully!')
        return start_menu()
    else: 
        print('Flashcard type doesnt exist')
'''
Adds a topic

:return: returns nothing
'''
def add_topic():
    content = post_topics()
    topic_input = input('Enter a topic: ')
    if topic_input in content: 
        print('Topic already exists')
    else:
        content[topic_input] = []
        save_content(content)
        print('Topic added successfully')
    
'''
Function that shows the start menu

:return: returns nothing
'''
def start_menu():
    print("----------------------------------------------------------------------------------------------------")
    input_option = input("Do you want to: 🐝\n"+ 
        "1. Show all topics\n"+
        "2. Add another flashcard \n"+
        "3. Start quiz \n"+
        "4. Add another topic \n"+
        "5. Show all flashcards \n"+
        "6. Quit \n"+
        " ---------------------------------------------------------------------------------------------------- \n"+
        "")
    input_options = {
        '1': post_topics,
        '2': add_flashcard,
        '3': start_quiz,
        '4': add_topic,
        '5': post_all_flashcards,
        '6': exit
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print('Invalid Option :/')
'''
Post topics

:return: returns content:array
'''
def post_topics(): 
    with open(json_file_const, "r") as file:
        content = json.load(file)
        json.dumps(content, indent=4)
        for i in content:
            print(i)
    return content

'''
Saves a flashcard

:param content: The name of foo
:return: returns nothing
'''
def post_all_flashcards(input_topic):
    with open(json_file_const, "r") as file:
        content = json.load(file)
        json.dumps(content, indent=4)
        for i in content[input_topic]:
            print(i)
    return content

'''
Starts the quiz
 
:return: returns nothing
'''
def start_quiz(): 
    content = post_topics()
    input_topic = input('Type the name of the topic: ').strip()

    if input_topic not in content:
        print('Topic doesn’t exist')
        return start_menu()  # Return to prevent further execution

    for question_data in content[input_topic]:
        print("\nQuestion:", question_data["question"])
        print("Type:", question_data["question-type"])

        if question_data["question-type"] == multiple_choise_type_const:
            for key, value in question_data["option"].items():
                print(f"{key}: {value}")

        input_answer = input("Your Answer: ").strip()

        if input_answer.lower() == question_data["correct-answer"].lower():
            points = manage_points(True)
            print("Correct! Points:", points)
        else:
            print("Wrong Answer. Correct answer was:", question_data["correct-answer"])

'''
Stops the application

:return: returns nothing 
'''
def exit(): 
    sys.exit()



'''
--------- "main method" --------- 
'''
while True: 
    start_menu()




