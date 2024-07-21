
def is_palindrome(s):
    # remove all non-alphanumeric characters and convert string to lowercase
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # check if the reversed string is equal to the original string
    return s == s[::-1]

# Test the function
string1 = "A man, a plan, a canal, Panama"
print(is_palindrome(string1))  # Output: True

string2 = "hello world"
print(is_palindrome(string2))  # Output: False
