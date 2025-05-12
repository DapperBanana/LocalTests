
def is_palindrome(s):
    s = s.lower()  # convert to lowercase for case-insensitive comparison
    s = ''.join(ch for ch in s if ch.isalnum())  # remove non-alphanumeric characters
    
    return s == s[::-1]  # check if the string is equal to its reverse
    
# Test the function
input_str = "A man, a plan, a canal - Panama!"
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
