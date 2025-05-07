
def check_isbn(isbn):
    isbn = isbn.replace('-', '')  # remove any dashes
    if len(isbn) != 10:
        return False

    # Check if the first 9 characters are digits
    if not isbn[:-1].isdigit():
        return False

    # Check if the last character is a digit or 'X'
    if not isbn[-1].isdigit() and isbn[-1] != 'X':
        return False

    # Calculate the check digit
    check_sum = sum(int(isbn[i]) * (i + 1) for i in range(9))
    check_digit = check_sum % 11

    if isbn[-1] == 'X':
        return check_digit == 10
    else:
        return check_digit == int(isbn[-1])

# Test the function
isbn = input("Enter an ISBN number: ")
if check_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
