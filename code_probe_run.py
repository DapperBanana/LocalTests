
def get_response(user_input):
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm a computer program, so I don't have feelings, but thank you for asking!",
        "what is your name": "I'm just a simple chatbot.",
        "bye": "Goodbye! Have a great day!"
    }
    
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm sorry, I don't understand. Can you please rephrase that?"

print("Welcome! I'm a simple chatbot. You can start chatting with me by typing your messages.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
    
    if user_input.lower() == "bye":
        break
