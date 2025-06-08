
import random

def get_response(user_input):
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a computer program, but I'm here to assist you.",
        "what's your name": "I'm a chatbot, feel free to give me a name!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Let me know if you need anything else."
    }
    
    response = responses.get(user_input.lower(), "I'm not sure how to respond to that.")
    return response

print("Welcome to the chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
