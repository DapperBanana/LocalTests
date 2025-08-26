
def display_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1, 2, 3, 4): ")
    return answer

def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is {}.".format(correct_answer))
        return False

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "correct_answer": "2"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Venus", "Saturn", "Jupiter", "Mars"],
        "correct_answer": "3"
    }
]

score = 0

for question in questions:
    user_answer = display_question(question["question"], question["options"])
    if check_answer(question["correct_answer"], user_answer):
        score += 1

print("Quiz complete! You scored {}/{}.".format(score, len(questions)))
