
import random

# List of possible responses from the chatbot
responses = [
    "Hello! How can I help you?",
    "What's on your mind?",
    "Tell me more about that.",
    "I'm here to chat with you.",
    "How are you feeling today?",
    "Let's talk about something interesting.",
    "I'm here to listen."
]

while True:
    user_input = input("You: ").lower()

    # Check if the user wants to quit the chatbot
    if user_input == "quit":
        print("Chatbot: Goodbye! Have a great day.")
        break

    # Generate a random response from the chatbot
    response = random.choice(responses)
    print("Chatbot:", response)
