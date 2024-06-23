
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # convert the string to lowercase and remove whitespaces
    return s == s[::-1]  # check if the reversed string is equal to the original string

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
