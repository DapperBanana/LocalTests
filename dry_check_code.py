
def is_palindrome(sentence):
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    return clean_sentence == clean_sentence[::-1]

user_input = input("Enter a sentence: ")
if is_palindrome(user_input):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
