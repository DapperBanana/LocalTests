
def is_palindrome(s):
    # Remove all non-alphanumeric characters from the string and convert it to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get the input string from the user
input_str = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")
