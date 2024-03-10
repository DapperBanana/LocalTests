
def is_palindrome_sentence(sentence):
    sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    return sentence == sentence[::-1]

# Get user input
user_input = input("Enter a sentence to check if it is a palindrome: ")

if is_palindrome_sentence(user_input):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a palindrome.")
