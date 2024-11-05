
def is_valid_credit_card(card_number):
    # Remove any spaces or dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")
    
    if not card_number.isdigit():
        return False
    
    if len(card_number) != 16:
        return False
    
    # Perform Luhn's algorithm to validate the credit card number
    total = 0
    for i in range(16):
        digit = int(card_number[15 - i])
        if i % 2 == 0:
            total += digit
        else:
            total += (2 * digit) % 10 + (2 * digit) // 10
    
    return total % 10 == 0

# Test the program with some example credit card numbers
credit_card_numbers = [
    "4111-1111-1111-1111",
    "6011-1111-1111-1117",
    "1234-5678-9012-3456",
    "5313-1313-1313-1316"
]

for card_number in credit_card_numbers:
    if is_valid_credit_card(card_number):
        print(f"{card_number} is a valid credit card number")
    else:
        print(f"{card_number} is not a valid credit card number")
