
def is_palindrome_sentence(sentence):
    sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    
    return sentence == sentence[::-1]

# Test the function with some example strings
print(is_palindrome_sentence("A man, a plan, a canal: Panama")) # True
print(is_palindrome_sentence("Racecar")) # True
print(is_palindrome_sentence("Hello, world!")) # False
print(is_palindrome_sentence("Was it a car or a cat I saw?")) # True
