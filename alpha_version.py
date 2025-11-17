
def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

def get_user_input():
    while True:
        user_input = input("Enter your answer (1, 2, 3, etc.): ")
        if user_input.isdigit():
            return int(user_input)

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["London", "Paris", "Berlin"],
            "correct_answer": 2
        },
        {
            "question": "What is 2 + 2?",
            "choices": ["3", "4", "5"],
            "correct_answer": 2
        },
        {
            "question": "Who wrote Romeo and Juliet?",
            "choices": ["William Shakespeare", "Jane Austen", "Charles Dickens"],
            "correct_answer": 1
        }
    ]

    score = 0

    for question in questions:
        display_question(question["question"], question["choices"])
        user_answer = get_user_input()
        if check_answer(user_answer, question["correct_answer"]):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    main()
