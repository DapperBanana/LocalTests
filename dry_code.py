
def is_valid_credit_card(number):
    # Remove any white spaces from the card number
    number = number.replace(" ", "")
    
    # Check if the card number contains only digits
    if not number.isdigit():
        return False
    
    # Check if the card number has a valid length
    if len(number) != 16:
        return False
    
    # Check the card number using Luhn algorithm
    digits = [int(x) for x in number]
    checksum = sum(digits[::-2] + [sum(divmod(d*2, 10)) for d in digits[-2::-2]])
    return checksum % 10 == 0


# Test the program
card_number = input("Enter a credit card number: ")
if is_valid_credit_card(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
