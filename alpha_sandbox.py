
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove any dashes from the input string
    if len(isbn) != 10:  # ISBN-10 numbers have 10 digits
        return False

    if not isbn[:-1].isdigit():  # Check if the first 9 characters are digits
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):  # Check if the last character is a digit or 'X'
        return False

    product = 0
    for i in range(9):
        product += int(isbn[i]) * (i + 1)

    if isbn[-1] == 'X':  # Check for 'X' at the end
        product += 10
    else:
        product += int(isbn[-1])

    return product % 11 == 0  # Check if the sum is divisible by 11


# Test the function
isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
