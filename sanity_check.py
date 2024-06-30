
def quiz():
    questions = [
        {
            'question': 'What is the capital of France?',
            'choices': ['Berlin', 'London', 'Paris', 'Rome'],
            'answer': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'choices': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
            'answer': 'Mars'
        },
        {
            'question': 'Who is the author of the Harry Potter series?',
            'choices': ['J.R.R. Tolkien', 'J.K. Rowling', 'Stephenie Meyer', 'George R.R. Martin'],
            'answer': 'J.K. Rowling'
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        print("Question", i+1)
        print(q['question'])
        for j, choice in enumerate(q['choices']):
            print(j+1, choice)
        
        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        
        if q['choices'][int(user_answer)-1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", q['answer'])
        
        print()
    
    print("Quiz complete! You got", score, "out of", len(questions), "questions correct.")

if __name__ == "__main__":
    quiz()
