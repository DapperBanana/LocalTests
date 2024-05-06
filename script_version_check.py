
# Simple text-based chatbot

def chat():
    print("Hello! I am a chatbot. You can type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

def get_response(user_input):
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, so I'm always good. How can I assist you?"
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

if __name__ == "__main__":
    chat()
