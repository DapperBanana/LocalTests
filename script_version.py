
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question("What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n", "b"),
    Question("What is the largest mammal?\n(a) Elephant\n(b) Blue whale\n(c) Giraffe\n", "b"),
    Question("What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Chloroplast\n", "b")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")


run_quiz(questions)
