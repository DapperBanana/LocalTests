
# Personality Quiz

print("Welcome to the Personality Quiz!")

# Questions
questions = [
    "1. What is your favorite color?\n a) Red\n b) Blue\n c) Green\n",
    "2. What is your favorite animal?\n a) Dog\n b) Cat\n c) Bird\n",
    "3. How do you like to spend your free time?\n a) Reading\n b) Watching TV\n c) Outdoor activities\n"
]

# Answers
answers = ["a", "b", "c"]

# User's answers
user_answers = []

# Ask each question and record user's answers
for question in questions:
    user_answer = input(question)
    user_answers.append(user_answer)

# Calculate results
result_a = user_answers.count("a")
result_b = user_answers.count("b")
result_c = user_answers.count("c")

# Determine personality type based on the results
if result_a > result_b and result_a > result_c:
    personality_type = "Type A"
elif result_b > result_a and result_b > result_c:
    personality_type = "Type B"
else:
    personality_type = "Type C"

# Display result
print(f"Your personality type is: {personality_type}")
