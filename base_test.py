
import random

def get_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm just a computer program, so I don't have feelings.",
        "what is your name": "I'm a chatbot, you can call me Bot.",
        "bye": "Goodbye, have a great day!"
    }
    
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm not sure how to respond to that."

def chat():
    print("Welcome! Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("Bot: Goodbye, have a great day!")
            break
        
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
