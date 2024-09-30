
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    input_string = input_string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    if input_string == input_string[::-1]:
        return True
    else:
        return False

# Input string
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
