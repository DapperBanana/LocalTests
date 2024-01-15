
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            print(question.prompt)
            for i, option in enumerate(question.options):
                print(f"{i+1}. {option}")

            user_answer = input("Enter your answer (1-4): ")
            self.check_answer(question, int(user_answer))

        print(f"\nYou scored {self.score}/{len(self.questions)}")

    def check_answer(self, question, user_answer):
        if user_answer == question.answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")

# Define the questions
question1 = Question("What is the capital of Brazil?", ["A. Rio de Janeiro", "B. São Paulo", "C. Brasília", "D. Salvador"], 3)
question2 = Question("What is the largest continent on Earth?", ["A. Asia", "B. Africa", "C. Europe", "D. North America"], 1)
question3 = Question("Which planet is closest to the Sun?", ["A. Mars", "B. Venus", "C. Mercury", "D. Jupiter"], 3)

# Create the quiz and run it
quiz = Quiz([question1, question2, question3])
quiz.run_quiz()
