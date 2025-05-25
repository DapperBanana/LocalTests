
def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "") 
    if not card_number.isdigit(): 
        return False
    
    if len(card_number) != 16:
        return False
    
    total_sum = 0
    for i in range(0, 16):
        if i % 2 == 0:
            digit = int(card_number[i]) * 2
            if digit > 9:
                digit = digit - 9
            total_sum += digit
        else:
            total_sum += int(card_number[i])
    
    return total_sum % 10 == 0

# Test the program
card_number = "4539 1488 0343 6467"
if is_valid_credit_card(card_number):
    print("The card number is valid")
else:
    print("The card number is invalid")
