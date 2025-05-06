
def is_valid_isbn(isbn):
    # Remove any hyphens from the input string
    isbn = isbn.replace("-", "")

    # Check if the ISBN is exactly 10 characters long
    if len(isbn) != 10:
        return False

    # Check if the first 9 characters are digits
    if not isbn[:-1].isdigit():
        return False

    # Check if the last character is a digit or 'X'
    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False

    # Calculate the ISBN checksum
    checksum = 0
    for i in range(9):
        checksum += (i + 1) * int(isbn[i])
    if isbn[-1] == 'X':
        checksum += 10
    else:
        checksum += int(isbn[-1])

    # Check if the checksum is divisible by 11
    if checksum % 11 == 0:
        return True
    else:
        return False

# Test the function with some sample ISBN numbers
print(is_valid_isbn("0-306-40615-2"))  # True
print(is_valid_isbn("0-306-40615-5"))  # False
print(is_valid_isbn("3-540-21191-X"))  # True
print(is_valid_isbn("3-540-21191-8"))  # False
