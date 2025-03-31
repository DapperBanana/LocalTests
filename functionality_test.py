
# Define the questions and their corresponding options and answers
questions = {
    "What is the capital of France?": {
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": "Paris"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    "What is the largest mammal in the world?": {
        "options": ["Elephant", "Blue whale", "Giraffe", "Hippo"],
        "answer": "Blue whale"
    }
}

# Function to display the questions and get the user's answers
def take_quiz(questions):
    score = 0

    for question, data in questions.items():
        print(question)
        for i, option in enumerate(data["options"]):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of your choice: ")
        if data["options"][int(user_answer) - 1] == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", data["answer"])

        print()

    print(f"Quiz completed! Your score is: {score}/{len(questions)}")

# Run the quiz
take_quiz(questions)
