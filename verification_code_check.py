
def take_quiz():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2+2?", "answer": "4"},
        {"question": "Who wrote Romeo and Juliet?", "answer": "Shakespeare"}
    ]
    
    score = 0
    
    for question in questions:
        user_answer = input(question["question"] + "\n")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + question["answer"])
    
    print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")
    
take_quiz()
