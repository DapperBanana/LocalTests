
def chatbot():
    print("Hello! I am a chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day.")
            break
        
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            print("Chatbot: Hello there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a computer program, so I don't have feelings, but thanks for asking!")
        elif "weather" in user_input.lower():
            print("Chatbot: I'm not sure about the weather. You can check online or on your phone.")
        elif "joke" in user_input.lower():
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")
            
chatbot()
