
def is_valid_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the cleaned sentence is a palindrome
    return cleaned_sentence == cleaned_sentence[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama"
if is_valid_palindrome(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
