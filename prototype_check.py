
def display_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your choice (1, 2, 3, etc.): ")
    return int(user_answer)

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer was: " + str(correct_answer))
        return False

def run_quiz(quiz_questions):
    score = 0
    for question, options, correct_answer in quiz_questions:
        user_answer = display_question(question, options)
        if check_answer(user_answer, correct_answer):
            score += 1
    print("You scored", score, "out of", len(quiz_questions))

quiz_questions = [
    ("What is the capital of France?", ["Paris", "London", "Berlin"], 1),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus"], 2),
    ("What is 2 + 2?", ["3", "4", "5"], 2)
]

run_quiz(quiz_questions)
