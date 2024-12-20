
# Define the responses from the chatbot
responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a computer program, so I don't have feelings. How can I assist you?",
    "what is your name": "I am a chatbot programmed to assist you. How can I help you today?",
    "bye": "Goodbye! Have a great day!",
}

# Function to simulate the chatbot
def chatbot():
    print("Hello! I am a chatbot. You can start chatting with me now.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in responses:
            print("Bot:", responses[user_input])
        elif user_input == "exit":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand. Please ask a different question.")
        
if __name__ == '__main__':
    chatbot()
