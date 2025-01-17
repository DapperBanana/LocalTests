
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for q in self.questions:
            print(q)
            answer = input("Your answer: ")
            if answer.lower() == self.questions[q]:
                self.score += 1

        print(f"You got {self.score} out of {len(self.questions)} questions correct.")

questions = {
    "What is the capital of France?": "a",
    "What is 2 + 2?": "b",
    "Who is the current President of the United States?": "c"
}

quiz = Quiz(questions)
quiz.run_quiz()
