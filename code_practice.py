
import random

def get_response(input_text):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm just a computer program, I don't have feelings.",
        "what's your name": "I'm a chatbot, you can call me Bot.",
        "bye": "Goodbye!",
        "default": "I'm sorry, I don't understand. Can you ask me something else?"
    }
    
    input_text = input_text.lower()
    
    if input_text in responses:
        return responses[input_text]
    else:
        return responses['default']

print("Welcome to the Chatbot! Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        response = get_response(user_input)
        print("Bot:", response)
