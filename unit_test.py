
questions = [
    "What is the capital of France?\n(a) Paris\n(b) Rome\n(c) Madrid\n",
    "Which is the largest planet in our solar system?\n(a) Jupiter\n(b) Mars\n(c) Saturn\n",
    "Who is known as the father of computer science?\n(a) Alan Turing\n(b) Steve Jobs\n(c) Bill Gates\n"
]

answers = ["a", "a", "a"]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Enter your answer (a, b, or c): ").lower()
    if user_answer == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

print("Quiz complete!")
print("Your score:", score, "out of", len(questions))
