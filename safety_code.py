
def is_palindrome(string):
    # Convert the string to lowercase and remove any spaces or special characters
    cleaned_string = ''.join(e for e in string.lower() if e.isalnum())
    
    # Reverse the cleaned string
    reversed_string = cleaned_string[::-1]
    
    # Check if the reversed string is equal to the cleaned string
    if cleaned_string == reversed_string:
        return True
    else:
        return False

# Get the input string from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
