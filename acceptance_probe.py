
class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + " ").lower()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# Create a list of questions
questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) London\n(c) Rome\n", ["a", "b", "c"], "a"),
    Question("Which is the largest planet in our solar system?\n(a) Jupiter\n(b) Saturn\n(c) Mars\n", ["a", "b", "c"], "a"),
    Question("What is the chemical symbol for gold?\n(a) Ag\n(b) Au\n(c) Hg\n", ["a", "b", "c"], "b"),
]

# Run the quiz
run_quiz(questions)
