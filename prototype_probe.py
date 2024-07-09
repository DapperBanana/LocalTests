
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

questions = [
    Question("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Rome"], "B"),
    Question("What is the largest planet in our solar system?", ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"], "B"),
    Question("Who wrote the famous play Romeo and Juliet?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. J.K. Rowling"], "A")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for option in question.options:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is {}\n".format(question.answer))
    print("You got {}/{} questions correct.".format(score, len(questions))

run_quiz(questions)
