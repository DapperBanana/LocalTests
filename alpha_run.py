
def run_quiz():
    questions = {
        "Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter", "Saturn"],
        "What is the largest ocean in the world?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "Who wrote the novel 'Pride and Prejudice'?": ["Jane Austen", "F. Scott Fitzgerald", "Leo Tolstoy", "Charles Dickens"],
        "What is the capital of France?": ["Paris", "Rome", "Berlin", "London"]
    }
    
    score = 0
    
    for question, options in questions.items():
        print(question)
        
        # Print options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        # Get user's answer
        user_answer = input("Enter the number of your answer (1-4): ")
        
        # Validate answer
        if user_answer.isdigit() and int(user_answer) in range(1, 5):
            answer_index = int(user_answer) - 1
            if options[answer_index] == options[0]:
                score += 1
        else:
            print("Invalid input! Skipping question...")
    
    print(f"\nYou scored {score}/{len(questions)}")
    
run_quiz()
