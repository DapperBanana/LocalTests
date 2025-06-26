
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# Get user input
user_input = input("Enter a string: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
