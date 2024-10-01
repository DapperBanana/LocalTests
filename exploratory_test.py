
def is_palindrome_sentence(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


# Test the program
input_string = "A man, a plan, a canal, Panama"
if is_palindrome_sentence(input_string):
    print("The string is a valid palindrome sentence.")
else:
    print("The string is not a valid palindrome sentence.")
