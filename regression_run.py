
import random

# Define some responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?", "Pretty good, how about you?"],
    "what's your name": ["I'm just a simple chatbot", "I'm a chatbot, you can call me whatever you like", "I'm Chatbot, pleased to meet you!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
}

def chatbot():
    print("Welcome to the chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print(random.choice(responses["bye"]))
            break
        
        if user_input in responses:
            print("Chatbot:", random.choice(responses[user_input]))
        else:
            print("Chatbot: I'm not sure how to respond to that.")
        

if __name__ == "__main__":
    chatbot()
