
print("Welcome to the Personality Quiz!")

questions = [
    "1. What is your favorite color?\nA. Red\nB. Blue\nC. Green\n",
    "2. What is your favorite animal?\nA. Dog\nB. Cat\nC. Bird\n",
    "3. How do you prefer to spend your free time?\nA. Outdoors\nB. Indoors\nC. Socializing\n"
]

answers = []

for question in questions:
    answer = input(question)
    answers.append(answer.upper())

# Calculate the score based on the answers
score = 0
for ans in answers:
    if 'A' in ans:
        score += 1
    elif 'B' in ans:
        score += 2
    elif 'C' in ans:
        score += 3

# Determine the personality type based on the score
if score <= 4:
    personality = "Introverted and thoughtful"
elif score <= 8:
    personality = "Balanced and adaptable"
else:
    personality = "Outgoing and sociable"

print(f"Your personality type is: {personality}")
