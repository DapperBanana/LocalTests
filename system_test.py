
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer.lower() == user_answer.lower()

quiz1 = Quiz("What is the capital of France?", "Paris")
quiz2 = Quiz("What is the largest planet in our solar system?", "Jupiter")
quiz3 = Quiz("Who wrote the Harry Potter book series?", "J.K. Rowling")

quiz_list = [quiz1, quiz2, quiz3]

score = 0

for quiz in quiz_list:
    user_answer = input(quiz.question + " ")
    if quiz.check_answer(user_answer):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + quiz.answer)

print("Quiz complete! You scored " + str(score) + " out of " + str(len(quiz_list)))
