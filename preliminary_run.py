
def is_valid_credit_card(card_number):
    # Remove any spaces and dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if the card number is 16 digits long and consists only of digits
    if len(card_number) != 16 or not card_number.isdigit():
        return False
    
    # Use Luhn algorithm to validate the credit card number
    total = 0
    for i in range(0, 16):
        digit = int(card_number[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    if total % 10 == 0:
        return True
    else:
        return False

# Test the function
card_number = "4539 1488 0343 6467"
if is_valid_credit_card(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
