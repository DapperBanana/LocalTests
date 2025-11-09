
def get_user_input(question):
    user_input = input(f"{question} ")
    return user_input

def check_answer(question, correct_answer):
    user_answer = get_user_input(question)
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print("Incorrect. The correct answer is: " + correct_answer + "\n")
        return False

def quiz():
    score = 0

    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote the Harry Potter book series?": "J.K. Rowling"
    }

    for question, answer in questions.items():
        if check_answer(question, answer):
            score += 1

    print(f"You scored {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
