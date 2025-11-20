
import random

def chatbot():
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just a computer program, but thanks for asking.",
        "what is your name": "I'm a chatbot. You can call me Chatbot.",
        "goodbye": "Goodbye! Have a great day."
    }

    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Chatbot: Goodbye! See you later.")
            break
        
        response = responses.get(user_input, "I'm sorry, I don't understand. Please ask me something else.")
        print("Chatbot:", response)

if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'quit' to exit.")
    chatbot()
