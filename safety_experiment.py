
def run_quiz():
    # Define quiz questions and answers
    questions = [
        "What is the capital of France? ",
        "What is the largest planet in our solar system? ",
        "What is the powerhouse of the cell? "
    ]
    
    answers = [
        "Paris",
        "Jupiter",
        "Mitochondria"
    ]
    
    # Initialize score
    score = 0
    
    # Ask questions and check answers
    for i in range(len(questions)):
        user_answer = input(questions[i])
        
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + answers[i])
    
    # Print final score
    print("Quiz completed. You scored {} out of {}.".format(score, len(questions))

# Run the quiz
run_quiz()
