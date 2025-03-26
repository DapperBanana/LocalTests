
# Define the questions and their corresponding answers

questions = [
    "What is your favorite color?\nA. Red\nB. Blue\nC. Green\n",
    "What is your ideal vacation spot?\nA. Beach\nB. Mountains\nC. City\n",
    "What is your favorite season?\nA. Summer\nB. Fall\nC. Winter\n",
]

# Define the personality types and their corresponding descriptions

personalities = {
    "A": "You are an adventurous and outgoing person.",
    "B": "You are a calm and introspective person.",
    "C": "You are a creative and imaginative person."
}

# Function to administer the quiz

def personality_quiz():
    print("Welcome to the Personality Quiz!\n")
    personality = ""
    
    for question in questions:
        answer = input(question).upper()
        
        if answer in personalities:
            personality += answer
        else:
            print("Invalid response. Please choose A, B, or C.")
    
    print("\nBased on your answers, you are:", personalities[personality])

# Run the personality quiz

personality_quiz()
