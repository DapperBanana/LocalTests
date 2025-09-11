
def is_valid_credit_card(number):
    # Remove any spaces or dashes from the input
    number = number.replace(' ', '').replace('-', '')
    
    if not number.isdigit():
        return False
    
    if len(number) < 13 or len(number) > 16:
        return False
    
    total = 0
    length = len(number)
    
    for i in range(length):
        digit = int(number[length - i - 1])
        
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        total += digit
    
    return total % 10 == 0

# Test the function
card_number = input("Enter a credit card number: ")
if is_valid_credit_card(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
