
import random

# List of responses for the chatbot
responses = ["Hello!", "How can I help you?", "Nice to meet you!", "How's your day going?", "What's on your mind?"]

# Function to generate response for user input
def chatbot_response(user_input):
    return random.choice(responses)

# Main function for the chatbot
def chatbot():
    print("Welcome to the chatbot. Type 'exit' to end the conversation.")
    
    # Loop to keep the conversation going until user exits
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Start the chatbot
chatbot()
