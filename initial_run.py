
import random

# List of possible responses from the chatbot
responses = [
    "Hello, how can I help you?",
    "What's up? How can I assist you today?",
    "Greetings! How can I be of service?",
    "Hey there, what do you need help with?",
    "Hi, how can I assist you today?"
]

# Function to generate a random response from the list of possible responses
def get_response():
    return random.choice(responses)

# Main function to run the chatbot
def chatbot():
    print("Welcome to the chatbot!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        response = get_response()
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
