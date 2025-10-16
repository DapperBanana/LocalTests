
def is_valid_credit_card(number):
    number = number.replace(" ", "")  # Remove spaces from the input string
    if len(number) != 16:
        return False
    
    total = 0
    for i in range(16):
        digit = int(number[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    return total % 10 == 0

# Test cases
credit_card_number = "4539 1488 0343 6467"
if is_valid_credit_card(credit_card_number):
    print(f"{credit_card_number} is a valid credit card number")
else:
    print(f"{credit_card_number} is not a valid credit card number")
