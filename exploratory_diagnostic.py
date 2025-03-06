
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote Romeo and Juliet?": "William Shakespeare"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + "\n")
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is: {}\n".format(answer))

print("Quiz complete! You scored {}/{}.\n".format(score, len(questions)))
