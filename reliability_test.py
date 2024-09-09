
def chatbot():
    print("Hello! I am a chatbot.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand. Can you ask another question?")

if __name__ == "__main__":
    chatbot()
