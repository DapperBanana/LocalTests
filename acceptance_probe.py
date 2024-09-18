
def is_palindrome_sentence(s):
    s = ''.join(char.lower() for char in s if char.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse

# Test the function
sentence = "A man, a plan, a canal, Panama"
if is_palindrome_sentence(sentence):
    print("The given string is a valid palindrome sentence.")
else:
    print("The given string is not a valid palindrome sentence.")
