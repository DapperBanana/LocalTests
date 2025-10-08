
def is_valid_credit_card(card_number):
    card_number = card_number.replace(' ', '')  # Remove any spaces in the card number
    if not card_number.isdigit():  # Check if the card number contains only digits
        return False

    if len(card_number) != 16:  # Check if the card number is of length 16
        return False

    total = 0
    for i in range(0, len(card_number)):
        digit = int(card_number[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    if total % 10 == 0:  # Check if the total sum is divisible by 10
        return True
    else:
        return False

# Test the function with some examples
print(is_valid_credit_card("4539 1488 0343 6467"))  # True
print(is_valid_credit_card("4539148803436467"))  # True
print(is_valid_credit_card("4532 5601 3071 4523"))  # False
print(is_valid_credit_card("4532156130714523"))  # False
