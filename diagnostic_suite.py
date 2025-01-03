
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
question_prompts = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n",
    "Who wrote the novel 'Pride and Prejudice'?\n(a) Emily Bronte\n(b) Jane Austen\n(c) Charlotte Bronte\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_quiz(questions)
