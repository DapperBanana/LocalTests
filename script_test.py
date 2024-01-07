
class Question:
    def __init__(self, prompt, choices, correct_choice):
        self.prompt = prompt
        self.choices = choices
        self.correct_choice = correct_choice

    def display_question(self):
        print(self.prompt)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def is_correct(self, choice_number):
        return self.correct_choice == choice_number


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for question in self.questions:
            question.display_question()
            choice = int(input("Enter your choice number: "))
            if question.is_correct(choice):
                self.score += 1
                print("Correct!\n")
            else:
                print("Incorrect!\n")
        print(f"You scored {self.score}/{len(self.questions)}")


if __name__ == '__main__':
    # Create quiz questions
    question1 = Question("What is the capital of France?",
                         ["Paris", "London", "Berlin", "Madrid"], 1)
    question2 = Question("Which planet is known as the red planet?",
                         ["Venus", "Mars", "Jupiter", "Saturn"], 2)
    question3 = Question("Who invented the telephone?",
                         ["Isaac Newton", "Thomas Edison", "Alexander Graham Bell", "Nikola Tesla"], 3)

    # Create quiz and add questions
    quiz = Quiz()
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)

    # Run the quiz
    quiz.run()
