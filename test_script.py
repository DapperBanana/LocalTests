
# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    }
]

# Function to display question and options
def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your choice (1/2/3/4): ")
    return user_answer

# Function to check answer
def check_answer(answer, user_answer):
    if answer == answer_key[int(user_answer)-1]:
        return True
    else:
        return False

# Start quiz
score = 0
answer_key = [question["answer"] for question in questions]

print("Welcome to the Quiz!")

for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}:")
    user_answer = display_question(question)
    
    if check_answer(question["answer"], user_answer):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    print(f"Current Score: {score}/{i+1}")

print("\nQuiz completed!")
print(f"Your final score is: {score}/{len(questions)}")
