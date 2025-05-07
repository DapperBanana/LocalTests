
def is_valid_credit_card(number):
    number = number.replace(" ", "")  # Remove any spaces
    if not number.isdigit():
        return False

    total = 0
    length = len(number)
    parity = length % 2

    for i in range(length):
        digit = int(number[i])
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


credit_card_number = input("Enter a credit card number: ")
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
