
def is_palindrome(num):
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    
    if num_str == reversed_num_str:
        return True
    else:
        return False

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
