
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lower case and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
