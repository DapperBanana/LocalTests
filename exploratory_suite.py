
# Question dictionary with questions as keys and answers as values
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the play Romeo and Juliet?": "William Shakespeare"
}

score = 0

print("Welcome to the Educational Quiz!")
print("Please answer the following questions:")

for question, correct_answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: {}".format(correct_answer))

print("\nQuiz complete!")
print("Your final score is: {}/{}".format(score, len(questions)))
