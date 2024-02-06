
def is_valid_credit_card(number):
    # Reverse the credit card number and convert it into a list of integers
    digits = list(map(int, str(number)[::-1]))

    # Apply the Luhn algorithm
    odd_sum = sum(digits[0::2])
    even_sum = sum(sum(divmod(i * 2, 10)) for i in digits[1::2])

    return (odd_sum + even_sum) % 10 == 0

# Test the program
credit_card_number = input("Enter a credit card number: ")

if is_valid_credit_card(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
