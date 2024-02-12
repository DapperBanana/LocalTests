
def is_valid_isbn(isbn):
    # Remove any hyphens from the string
    isbn = isbn.replace("-", "")

    # Check if the length of the string is valid
    if len(isbn) != 10:
        return False

    # Check if the first 9 characters are digits
    if not isbn[:-1].isdigit():
        return False

    # Check if the last character is a digit or 'X'
    if not (isbn[-1].isdigit() or isbn[-1].upper() == 'X'):
        return False

    # Calculate the checksum
    checksum = sum(int(isbn[i]) * (10 - i) for i in range(9))
    checksum += (10 if isbn[-1].upper() == 'X' else int(isbn[-1]))

    # Check if the checksum is divisible by 11
    if checksum % 11 != 0:
        return False

    return True

# Prompt the user for an ISBN number
isbn_number = input("Enter an ISBN number: ")

# Check if the entered ISBN number is valid and print the result
if is_valid_isbn(isbn_number):
    print("Valid ISBN number")
else:
    print("Invalid ISBN number")
