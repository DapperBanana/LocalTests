
def is_palindrome(num):
    num_str = str(num)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
