
import random

# Define possible responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

print("Welcome to the chatbot!")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    response = responses.get(user_input, ["I'm sorry, I don't understand that."])
    print("Chatbot:", random.choice(response))
