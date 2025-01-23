
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(' ', '').lower()
    
    # Check if string is equal to its reverse
    return s == s[::-1]

# Test the function
s = "A man a plan a canal Panama"
if is_palindrome(s):
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")

s = "Hello World"
if is_palindrome(s):
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")
