
# Define the questions for the personality quiz
questions = {
    "1": "What is your favorite color?\nA) Red\nB) Blue\nC) Green\nD) Yellow",
    "2": "What is your favorite animal?\nA) Dog\nB) Cat\nC) Bird\nD) Horse",
    "3": "What is your favorite season?\nA) Spring\nB) Summer\nC) Fall\nD) Winter"
}

# Define the personality types based on the user's answers
personalities = {
    "ABCD": "You are a social and outgoing individual.",
    "ACBD": "You are a creative and artistic person.",
    "ADBC": "You are a calm and thoughtful soul.",
    "BACD": "You are a confident and ambitious go-getter."
}

# Initialize an empty string to store user's answers
answers = ""

# Iterate through the questions and get user's answers
for q_num, question in questions.items():
    print(question)
    answer = input("Enter your choice (A/B/C/D): ").upper()
    
    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid choice, please select A, B, C, or D.")
        answer = input("Enter your choice (A/B/C/D): ").upper()
    
    answers += answer

# Get the user's personality type based on their answers
personality = personalities.get(answers, "You have a unique personality!")

# Display the user's personality type
print("\nYour personality type is:", personality)
