
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert string to lowercase and remove spaces
    return s == s[::-1]  # Check if the reversed string is equal to the original string

# Test the function
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
