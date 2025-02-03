
def is_palindrome(input_str):
    # Remove all non-alphanumeric characters from the input string
    input_str = ''.join(e for e in input_str if e.isalnum()).lower()
    
    # Check if the input string is equal to its reverse
    if input_str == input_str[::-1]:
        return True
    else:
        return False

# Test the function
input_string = "A man, a plan, a canal: Panama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
