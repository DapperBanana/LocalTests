
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for q in self.questions:
            print(q)
            answer = input("Enter your answer: ")
            if answer.lower() == self.questions[q].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer is: " + self.questions[q])
        
        print("Quiz complete! You scored: ", self.score)

# Define the questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "How many continents are there?": "7",
}

# Create an instance of the Quiz class and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
