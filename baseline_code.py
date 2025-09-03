
def is_valid_credit_card_number(card_number):
    card_number = card_number.replace(' ', '')  # remove any spaces
    if not card_number.isdigit():
        return False
    
    if len(card_number) != 16:
        return False
    
    total = 0
    for i, digit in enumerate(card_number):
        if i % 2 == 0:
            double_digit = int(digit) * 2
            if double_digit > 9:
                double_digit = double_digit - 9
            total += double_digit
        else:
            total += int(digit)
    
    return total % 10 == 0

# Test the program
card_number = "4539 1488 0343 6467"
if is_valid_credit_card_number(card_number):
    print(f"{card_number} is a valid credit card number.")
else:
    print(f"{card_number} is not a valid credit card number.")
