
# Quiz questions and answers
questions = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n",
    "Who wrote the play 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Jane Austen\n(c) Charles Dickens\n",
    "What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n"
]

answers = ["b", "a", "b"]

# Function to run the quiz
def run_quiz(questions, answers):
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Enter your answer (a, b, or c): ")
        if user_answer.lower() == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is {}\n".format(answers[i]))
    
    print("You got {} out of {} questions correct.".format(score, len(questions))

# Run the quiz
run_quiz(questions, answers)
