
def is_valid_credit_card(number):
    # Remove any whitespace from the input
    number = number.replace(" ", "")

    # Check if the input is a digit and has 16 characters
    if (not number.isdigit()) or (len(number) != 16):
        return False

    # Check if the input passes the Luhn algorithm
    total = 0
    for i in range(0, 16):
        digit = int(number[i])
        if i % 2 == 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total = total + digit

    if total % 10 == 0:
        return True
    else:
        return False

# Test the function
input_number = input("Enter a credit card number: ")
if is_valid_credit_card(input_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
