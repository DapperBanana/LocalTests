
# define the quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the square root of 16?": "4",
    "Who wrote the novel 'Pride and Prejudice'?": "Jane Austen"
}

# initialize the score
score = 0

# iterate over each question and present it to the user
for question, answer in questions.items():
    print(question)
    user_answer = input("Your answer: ")

    # check if the user's answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# display the final score
print("Quiz completed!")
print("Your score:", score, "out of", len(questions))
