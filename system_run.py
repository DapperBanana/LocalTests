
def is_palindrome(num):
    num_str = str(num)
    reverse_num_str = num_str[::-1]
    
    if num_str == reverse_num_str:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
