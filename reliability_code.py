
def chatbot():
    print("Hello! I'm a chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello":
            print("Chatbot: Hello there!")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm just a program, so I don't have feelings. But thanks for asking!")
        elif user_input.lower() == "goodbye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
            
if __name__ == "__main__":
    chatbot()
