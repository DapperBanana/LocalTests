
def is_palindrome(s):
    s = s.lower() # convert the string to lowercase
    s = ''.join(e for e in s if e.isalnum()) # remove non-alphanumeric characters
    
    return s == s[::-1]

# Test the function
s1 = "A man, a plan, a canal, Panama"
s2 = "hello"
s3 = "racecar"

print(is_palindrome(s1)) # True
print(is_palindrome(s2)) # False
print(is_palindrome(s3)) # True
