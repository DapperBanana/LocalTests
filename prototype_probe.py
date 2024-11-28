
print("Welcome to the Personality Quiz!")
print("Answer the following questions with A, B, C, or D")

# Questions for the personality quiz
questions = [
    "What is your favorite color?\nA) Red\nB) Blue\nC) Green\nD) Yellow",
    "What is your favorite season?\nA) Summer\nB) Winter\nC) Spring\nD) Fall",
    "How do you prefer to spend your weekends?\nA) Going out with friends\nB) Reading a book\nC) Hiking in nature\nD) Watching movies at home"
]

# List of personality types
personality_types = {
    "A": "Bold and adventurous",
    "B": "Introverted and analytical",
    "C": "Nature lover and free-spirited",
    "D": "Easygoing and laid-back"
}

# Initialize empty list to store user answers
answers = []

# Loop through each question and get user input
for question in questions:
    print(question)
    answer = input("Your choice: ").upper()
    
    # Check if user input is valid
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Please enter A, B, C, or D")
        answer = input("Your choice: ").upper()
    
    answers.append(answer)

# Calculate the personality type based on user answers
personality_count = {}
for answer in answers:
    if answer in personality_count:
        personality_count[answer] += 1
    else:
        personality_count[answer] = 1

# Determine the most common personality type
most_common_type = max(personality_count, key=personality_count.get)

# Print out the user's personality type
print("\nYou are a:", personality_types[most_common_type])
