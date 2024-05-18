
def chatbot():
    print("Hello! I am a chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "how are you" in user_input.lower():
            print("Chatbot: I am just a computer program, so I do not have feelings, but thanks for asking!")
        elif "?" in user_input:
            print("Chatbot: I'm not sure how to respond to that question. Could you rephrase it?")
        else:
            print("Chatbot: That's interesting. Tell me more.")
            
chatbot()
