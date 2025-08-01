
class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers

    def run_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            print(self.questions[i])
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == self.answers[i].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is", self.answers[i])
        
        print("Quiz complete! You scored", score, "out of", len(self.questions))

# Main program
questions = ["What is the capital of France?", "What is the largest planet in our solar system?", "Who wrote Romeo and Juliet?"]
answers = ["Paris", "Jupiter", "William Shakespeare"]

quiz = Quiz(questions, answers)
quiz.run_quiz()
