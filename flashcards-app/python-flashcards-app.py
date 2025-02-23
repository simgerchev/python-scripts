import json
import sys

json_file_const = 'flashcards.json'
short_answer_type_const = 'short-answer'
multiple_choice_type_const = 'multiple-choice'
note_type_const = 'note'
question_type_const = 'question-type'
correct_answer_const = 'correct-answer'

'''
notes 
                .---.
           '-.  |   |  .-'         
             ___|   |___          
        -=  [           ]  =-    
            `---.   .---'         
         __||__ |   | __||__      
         '-..-' |   | '-..-'   
           ||   |   |   ||     
           ||_.-|   |-,_||     
         .-"`   `"`'`   `"-.   
       .'                   '.

'''
def get_flashcard_types(): 
    flashcard_types = [multiple_choice_type_const, short_answer_type_const, note_type_const]
    return flashcard_types

def get_flashcard_type_input():
    flashcard_type_input = {
        multiple_choice_type_const: get_multiple_choice_input,
        short_answer_type_const: get_short_answer_input,
        note_type_const: get_note_input
    }
    return flashcard_type_input
       
def save_content(content):
    with open(json_file_const, "w") as file:
        json.dump(content, file, indent=4)
  
def post_topics(): 
    with open(json_file_const, "r") as file:
        content = json.load(file)
        json.dumps(content, indent=4)
        for topic in content:
            print(topic)
    return content

def check_if_answer_correct(flashcard): 
    if input("Give your answer: ") == flashcard["correct-answer"]:
        print("Answer is correct")
        return True
    else:
        print("Answer is incorrect")
        return False

def add_flashcard(): 
    content, input_topic = post_all_flashcards()
    flashcard_type = input('What flashlight do you want to add? multiple-choice / short-answer / note: ').strip().lower() 
    flashcard_type_input = get_flashcard_type_input() 
    if flashcard_type in flashcard_type_input: 
        content[input_topic].append(flashcard_type_input[flashcard_type]())
        save_content(content)
        print('Flashcard added successfully!')
        return start_menu()
    else: 
        print('Flashcard type doesnt exist')

def get_multiple_choice_output(flashcard): 
    for key, value in flashcard["option"].items():
        print(f"{key}: {value}")

def get_short_answer_output(flashcard): 
    print(flashcard["flashcard"])

def get_note_output(flashcard):
    for note in flashcard["notes"]:
        print(f"{note}")

def determine_output_type(flashcard):
    output_options = {
        multiple_choice_type_const: get_multiple_choice_output,
        short_answer_type_const: get_short_answer_output,
        note_type_const: get_note_output
    }
    if flashcard["flashcard-type"] in output_options: 
        output_options[flashcard["flashcard-type"]](flashcard)  

def post_all_flashcards():
    content = post_topics()
    input_topic = input('Type the name of the topic: ').strip().lower()
    flashcard_types = get_flashcard_types()
    if input_topic in content:
        with open(json_file_const, "r") as file:
            content = json.load(file)
            json.dumps(content, indent=4)
            for flashcard in content[input_topic]:
                print(f"Flashcard: {flashcard['flashcard']} \n ")
                if flashcard["flashcard-type"] in flashcard_types: 
                    determine_output_type(flashcard)        
    else: 
        print('Topic doesnt exist')
        return start_menu()
    return content, input_topic

def start_quiz():
    points = 0
    content = post_topics()
    input_topic = input('Type the name of the topic: ').strip().lower()
    flashcard_types = get_flashcard_types() 
    for flashcard in content[input_topic]:
        print("\nQuestion:", flashcard["flashcard"])
        print("Type:", flashcard["flashcard-type"])
        if flashcard["flashcard-type"] in flashcard_types:
            determine_output_type(flashcard)
            if flashcard["flashcard-type"] != note_type_const:
                if(check_if_answer_correct(flashcard)):
                    points += 1
    return print(points)
def get_multiple_choice_input():
    options = {}
    for input_option in ["A", "B", "C"]:
        options[input_option] = input(f'Enter the option for {input_option} here: ')
    return {"flashcard": input('Enter your flashcard here: '), "option": options, "correct-answer": input('Enter the correct answer here: '), "flashcard-type": "multiple-choice"}
    
def get_short_answer_input():
    return {"flashcard": input('Enter your flashcard here: '), "correct-answer": input('Enter the correct answer here: '), "flashcard-type": "short-answer"}

def get_note_input():
    note_input = input('Enter note')
    notes = []
    while note_input:
        notes.append(note_input)
        note_input = input('Enter yes/y if you want to add another note: ')
        if note_input == 'yes' or note_input == 'y': 
            note_input = True
        else: 
            note_input = False
    return {"flashcard": input('Enter your flashcard here: '), "notes": notes, "flashcard-type": "note"}

def add_topic():
    content = post_topics()
    topic_input = input('Enter a topic: ')
    if topic_input in content: 
        print('Topic already exists')
    else:
        content[topic_input] = []
        save_content(content)
        print('Topic added successfully')
        
def delete_topic():
    content = post_topics()
    topic_input = input('Which topic do you want to delete?')
    if topic_input in content: 
        content.pop(topic_input)
        save_content(content)
        print('Flashcard deleted successfully')
    else: 
        print("Topic does not exist")
        
def delete_flashcard(): 
    content, input_topic = post_all_flashcards()
    flashcard_input = int(input('Which flashcard do you want to delete?').strip().lower()) 
    if flashcard_input < len(content[input_topic]): 
        del content[input_topic][flashcard_input - 1]
        save_content(content)
        print('Flashcard deleted successfully!')
        return start_menu()
    else: 
        print('Flashcard does not exist')

def start_menu():
    print("----------------------------------------------------------------------------------------------------")
    input_option = input("Do you want to: 🐝\n"+ 
        "1. Show all topics\n"+
        "2. Add another flashcard \n"+
        "3. Start quiz \n"+
        "4. Add another topic \n"+
        "5. Show all flashcards \n"+
        "6. Delete Topic \n"+
        "7. Delete Flashcard \n"+
        "8. Quit \n"+
        " ---------------------------------------------------------------------------------------------------- \n"+
        "")
    input_options = {
        '1': post_topics,
        '2': add_flashcard,
        '3': start_quiz,
        '4': add_topic,
        '5': post_all_flashcards,
        '6': delete_topic,
        '7': delete_flashcard,
        '8': exit
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")
        start_menu()

while True:
    start_menu()
 
def exit(): 
    sys.exit()
  

