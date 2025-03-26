
import random

# List of greetings
greetings = ['hi', 'hello', 'hey', 'hi there']

# List of responses
responses = ['Hello!', 'Hi there!', 'Hey!', 'Nice to meet you!']

# Function to respond to user input
def respond(input):
    if input.lower() in greetings:
        return random.choice(responses)
    else:
        return "I'm just a basic chatbot. Feel free to say hi or ask me anything!"

# Main program loop
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Chatbot:", response)
