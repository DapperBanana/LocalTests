
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    Quiz("What is the capital of France?", "Paris"),
    Quiz("What is the largest planet in our solar system?", "Jupiter"),
    Quiz("Who wrote Romeo and Juliet?", "William Shakespeare")
]

score = 0

for q in questions:
    user_answer = input(q.question + "\nYour answer: ")
    if user_answer.lower() == q.answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer is {q.answer}")

print(f"Quiz complete! You got {score}/{len(questions)} questions correct.")
