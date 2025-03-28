
def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase
    s = "".join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    
    return s == s[::-1]

# Test the function with some example strings
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True
