
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n",
    "What is 2 + 2?\n(a) 4\n(b) 5\n(c) 6\n",
    "What is the largest planet in our solar system?\n(a) Venus\n(b) Earth\n(c) Jupiter\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_quiz(questions)
