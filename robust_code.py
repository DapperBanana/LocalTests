
def chatbot():
    print("Hello! I am a text-based chatbot. Let's chat!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello":
            print("Chatbot: Hello there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a program, so I don't have feelings. But thank you for asking!")
        elif "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure what you're trying to say. Can you be more specific?")
            
chatbot()
