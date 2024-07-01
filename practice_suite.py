
# Define a dictionary of questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
}

# Initialize score
score = 0

# Iterate over quiz questions
for question, correct_answer in quiz_questions.items():
    # Print question
    print(question)
    
    # Ask user for answer
    user_answer = input("Your answer: ")
    
    # Check if answer is correct
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")

# Print final score
print(f"Your score is: {score}/{len(quiz_questions)}")
