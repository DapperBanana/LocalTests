
def is_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
