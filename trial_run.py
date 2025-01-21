
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

quiz_questions = [
    Quiz("What is the capital of France?", "Paris"),
    Quiz("What is the largest planet in our solar system?", "Jupiter"),
    Quiz("What is the powerhouse of the cell?", "Mitochondria"),
    Quiz("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    Quiz("What year did World War II end?", "1945")
]

def run_quiz(quiz_questions):
    score = 0
    for quiz in quiz_questions:
        user_answer = input(quiz.question + "\n")
        if user_answer.lower() == quiz.answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + quiz.answer)
    print("Quiz completed! You got", score, "out of", len(quiz_questions), "questions correct.")

run_quiz(quiz_questions)
