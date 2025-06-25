
print("Welcome to the Personality Quiz!")
print("Answer the following questions to find out more about your personality.")

# Questions for the quiz
questions = [
    "What is your favorite color?\nA) Red\nB) Blue\nC) Green\nD) Yellow",
    "What is your favorite animal?\nA) Dog\nB) Cat\nC) Bird\nD) Fish",
    "What is your ideal vacation spot?\nA) Beach\nB) Mountains\nC) City\nD) Countryside",
    "What is your favorite hobby?\nA) Reading\nB) Sports\nC) Cooking\nD) Painting"
]

# Answers list to store user's choices
answers = []

# Loop through each question and get user's choice
for i, question in enumerate(questions):
    print(question)
    answer = input("Enter your choice (A, B, C, or D): ").upper()
    answers.append(answer)

# Calculate the result based on user's answers
score = 0
for answer in answers:
    if answer == 'A':
        score += 1
    elif answer == 'B':
        score += 2
    elif answer == 'C':
        score += 3
    elif answer == 'D':
        score += 4

# Determine user's personality based on score
if score >= 4 and score <= 6:
    print("You are a creative and artistic person!")
elif score >= 7 and score <= 10:
    print("You are a nature lover and enjoy outdoor activities!")
elif score >= 11 and score <= 14:
    print("You are a social and outgoing person!")
elif score >= 15 and score <= 16:
    print("You are a bookworm and enjoy quiet activities!")

print("Thank you for taking the Personality Quiz!")
