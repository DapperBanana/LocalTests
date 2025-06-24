
def is_palindrome(s):
    s = s.lower()  # convert the string to lowercase
    s = ''.join(e for e in s if e.isalnum())  # remove non-alphanumeric characters

    return s == s[::-1]

# Test the program
s = "A man, a plan, a canal, Panama"
if is_palindrome(s):
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")
