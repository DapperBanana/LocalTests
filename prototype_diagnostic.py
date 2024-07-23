
# Chatbot program
print("Hello! I am a chatbot. What is your name?")
user_name = input()

print(f"Nice to meet you, {user_name}! How can I help you today?")

while True:
    user_input = input("You: ")

    if "hello" in user_input:
        print("Chatbot: Hello there! How can I help you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a computer program, so I'm always doing well. How can I assist you today?")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        print("Chatbot: I'm sorry, I don't understand. Can you please ask another question?")
