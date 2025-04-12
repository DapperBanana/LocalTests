
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n", "b"),
    Question("What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n", "b"),
    Question("Who wrote the play 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Jane Austen\n(c) J.K. Rowling\n", "a")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer was: " + question.answer + "\n")

    print("You got " + str(score) + "/" + str(len(questions)) + " questions correct.")

run_quiz(questions)
