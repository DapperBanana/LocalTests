
def is_valid_credit_card(number):
    # Remove any spaces or dashes in the input
    number = number.replace(" ", "")
    number = number.replace("-", "")
    
    # Check if the length of the input is valid for a credit card number
    if len(number) != 16:
        return False
    
    # Check if all characters in the input are digits
    if not number.isdigit():
        return False
    
    # Check if the credit card number passes the Luhn algorithm
    total = 0
    is_second_digit = False
    for digit in reversed(number):
        digit = int(digit)
        if is_second_digit:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        is_second_digit = not is_second_digit
    
    if total % 10 == 0:
        return True
    else:
        return False

# Test the function with some sample credit card numbers
print(is_valid_credit_card("4539562436897327"))  # True
print(is_valid_credit_card("4539-5624-3689-7327"))  # True
print(is_valid_credit_card("4539562436897328"))  # False
print(is_valid_credit_card("abcdefgh123456789"))  # False
