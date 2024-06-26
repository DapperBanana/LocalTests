
def is_palindrome(s):
    s = s.lower()  # convert the input string to lowercase
    s = ''.join(e for e in s if e.isalnum())  # remove non-alphanumeric characters

    return s == s[::-1]  # check if the string is equal to its reverse

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
