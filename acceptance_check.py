
def is_valid_palindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    return s == s[::-1]

# Test the function
input_string = "A man, a plan, a canal, Panama"
if is_valid_palindrome(input_string):
    print("The string is a valid palindrome sentence.")
else:
    print("The string is not a valid palindrome sentence.")
