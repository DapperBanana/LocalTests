
import random

# Define responses for the chatbot
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a chatbot, I don't have feelings but thanks for asking!",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand. Can you please rephrase your question?"
}

# Define function to simulate chatbot behavior
def chatbot():
    print("Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot:", responses["default"])

        if "goodbye" in user_input:
            break

if __name__ == "__main__":
    chatbot()
