
def is_valid_credit_card(cc_number):
    cc_number = cc_number.replace(" ", "")  # Remove any spaces from the credit card number
    
    if not cc_number.isdigit():
        return False

    if len(cc_number) != 16:
        return False

    total = 0
    for i, digit in enumerate(cc_number[::-1]):
        if i % 2 == 0:
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:
                total += doubled_digit - 9
            else:
                total += doubled_digit
        else:
            total += int(digit)

    return total % 10 == 0


# Test the function
credit_card_number = "1234 5678 9012 3456"
if is_valid_credit_card(credit_card_number):
    print(f"{credit_card_number} is a valid credit card number.")
else:
    print(f"{credit_card_number} is not a valid credit card number.")
