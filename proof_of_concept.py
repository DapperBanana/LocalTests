
class Quiz:
    def __init__(self):
        self.questions = []
        self.answers = []

    def add_question(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)

    def administer_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            print(self.questions[i])
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == self.answers[i].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is: " + self.answers[i])

        print("Quiz complete. You scored {} out of {}.".format(score, len(self.questions))


# Create an instance of the Quiz class
quiz = Quiz()

# Add questions and answers to the quiz
quiz.add_question("What is the capital of France?", "Paris")
quiz.add_question("What is the largest planet in our solar system?", "Jupiter")
quiz.add_question("Who wrote the play Romeo and Juliet?", "William Shakespeare")

# Administer the quiz
quiz.administer_quiz()
