
def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
        
def get_user_choice(choices):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(choices):
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and", len(choices))

def check_answer(answer, user_choice):
    return answer == user_choice

questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "What is the largest planet in our solar system?": ["Earth", "Mars", "Jupiter", "Venus"],
    "Who is known as the 'Father of Computers'?": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"]
}

score = 0
for question, choices in questions.items():
    display_question(question, choices)
    user_choice = get_user_choice(choices)
    if check_answer(choices.index("Paris") + 1, user_choice):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Paris.")

print("\nQuiz Complete!")
print("Final Score:", score, "out of", len(questions))
