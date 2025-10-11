
def validate_credit_card_number(card_number):
    card_number = card_number.replace(" ", "")
    
    if not card_number.isdigit():
        return False
    
    if len(card_number) != 16:
        return False
    
    total = 0
    for i, digit in enumerate(card_number):
        digit = int(digit)
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    return total % 10 == 0

# Test the program
card_number = "1234 5678 9012 3456"
if validate_credit_card_number(card_number):
    print("The card number is valid.")
else:
    print("The card number is invalid.")
