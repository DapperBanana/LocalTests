
# Define the questions and answers
questions = {
    "What is the capital of France?": {
        "a": "Paris",
        "b": "London",
        "c": "Berlin"
    },
    "Which planet is known as the Red Planet?": {
        "a": "Mars",
        "b": "Jupiter",
        "c": "Venus"
    },
    "What is the largest mammal on Earth?": {
        "a": "Elephant",
        "b": "Blue Whale",
        "c": "Giraffe"
    }
}

# Store the correct answers
correct_answers = {
    "What is the capital of France?": "a",
    "Which planet is known as the Red Planet?": "a",
    "What is the largest mammal on Earth?": "b"
}

# Function to administer the quiz
def administer_quiz(questions, correct_answers):
    score = 0
    for question, choices in questions.items():
        print(question)
        for choice, answer in choices.items():
            print(f"{choice}) {answer}")
        
        user_answer = input("Enter your choice: ")
        
        if user_answer.lower() == correct_answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"\nYour final score is: {score}/{len(questions)}")

# Run the quiz
administer_quiz(questions, correct_answers)
