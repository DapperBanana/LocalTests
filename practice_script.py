
def is_palindrome(s):
    s = s.lower()  # convert string to lowercase
    s = ''.join(c for c in s if c.isalnum())  # remove non-alphanumeric characters

    return s == s[::-1]  # check if the string is equal to its reverse

# Test the function
string = "A man, a plan, a canal, Panama!"
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
