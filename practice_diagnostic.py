
def is_valid_palindrome(sentence):
    # Remove spaces and punctuation
    clean_sentence = ''.join(e for e in sentence if e.isalnum()).lower()
    
    # Check if the sentence is a palindrome
    return clean_sentence == clean_sentence[::-1]

# Test the program with a few examples
print(is_valid_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_valid_palindrome("Hello World"))  # Output: False
print(is_valid_palindrome("Was it a car or a cat I saw"))  # Output: True
