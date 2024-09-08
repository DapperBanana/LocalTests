
def ask_question(question, options, answer):
    print(question)
    for idx, choice in enumerate(options):
        print(f"{idx + 1}. {choice}")
    
    user_answer = int(input("Enter your answer: "))
    
    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is: ", options[answer - 1])
        return False

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": 2
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 2
    }
]

score = 0

for question in questions:
    if ask_question(question["question"], question["options"], question["answer"]):
        score += 1

print(f"You got {score}/{len(questions)} questions correct.")
