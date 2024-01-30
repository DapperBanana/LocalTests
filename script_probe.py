
def is_valid_credit_card(number):
    # Remove any spaces from the input
    number = number.replace(' ', '')
    
    # Check if the input is a 16-digit number
    if not number.isdigit() or len(number) != 16:
        return False
    
    # Reverse the number and convert each digit to an integer
    digits = [int(digit) for digit in reversed(number)]
    
    # Apply the Luhn algorithm
    checksum = sum(digits[0::2]) + sum(sum(divmod(2 * digit, 10)) for digit in digits[1::2])
    
    # Check if the checksum is divisible by 10
    return checksum % 10 == 0

# Test the program
credit_card_number = input("Enter a credit card number: ")
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
