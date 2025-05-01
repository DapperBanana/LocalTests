
def is_palindrome(s):
    s = s.strip().lower()  # Remove leading and trailing whitespaces and convert to lowercase
    reversed_s = s[::-1]   # Reverse the string

    return s == reversed_s  # Check if the original string is the same as the reversed string

# Test the function
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
