
class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.score = 0

    def run_quiz(self):
        for i in range(len(self.questions)):
            print(f"Question {i+1}: {self.questions[i]}")
            answer = input("Enter your answer: ")
            if answer.lower() == self.answers[i].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is {self.answers[i]}")
        
        print(f"Quiz completed. Your score is {self.score}/{len(self.questions)}")

# Define the questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?"
]
answers = [
    "Paris",
    "Jupiter",
    "William Shakespeare"
]

# Create a Quiz object and run the quiz
quiz = Quiz(questions, answers)
quiz.run_quiz()
