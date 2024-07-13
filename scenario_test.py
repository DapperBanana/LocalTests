
def chat(question):
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a simple program, but thanks for asking!",
        "what's your name": "I'm a chatbot program created by [Your Name].",
        "goodbye": "Goodbye! Have a great day!",
    }
    
    question = question.lower()
    
    if question in responses:
        return responses[question]
    else:
        return "I'm sorry, I don't understand that question. Please try asking something else."

print("Welcome to the Chatbot program!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        response = chat(user_input)
        print("Chatbot:", response)
