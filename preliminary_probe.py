
def quiz():
    questions = ["What is the capital of France? ", 
                 "What is the largest planet in our solar system? ",
                 "Who painted the Mona Lisa? "]
    
    answers = ["Paris", "Jupiter", "Leonardo da Vinci"]
    
    score = 0
    
    for i in range(len(questions)):
        user_answer = input(questions[i])
        
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + answers[i])
    
    print("Quiz complete!")
    print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")
    percentage = (score / len(questions)) * 100
    print("Your score is: " + str(percentage) + "%")
    
quiz()
