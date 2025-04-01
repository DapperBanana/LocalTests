
# Define the questions and choices
questions = {
    "What is the capital of France?": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
    "What is the largest planet in our solar system?": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
    "Who painted the Mona Lisa?": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"]
}

# Define the answers
answers = {
    "What is the capital of France?": "B",
    "What is the largest planet in our solar system?": "B",
    "Who painted the Mona Lisa?": "A"
}

# Function to display the quiz and get user input
def run_quiz(questions, answers):
    score = 0
    for question, choices in questions.items():
        print(question)
        for choice in choices:
            print(choice)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", answers[question])
    
    print("Quiz completed. Your score is:", score)

# Run the quiz
run_quiz(questions, answers)
