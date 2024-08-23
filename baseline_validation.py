
questions = {
    "What is the capital of France?": {
        "A": "London",
        "B": "Paris",
        "C": "Berlin",
        "D": "Madrid"
    },
    "Which planet is known as the Red Planet?": {
        "A": "Venus",
        "B": "Mars",
        "C": "Jupiter",
        "D": "Saturn"
    },
    "What is the largest mammal in the world?": {
        "A": "Elephant",
        "B": "Blue Whale",
        "C": "Giraffe",
        "D": "Hippopotamus"
    }
}

answers = {
    "What is the capital of France?": "B",
    "Which planet is known as the Red Planet?": "B",
    "What is the largest mammal in the world?": "B"
}

score = 0

for question, options in questions.items():
    print(question)
    for option, value in options.items():
        print(option + ": " + value)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer == answers[question]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is " + answers[question] + "\n")

print("Quiz complete!")
print("Your score is: " + str(score) + "/" + str(len(questions)))
