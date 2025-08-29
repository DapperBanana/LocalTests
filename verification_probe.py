
def is_palindrome_sentence(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1] # Check if the string is equal to its reverse

# Test the function
sentence = input("Enter a sentence: ")
if is_palindrome_sentence(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
