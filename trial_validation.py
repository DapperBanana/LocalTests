
# Basic Text-based Chatbot

def chatbot():
    print("Hello! I am your friendly chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello" or user_input.lower() == "hi":
            print("Chatbot: Hello! How are you today?")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm just a computer program, so I don't have feelings, but I'm here to help you!")
        elif user_input.lower() == "what is your name":
            print("Chatbot: My name is Chatbot. Nice to meet you!")
        elif user_input.lower() == "exit" or user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please repeat or ask something else?")

if __name__ == "__main__":
    chatbot()
