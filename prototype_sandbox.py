
class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

questions = [
    Question("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Berlin"], "B"),
    Question("What is the largest planet in our solar system?", ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"], "B"),
    Question("What is the atomic number of oxygen?", ["A. 6", "B. 8", "C. 12", "D. 16"], "B"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for choice in question.choices:
            print(choice)
        answer = input("Enter your answer: ").upper()
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is {}\n".format(question.answer))
    
    print("Quiz completed! You got {} out of {} questions correct.".format(score, len(questions))

run_quiz(questions)
