
def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False

    checksum = 0

    for i in range(0, 9):
        if not isbn[i].isdigit():
            return False
        checksum += int(isbn[i]) * (10 - i)

    if isbn[9].isdigit():
        checksum += int(isbn[9]) if isbn[9] != 'X' else 10
    else:
        return False

    return checksum % 11 == 0


# Test the function with some sample ISBN numbers
print(is_valid_isbn("3-598-21507-X"))  # True
print(is_valid_isbn("99-9999-999-9"))  # False
print(is_valid_isbn("3-598-21508-X"))  # False
print(is_valid_isbn("359821507X"))  # True
