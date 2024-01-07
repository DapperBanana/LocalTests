
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Reverse the string
    reverse_s = s[::-1]
    # Check if the original string is equal to its reverse
    if s == reverse_s:
        return True
    else:
        return False

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
