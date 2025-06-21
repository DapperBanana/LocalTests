
def quiz():
    questions = ["What is the capital of France?", "What is the largest ocean on Earth?", "What is the powerhouse of the cell?"]
    answers = ["Paris", "Pacific", "Mitochondria"]
    score = 0
    
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answers[i])
    
    print("Quiz complete! You scored", score, "out of", len(questions))

quiz()
