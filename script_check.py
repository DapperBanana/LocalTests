
def chatbot():
    print("Hello! I am your chatbot. What can I help you with today?")
    
    while True:
        user_input = input("You: ")
        
        if "hello" in user_input.lower():
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a computer program, I don't have feelings, but thanks for asking!")
        elif "goodbye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase that?")
            
chatbot()
