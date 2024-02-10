
def is_palindrome(s):
    # Remove spaces and convert string to lowercase
    s = s.replace(" ", "").lower()

    # Reverse the string
    reversed_string = s[::-1]

    # Check if the original and reversed strings are the same
    if s == reversed_string:
        return True
    else:
        return False

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
