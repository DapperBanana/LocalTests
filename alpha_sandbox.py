
def is_palindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The input string is a valid palindrome sentence.")
else:
    print("The input string is not a palindrome sentence.")
