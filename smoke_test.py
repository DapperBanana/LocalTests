
def is_palindrome(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
