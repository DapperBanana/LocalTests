
class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        
    def start_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            print(f"Question {i+1}: {self.questions[i]}")
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == self.answers[i].lower():
                score += 1
                print("Correct!\n")
            else:
                print("Incorrect!\n")
        
        print(f"Quiz completed! You got {score} out of {len(self.questions)} questions correct.")

# Define quiz questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who wrote the play 'Romeo and Juliet'?"
]

answers = [
    "Paris",
    "Jupiter",
    "William Shakespeare"
]

# Create a Quiz object and start the quiz
my_quiz = Quiz(questions, answers)
my_quiz.start_quiz()
