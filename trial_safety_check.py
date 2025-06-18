
def is_valid_credit_card(card_number):
    card_number = card_number.replace(' ', '')  # Remove any spaces in the card number
    if not card_number.isdigit():
        return False
    
    digits = list(map(int, card_number))
    checksum = sum(digits[-1::-2])
    for i in digits[-2::-2]:
        checksum += sum(divmod(i * 2, 10))
        
    return checksum % 10 == 0

# Test the function with some examples
print(is_valid_credit_card('4539 1488 0343 6467'))  # Should return True
print(is_valid_credit_card('4539 1488 0343 6466'))  # Should return False
