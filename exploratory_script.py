
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # remove any spaces in the card number
    
    if not card_number.isdigit() or len(card_number) != 16:
        return False
    
    total = 0
    for i in range(16):
        digit = int(card_number[i])
        if i % 2 == 0:  # Double every other digit
            digit *= 2
            if digit > 9:  # If doubling results in a two-digit number, add the two digits together
                digit = digit // 10 + digit % 10
        total += digit
    
    return total % 10 == 0

# Test the function
card_number = input("Enter credit card number: ")
if is_valid_credit_card(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
