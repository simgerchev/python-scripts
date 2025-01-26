import json
import sys

json_file_const = 'random.json'

def save_flashcard(content):
	with open(json_file_const, "w") as file:
		json.dump(content, file, indent=4)


def change_question(): 
	content = post_topics()
	input_topic = input('Type the name of the topic: ')
	if input_topic in content:
		post_all_questions(input_topic)
		input_question_number = int(input('Type the number of the question you want to edit: '))
		input_type = input('Question or Answer: ')

		if input_type == 'question': 
			input_content = input('Enter your content: ')
			content[input_topic][input_question_number - 1][input_type] = input_content
		elif input_type == 'answer':
			input_option = input('Choose your option: ')
			input_content = input('Enter your content: ')
			content[input_topic][input_question_number - 1][input_type][input_option] = input_content
		else:
			print('Invalid Type')
			start_menu()
	else: 
		print('Key doesnt exist')
		start_menu()
	
	save_flashcard(content)

def add_question(): 
	content = post_topics()
	input_topic = input('Type the name of the topic: ')
	content = post_all_questions(input_topic)
	input_question = input('Enter your question here: ')
	input_first_answer = input('Enter your first answer here: ')
	input_second_answer = input('Enter your second answer here: ')
	input_third_answer = input('Enter your third answer here: ')

	new_entry = {"question": input_question, "answer": {"A":input_first_answer, "B":input_second_answer, "C":input_third_answer}}
	content[input_topic].append(new_entry)
	save_flashcard(content)

def add_topic():
	content = post_topics()
	input_topic = input('Type the name of the topic you want to add: ')

def start_menu():
	print("----------------------------------------------------------------------------------------------------")
	input_option = input("Do you want to: \n"+ 
		"1. Change existing question \n"+
		"2. Add another question \n"+
		"3. Show all topics \n"+
		"4. Quit \n"+
		" ---------------------------------------------------------------------------------------------------- \n"+
		"")
	if input_option == '1': 
		change_question() 
	if input_option == '2':
		add_question()
	if input_option == '3':
		post_topics()
	if input_option == '4':
		exit()

def post_topics(): 
	with open(json_file_const, "r") as file:
		content = json.load(file)
		json.dumps(content, indent=4)
		for i in content:
			print(i)
	return content

def post_all_questions(input_topic):
	with open(json_file_const, "r") as file:
		content = json.load(file)
		json.dumps(content, indent=4)
		for i in content[input_topic]:
			print(i)
	return content

def exit(): 
	sys.exit()


while True: 
	start_menu()
