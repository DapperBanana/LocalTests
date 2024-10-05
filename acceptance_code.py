
def is_palindrome_sentence(sentence):
    # Remove all non-alphanumeric characters from the string
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())

    # Check if the clean sentence is a palindrome
    if clean_sentence == clean_sentence[::-1]:
        return True
    else:
        return False

# Test the function with some examples
example1 = "A man, a plan, a canal, Panama"
example2 = "Racecar"
example3 = "Hello World"
example4 = "Was it a car or a cat I saw?"
example5 = "No 'x' in Nixon"

print(is_palindrome_sentence(example1))  # True
print(is_palindrome_sentence(example2))  # True
print(is_palindrome_sentence(example3))  # False
print(is_palindrome_sentence(example4))  # True
print(is_palindrome_sentence(example5))  # True
