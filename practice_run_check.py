
def is_valid_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert the sentence to lowercase
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the clean sentence is a palindrome
    return clean_sentence == clean_sentence[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama!"
if is_valid_palindrome(sentence):
    print("The given string is a valid palindrome sentence.")
else:
    print("The given string is not a valid palindrome sentence.")
