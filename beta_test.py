
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # Remove spaces from the card number
    
    if not card_number.isdigit():  # Check if the card number contains only digits
        return False
    
    if len(card_number) != 16:  # Check if the card number is of the correct length
        return False
    
    total_sum = 0
    for i in range(0, 16):
        digit = int(card_number[i])
        if i % 2 == 0:  # Double every other digit
            digit *= 2
            if digit > 9:  # If the doubled digit is greater than 9, subtract 9 from it
                digit -= 9
        total_sum += digit
    
    if total_sum % 10 == 0:  # Check if the total sum is divisible by 10
        return True
    else:
        return False

# Test the function with a sample credit card number
card_number = "4556 7376 1860 1327"
if is_valid_credit_card(card_number):
    print(f"{card_number} is a valid credit card number.")
else:
    print(f"{card_number} is not a valid credit card number.")
