
def is_palindrome(num):
    original_num = num
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = reverse_num * 10 + remainder
        num = num // 10
    if original_num == reverse_num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
