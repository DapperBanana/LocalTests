
def is_valid_palindrome_sentence(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())

    # Check if the cleaned sentence is a palindrome
    return cleaned_sentence == cleaned_sentence[::-1]

# Test the program
sentence1 = "A man, a plan, a canal, Panama!"
print(is_valid_palindrome_sentence(sentence1))  # Output: True

sentence2 = "Hello, world!"
print(is_valid_palindrome_sentence(sentence2))  # Output: False
