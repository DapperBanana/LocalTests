
# Personality quiz

print("Welcome to the personality quiz!")
print("Answer the following questions to determine your personality type.\n")

# Questions
questions = [
    "Q1 - What is your favorite color?\nA. Blue\nB. Red\nC. Green",
    "Q2 - What is your favorite season?\nA. Spring\nB. Summer\nC. Fall\nD. Winter",
    "Q3 - What is your ideal vacation spot?\nA. Beach\nB. Mountains\nC. City",
]

# Personality types and their corresponding scores
personality_types = {
    "Type A": 0,
    "Type B": 0,
    "Type C": 0,
}

# Answers
answers = []

# Ask the questions
for i, question in enumerate(questions):
    print(question)
    answer = input("Enter your choice (A/B/C/D): ").upper()
    answers.append(answer)

    # Calculate scores
    if answer == "A":
        personality_types["Type A"] += 1
    elif answer == "B":
        personality_types["Type B"] += 1
    elif answer == "C":
        personality_types["Type C"] += 1

# Determine the personality type
personality_type = max(personality_types, key=personality_types.get)

# Display the result
print("\nYour personality type is:", personality_type)
