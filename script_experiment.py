
# Personality quiz questions
questions = [
    "What is your favorite color? (a) Red (b) Blue (c) Green",
    "What is your favorite animal? (a) Dog (b) Cat (c) Bird",
    "What is your ideal vacation? (a) Beach resort (b) Mountain retreat (c) City exploration"
]

# Personality trait scores
traits = {
    "a": "Adventurous",
    "b": "Introverted",
    "c": "Social"
}

# Initialize trait scores
scores = {
    "Adventurous": 0,
    "Introverted": 0,
    "Social": 0
}

def get_user_input(question):
    while True:
        user_input = input(question + " ")
        if user_input.lower() in ['a', 'b', 'c']:
            return user_input.lower()
        else:
            print("Please enter a valid option (a, b, c)")

# Quiz loop
print("Welcome to the Personality Quiz!")
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
    answer = get_user_input("Choose a, b, or c:")
    trait = traits[answer]
    scores[trait] += 1

# Determine personality type
personality_type = max(scores, key=scores.get)
print(f"\nYour personality type is: {personality_type}")
