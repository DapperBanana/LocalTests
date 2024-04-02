
import random

# list of possible user inputs
greetings = ['hello', 'hi', 'hey', 'yo', 'hi there', 'howdy']
goodbyes = ['goodbye', 'bye', 'see ya', 'adios', 'bye bye']
questions = ['how are you?', 'what is your name?', 'what can you do?', 'tell me a joke']

# list of possible chatbot responses
hello_responses = ['Hello!', 'Hi there!', 'Hey!', 'Yo!', 'Howdy!']
goodbye_responses = ['Goodbye!', 'Bye!', 'See you later!', 'Adios!', 'Bye bye!']
questions_responses = ['I am a chatbot.', 'My name is Chatbot.', 'I can chat with you and tell jokes.', 'Why was six afraid of seven? Because seven eight (ate) nine!']

def chatbot():
    print("Welcome to the chatbot!")
    
    while True:
        user_input = input("You: ").lower()  # convert user input to lowercase
        
        if user_input in greetings:
            print(random.choice(hello_responses))
        elif user_input in goodbyes:
            print(random.choice(goodbye_responses))
            break
        elif user_input in questions:
            print(random.choice(questions_responses))
        else:
            print("I'm sorry, I don't understand that.")
            
if __name__ == '__main__':
    chatbot()
