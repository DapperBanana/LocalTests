
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What is the chemical symbol for gold?": "Au",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare"
}

score = 0

print("Welcome to the Educational Quiz!")

for question, answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

print(f"Quiz completed! Your score is: {score}/{len(questions)}")
