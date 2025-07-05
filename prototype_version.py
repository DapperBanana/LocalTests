
questions = {
    "What is the capital of France?": {
        "A": "London",
        "B": "Paris",
        "C": "Berlin",
        "D": "Madrid",
        "correct_answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "A": "Mars",
        "B": "Jupiter",
        "C": "Earth",
        "D": "Venus",
        "correct_answer": "A"
    },
    "Who wrote the play 'Romeo and Juliet'?": {
        "A": "William Shakespeare",
        "B": "Jane Austen",
        "C": "Charles Dickens",
        "D": "Mark Twain",
        "correct_answer": "A"
    }
}

score = 0

for question, options in questions.items():
    print(question)
    for option, answer in options.items():
        if option != "correct_answer":
            print(f"{option}: {answer}")
    user_answer = input("Enter your answer: ").upper()
    if user_answer == options["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {options['correct_answer']}")

print(f"Quiz complete! Your score is {score}/{len(questions)}")
