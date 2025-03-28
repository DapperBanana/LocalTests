
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
questions = [
    Question("What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n", "b"),
    Question("What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n", "b"),
    Question("What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
            
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_quiz(questions)
