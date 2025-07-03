
# Define a dictionary of possible responses
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a computer program, so I don't have feelings, but thanks for asking!",
    "goodbye": "Goodbye! Have a great day!",
    "what is your name": "I'm just a simple chatbot. What can I do for you?",
    "thanks": "You're welcome! Is there anything else I can assist you with?"
}

def chatbot():
    print("Welcome to the basic text-based chatbot. Start chatting with me!")
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "quit":
            print("Goodbye! Have a great day!")
            break
        
        response = responses.get(user_input, "I'm sorry, I don't understand. Can you try asking a different question?")
        print("Chatbot:", response)

chatbot()
