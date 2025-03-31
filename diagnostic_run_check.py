
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # Remove any spaces in the string
    
    if not card_number.isdigit():
        return False
    
    if len(card_number) < 13 or len(card_number) > 16:
        return False
    
    total = 0
    digits = list(map(int, card_number))
    length = len(digits)
    for i in range(length):
        digit = digits[length - i - 1]
        if i % 2 == 0:
            total += digit
        else:
            double_digit = digit * 2
            if double_digit > 9:
                total += double_digit - 9
            else:
                total += double_digit
                
    if total % 10 == 0:
        return True
    else:
        return False

# Test the function
card_number = "4556 7378 3289 7612"
if is_valid_credit_card(card_number):
    print("The credit card number is valid")
else:
    print("The credit card number is not valid")
