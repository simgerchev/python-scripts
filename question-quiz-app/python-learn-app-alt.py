import json
import random

# File to store flashcards
FLASHCARD_FILE = "flashcards.json"

# Load flashcards from file
def load_flashcards():
    try:
        with open(FLASHCARD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save flashcards to file
def save_flashcards(flashcards):
    with open(FLASHCARD_FILE, "w") as file:
        json.dump(flashcards, file, indent=4)

# Add a new flashcard
def add_flashcard(flashcards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("\nFlashcard added successfully!\n")

# View all flashcards
def view_flashcards(flashcards):
    if not flashcards:
        print("\nNo flashcards available.\n")
        return

    print("\nAll Flashcards:")
    for i, card in enumerate(flashcards, 1):
        print(f"{i}. Question: {card['question']} | Answer: {card['answer']}")
    print()

# Start a quiz
def start_quiz(flashcards):
    if not flashcards:
        print("\nNo flashcards available to quiz on.\n")
        return

    print("\nStarting the quiz! Type 'exit' to stop.\n")
    score = 0
    random.shuffle(flashcards)

    for card in flashcards:
        print(f"Question: {card['question']}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == "exit":
            break

        if user_answer.strip().lower() == card['answer'].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {card['answer']}\n")

    print(f"\nQuiz finished! Your score: {score}/{len(flashcards)}\n")

# Main menu
def main():
    flashcards = load_flashcards()

    while True:
        print("Flashcard Quiz App")
        print("1. Add a new flashcard")
        print("2. View all flashcards")
        print("3. Start a quiz")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            view_flashcards(flashcards)
        elif choice == "3":
            start_quiz(flashcards)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()










