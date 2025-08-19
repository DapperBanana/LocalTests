
def is_palindrome(sentence):
    # Remove spaces and punctuation from the sentence and convert it to lowercase
    clean_sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    
    # Check if the reversed clean sentence is equal to the clean sentence
    return clean_sentence == clean_sentence[::-1]

# Test the function with some examples
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("Hello world"))  # Output: False
print(is_palindrome("racecar"))  # Output: True
