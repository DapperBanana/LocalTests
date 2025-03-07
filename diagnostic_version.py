
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Rome\n",
    "What is the largest planet in our solar system?\n(a) Venus\n(b) Saturn\n(c) Jupiter\n",
    "Who wrote the play 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            
    print("You got", score, "out of", len(questions), "questions correct")

run_quiz(questions)
