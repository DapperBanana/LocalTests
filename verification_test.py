
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the powerhouse of the cell?": "Mitochondria"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + answer)

print("Quiz complete! You got {} out of {} questions correct.".format(score, len(questions)))
