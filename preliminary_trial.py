
def is_palindrome_sentence(sentence):
    sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    return sentence == sentence[::-1]

# Get input from user
user_input = input("Enter a sentence: ")

if is_palindrome_sentence(user_input):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
