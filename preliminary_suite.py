
def quiz():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"}
    ]

    score = 0

    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

    print(f"Quiz complete! You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    quiz()
