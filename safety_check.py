
def display_menu():
    print("---- Quiz Menu ----")
    print("1. Start Quiz")
    print("2. Quit")
    print("-------------------")

def start_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
            "answer": "B"
        }
    ]

    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        print(f"Question #{i+1}:")
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() == question["answer"]:
            score += 1
        print()

    print(f"Quiz completed! You scored {score}/{total_questions}.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
