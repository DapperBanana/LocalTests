
def is_valid_credit_card(number):
    # Step 1: Reverse the credit card number
    reversed_number = number[::-1]
    
    # Step 2: Starting from the second digit, double every other digit
    doubled_digits = []
    for i in range(1, len(reversed_number), 2):
        doubled = int(reversed_number[i]) * 2
        
        # If the doubled digit is greater than 9, subtract 9 from it
        if doubled > 9:
            doubled -= 9
        
        doubled_digits.append(doubled)
    
    # Step 3: Add all the digits together
    total = sum(doubled_digits) + sum(int(i) for i in reversed_number[::2])
    
    # Step 4: If the total is divisible by 10, it's a valid credit card number
    if total % 10 == 0:
        return True
    else:
        return False

# Testing the function
credit_card_number = input("Enter a credit card number: ")
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
