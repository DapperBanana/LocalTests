
class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i+1}. {choice}")

    def check_answer(self, answer):
        if answer == self.correct_answer:
            return True
        else:
            return False

questions = [
    Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
    Question("What is the largest planet in our solar system?", ["Neptune", "Mars", "Saturn", "Jupiter"], 4),
    Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], 2),
    Question("Which country is the largest by land area?", ["Russia", "China", "USA", "Canada"], 1),
    Question("What is the main ingredient in guacamole?", ["Tomato", "Onion", "Avocado", "Lemon"], 3)
]

score = 0
for question in questions:
    question.display_question()
    answer = int(input("Enter your answer (1-4): "))
    if question.check_answer(answer):
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

print(f"You scored {score}/{len(questions)}")
