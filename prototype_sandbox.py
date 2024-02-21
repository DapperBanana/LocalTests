
def chatbot():
    print("Hello! I am a text-based chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I don't know how to respond to that.")
            
if __name__ == "__main__":
    chatbot()
