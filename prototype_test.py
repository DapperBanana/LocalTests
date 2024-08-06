
def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    reversed_s = s[::-1]
    
    return s == reversed_s

# Test the function
if __name__ == "__main__":
    s = "A man, a plan, a canal, Panama!"
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
