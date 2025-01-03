
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '').replace(' ', '')  # Remove any dashes or spaces
    if len(isbn) != 10:  # Check if ISBN has 10 characters
        return False
    if not isbn[:-1].isdigit():  # Check if first 9 characters are digits
        return False
    last_digit = isbn[-1]
    if not (last_digit.isdigit() or last_digit.lower() == 'x'):  # Check if last digit is a digit or 'x'
        return False

    # Calculate the check digit
    check_sum = sum((i + 1) * int(char) for i, char in enumerate(isbn[:-1]))
    if last_digit.isdigit():
        check_digit = int(last_digit)
    else:
        check_digit = 10

    return check_sum % 11 == check_digit


# Test the function with some examples
isbn1 = '3-598-21507-X'
print(is_valid_isbn(isbn1))  # True

isbn2 = '3-598-21508-A'
print(is_valid_isbn(isbn2))  # False
