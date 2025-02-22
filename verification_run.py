
def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_user_answer():
    while True:
        user_input = input("Enter your answer: ")
        
        try:
            user_answer = int(user_input)
            if user_answer < 1 or user_answer > 4:
                raise ValueError
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Rome"],
        "correct_answer": 3
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Ribosome", "Mitochondria", "Endoplasmic Reticulum", "Nucleus"],
        "correct_answer": 2
    }
]

score = 0

for question in questions:
    display_question(question["question"], question["options"])
    user_answer = get_user_answer()
    if check_answer(user_answer, question["correct_answer"]):
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is option {}.\n".format(question["correct_answer"]))

print("Quiz completed! You scored {}/{}.".format(score, len(questions)))
