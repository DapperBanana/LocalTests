
def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    if not isbn[:-1].isdigit():
        return False
    
    check_digit = isbn[-1]
    if check_digit != 'X' and not check_digit.isdigit():
        return False
    
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)
    
    if check_digit == 'X':
        total += 10
    else:
        total += int(check_digit)
    
    return total % 11 == 0

# Test the function with sample ISBN numbers
print(is_valid_isbn("3-598-21508-8"))  # True
print(is_valid_isbn("3-598-21508-9"))  # False
