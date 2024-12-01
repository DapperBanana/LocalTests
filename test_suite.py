
def is_valid_palindrome(s):
    # Remove all non-alphanumeric characters and convert the string to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the string is a palindrome
    return s == s[::-1]

# Input string from user
input_string = input("Enter a string: ")

if is_valid_palindrome(input_string):
    print("The given string is a valid palindrome sentence.")
else:
    print("The given string is not a valid palindrome sentence.")
