
import random

# List of possible responses
responses = [
    "Hello! How can I help you today?",
    "What's on your mind?",
    "I'm here to chat! What's up?",
    "Tell me more...",
    "That's interesting. Please tell me more."
]

# Main chatbot function
def chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Select a random response from the list and print it
        response = random.choice(responses)
        print("Bot:", response)

# Run the chatbot
chatbot()
