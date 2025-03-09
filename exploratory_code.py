
def is_valid_isbn(isbn):
    # Remove any hyphens or spaces from the string
    isbn = isbn.replace("-", "").replace(" ", "")

    # Check if the ISBN is 10 or 13 digits long
    if len(isbn) != 10 and len(isbn) != 13:
        return False

    # Calculate the checksum for a 10-digit ISBN
    if len(isbn) == 10:
        if not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
            return False
        checksum = sum((i+1) * int(digit) if digit.isdigit() else 10 for i, digit in enumerate(isbn[:-1])) % 11
        if (checksum == 10 and isbn[-1] == 'X') or checksum == int(isbn[-1]):
            return True
        else:
            return False

    # Calculate the checksum for a 13-digit ISBN
    if len(isbn) == 13:
        if not isbn.isdigit():
            return False
        checksum = sum((3 - i%2) * int(digit) for i, digit in enumerate(isbn[:-1])) % 10
        check_digit = (10 - checksum) % 10
        if check_digit == int(isbn[-1]):
            return True
        else:
            return False

# Test the function
isbn1 = "978-3-16-148410-0"
isbn2 = "3-16-148410-0"
isbn3 = "9783161484005"

print(is_valid_isbn(isbn1))  # True
print(is_valid_isbn(isbn2))  # True
print(is_valid_isbn(isbn3))  # False
