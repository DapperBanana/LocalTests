
# Define a function to simulate the chatbot
def chatbot():
    print("Hello! I am a basic chatbot. You can start chatting with me or type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break
        
        # Respond based on user input
        if 'hi' in user_input or 'hello' in user_input:
            print("Chatbot: Hi! How can I help you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a computer program, but I'm here to help.")
        elif 'what can you do' in user_input:
            print("Chatbot: I can answer simple questions and have basic conversations. Feel free to ask me anything.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")
    
# Start the chatbot program
chatbot()
