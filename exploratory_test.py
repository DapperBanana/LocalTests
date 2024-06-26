
# Define a list of questions and their correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": ["A. J.K. Rowling", "B. George R.R. Martin", "C. Stephen King", "D. Suzanne Collins"],
        "answer": "A"
    }
]

# Function to display the quiz questions and get user input
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ")
        
        if user_answer.upper() == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is {}\n".format(question["answer"]))
    
    print("Quiz completed. You scored {}/{}.".format(score, len(questions))

# Run the quiz
run_quiz(questions)
