
def quiz(question, options, answer):
    print(question)
    
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your choice (1-4): "))
    
    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", options[answer-1])
        return False

# Quiz questions
questions = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 2),
    ("What is the largest planet in our solar system?", ["Venus", "Mars", "Jupiter", "Saturn"], 3),
    ("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"], 1)
]

score = 0

# Run the quiz
for q in questions:
    if quiz(*q):
        score += 1

print(f"Your final score is: {score}/{len(questions)}")
