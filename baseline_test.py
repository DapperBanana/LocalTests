
def is_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the clean sentence is equal to its reverse
    return clean_sentence == clean_sentence[::-1]

# Get user input
sentence = input("Enter a sentence to check if it is a palindrome: ")

# Check if the sentence is a palindrome
if is_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
