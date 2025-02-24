
import random

def chatbot():
    # Greetings
    greetings = ["Hello!", "Hi there!", "Hey, how are you?"]
    print(random.choice(greetings))
    
    # Conversation
    while True:
        user_input = input("You: ")
        response = ""
        
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            response = "Hello! How can I help you?"
        elif "how are you" in user_input.lower():
            response = "I'm just a computer program, so I'm always good!"
        elif "bye" in user_input.lower() or "exit" in user_input.lower():
            response = "Goodbye! Have a great day!"
            break
        else:
            response = "I'm sorry, I didn't understand that. Can you be more specific?"
        
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
