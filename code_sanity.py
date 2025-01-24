
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Test the function with a sample number
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
