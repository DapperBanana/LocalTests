
class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers

    def run_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            print(f"Question {i + 1}: {self.questions[i]}")
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == self.answers[i].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        print(f"Quiz complete! You got {score} out of {len(self.questions)} questions correct.")

# Define the questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the powerhouse of the cell?"
]
answers = [
    "Paris",
    "Jupiter",
    "Mitochondria"
]

# Create a Quiz object and run the quiz
quiz = Quiz(questions, answers)
quiz.run_quiz()
