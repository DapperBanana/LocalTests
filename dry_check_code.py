
def chatbot():
    print("Hello! I am a chatbot. Enter 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        if 'hello' in user_input.lower():
            print("Chatbot: Hello! How are you?")
        elif 'how are you' in user_input.lower():
            print("Chatbot: I'm just a computer program, but thanks for asking!")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you try rephrasing?")
    
chatbot()
