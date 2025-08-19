
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # remove spaces from the card number
    if not card_number.isdigit():
        return False
    
    if len(card_number) < 13 or len(card_number) > 16:
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
card_number = "4556 7375 8797 5655"
if is_valid_credit_card(card_number):
    print(f"{card_number} is a valid credit card number.")
else:
    print(f"{card_number} is not a valid credit card number.")
