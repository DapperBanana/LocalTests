
def is_valid_credit_card(card_number):
    card_number = card_number.replace(' ', '')  # Remove any spaces from the card number
  
    if not card_number.isdigit():
        return False
  
    if not 13 <= len(card_number) <= 16:
        return False
  
    total = 0
    for i in range(len(card_number) - 1, -1, -1):
        digit = int(card_number[i])
        if (len(card_number) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

# Test the function
card_number = "4539 1488 0343 6467"
if is_valid_credit_card(card_number):
    print(f"{card_number} is a valid credit card number.")
else:
    print(f"{card_number} is not a valid credit card number.")
