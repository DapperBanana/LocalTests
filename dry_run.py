
# Function to get user input and respond
def chatbot():
    print("Hello! I am a basic chatbot. How can I help you today?")
    
    while True:
        user_input = input("User: ")
        
        if "hello" in user_input.lower():
            print("Chatbot: Hello, how are you?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I am just a computer program, so I don't have feelings. But thanks for asking!")
        elif "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase that?")
            
if __name__ == "__main__":
    chatbot()
