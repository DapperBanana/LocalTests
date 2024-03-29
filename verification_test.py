
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove any hyphens from the input
    
    # Check if the length of the ISBN is correct
    if len(isbn) != 10:
        return False
    
    # Calculate the check digit
    check_digit = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        check_digit += int(isbn[i]) * (i + 1)
    
    check_digit %= 11
    if check_digit == 10:
        check_digit = 'X'
    else:
        check_digit = str(check_digit)
    
    # Check if the last digit matches the calculated check digit
    if isbn[-1] != check_digit:
        return False
    
    return True

# Test the function with some examples
print(is_valid_isbn('3-598-21507-X'))  # True
print(is_valid_isbn('3-598-21507-9'))  # False
print(is_valid_isbn('123456789X'))  # False
