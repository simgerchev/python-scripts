import json
import sys

# json constants 
json_file_const = 'flashcards.json'
short_answer_type_const = 'short-answer'
multiple_choise_type_const = 'multiple-choise'
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
def save_flashcard(content):
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
Adds a question

:return: returns nothing
'''
def add_question(): 
	content = post_topics()
	input_topic = input('Type the name of the topic: ').strip().lower()
	if input_topic not in content:
		print('Topic doesnt exist')
		return start_menu()
		
	post_all_questions(input_topic)
	question_type = input('What question do you want to add? multiple-choise / short-answer').strip().lower() 

	def get_multiple_choise_input():
		options = {}
		for input_option in options["A", "B", "C"]:
			options[input_option] = input(f'Enter the option for {input_option} here: ')
		return {"question": input('Enter your question here: ').strip().lower(), "option": options}
	
	def get_short_answer_input():
		return {"question": input('Enter your question here: ').strip().lower(), "answer": input('Enter your first answer here: ').strip().lower()}
		
	question_types = {
		multiple_choise_type_const: get_multiple_choise_input
		short_answer_type_const: get_short_answer_input
	}
	
	if question_type in question_types: 
		content[input_topic].append(question_types[question_type])
		save_flashcard(content)
		print('Question added successfully!')
		return start_menu()
	else: 
		print('Question type doesnt exist')

'''
Adds a topic

:return: returns nothing
'''
def add_topic():
	content = post_topics()
	input_topic = input('Type the name of the topic you want to add: ')

'''
Function that shows the start menu

:return: returns nothing
'''
def start_menu():
	print("----------------------------------------------------------------------------------------------------")
	input_option = input("Do you want to: 🐝\n"+ 
		"1. Show all topics\n"+
		"2. Add another question \n"+
		"3. Start quiz \n"+
		"4. Quit \n"+
		" ---------------------------------------------------------------------------------------------------- \n"+
		"")
	if input_option == '1':
		post_topics()
	if input_option == '2':
		add_question()
	if input_option == '3':
		start_quiz()
	if input_option == '4':
		exit()

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
def post_all_questions(input_topic):
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




