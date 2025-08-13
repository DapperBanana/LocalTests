
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define the list of questions
questions = [
    Question("What is the capital of France?\n(a) London\n(b) Berlin\n(c) Paris\n", "c"),
    Question("What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n", "b"),
    Question("What is the largest planet in our solar system?\n(a) Venus\n(b) Jupiter\n(c) Earth\n", "b")
]

# Helper function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: {}\n".format(question.answer))
    
    print("You got {} out of {} questions correct.".format(score, len(questions))

# Run the quiz
run_quiz(questions)
