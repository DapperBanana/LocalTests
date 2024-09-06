
def is_palindrome(number):
    original_number = number
    reverse_number = 0
    
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10
    
    if original_number == reverse_number:
        return True
    else:
        return False

number = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
