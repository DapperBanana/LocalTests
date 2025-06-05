
# Define a list of questions with their corresponding answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria"
}

# Initialize a variable to keep track of the score
score = 0

# Iterate through each question in the questions dictionary
for question, answer in questions.items():
    # Display the question to the user
    user_answer = input(question + " ")

    # Check if the user's answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + answer)

# Display the final score to the user
print("Quiz completed. Your score is: " + str(score))
