
import random

# List of possible responses from the chatbot
responses = [
    "Hello! How can I help you today?",
    "What's on your mind?",
    "Tell me more about that.",
    "I'm here to assist you.",
    "How can I make your day better?",
    "I'm listening.",
    "Let's have a chat."
]

# Function to generate a random response from the list
def get_response():
    return random.choice(responses)

# Main loop of the chatbot
while True:
    user_input = input("User: ")
    
    # Exit the loop if user types 'bye'
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day.")
        break
    
    # Generate and print a response from the chatbot
    print("Chatbot: " + get_response())
