
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare"
}

def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + "\n")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: {}\n".format(answer))

    print("Quiz complete! You scored {}/{}.".format(score, len(questions))

run_quiz(questions)
