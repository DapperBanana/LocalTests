
class Question:
    def __init__(self, prompt, answers, correct_answer):
        self.prompt = prompt
        self.answers = answers
        self.correct_answer = correct_answer

questions = [
    Question("What is the capital of France?", ["A) London", "B) Paris", "C) Berlin", "D) Rome"], "B"),
    Question("What is 2 + 2?", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
    Question("Who is the current president of the United States?", ["A) Barack Obama", "B) Donald Trump", "C) Joe Biden", "D) George Bush"], "C"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n" + "\n".join(question.answers) + "\n")
        if answer.upper() == question.correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + question.correct_answer + "\n")
    
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_quiz(questions)
