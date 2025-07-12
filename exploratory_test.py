
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove any hyphens
    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit() or not (isbn[-1].isdigit() or isbn[-1].lower() == 'x'):
        return False

    checksum = 0
    for i in range(9):
        checksum += int(isbn[i]) * (i + 1)
    if isbn[-1] == 'X':
        checksum += 10 * 10
    else:
        checksum += int(isbn[-1]) * 10

    return checksum % 11 == 0

# Test the function
isbn = input("Enter ISBN number: ")
if is_valid_isbn(isbn):
    print("Valid ISBN number")
else:
    print("Invalid ISBN number")
