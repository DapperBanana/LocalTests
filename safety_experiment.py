
def chat():
    print("Hello! I am a basic chatbot. Let's have a conversation!")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello" or user_input.lower() == "hi":
            print("Chatbot: Hi there! How are you?")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm just a program, so I don't have feelings. But thanks for asking!")
        elif user_input.lower() == "what's your name" or user_input.lower() == "name":
            print("Chatbot: I'm just a basic chatbot. You can call me Chatbot.")
        elif user_input.lower() == "bye" or user_input.lower() == "exit" or user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")
        

if __name__ == "__main__":
    chat()
