
def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase
    s = ''.join(e for e in s if e.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if string is equal to its reverse

# Test the function
input_string = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
