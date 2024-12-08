
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # Remove any spaces in the card number
    if not card_number.isdigit():
        return False

    if len(card_number) != 16:
        return False

    total = 0
    for index, digit in enumerate(card_number[::-1]):
        digit = int(digit)
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


# Example usage
card_number = "4539 1488 0343 6467"
if is_valid_credit_card(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
