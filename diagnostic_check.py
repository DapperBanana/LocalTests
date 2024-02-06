
def is_valid_isbn(isbn):
    # Remove any hyphens or spaces from the ISBN string
    isbn = isbn.replace('-', '').replace(' ', '')

    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit():
        return False

    check_digit = isbn[-1]
    if check_digit.isdigit():
        check_digit = int(check_digit)
    else:
        check_digit = 10 if check_digit == 'X' else -1

    # Calculate the weighted sum of the digits
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(isbn[:-1], range(10, 0, -1)))

    return (weighted_sum + check_digit) % 11 == 0


isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print("Valid ISBN")
else:
    print("Invalid ISBN")
