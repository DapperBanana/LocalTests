
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O"
}

score = 0

for question in questions:
    answer = input(question + "\nYour answer: ")
    if answer.lower() == questions[question].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + questions[question])

print("Quiz complete. You scored {} out of {}.".format(score, len(questions)))
