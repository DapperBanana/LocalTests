
def is_valid_ISBN(isbn):
    # Remove any dashes or spaces from the input string
    isbn = isbn.replace("-", "").replace(" ", "")
    
    # Check if the string is of length 10 or 13
    if len(isbn) != 10 and len(isbn) != 13:
        return False
    
    # Check if the string contains only digits and 'X' (for the last digit of a 10-digit ISBN)
    if not isbn[:-1].isdigit() or not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False

    # Calculate the check digit for a 10-digit ISBN
    if len(isbn) == 10:
        check_sum = sum(int(isbn[i]) * (i + 1) for i in range(9))
        check_digit = check_sum % 11
        if isbn[-1] == 'X':
            check_digit = 10
        
        return check_digit == int(isbn[-1])
    
    # Calculate the check digit for a 13-digit ISBN
    if len(isbn) == 13:
        check_sum = sum(int(isbn[i]) * (3 if i % 2 == 0 else 1) for i in range(12))
        check_digit = (10 - (check_sum % 10)) % 10

        return check_digit == int(isbn[-1])

# Test the function
isbn = "3-598-21508-8"
print(is_valid_ISBN(isbn))  # Should return True

isbn = "3-598-21508-9"
print(is_valid_ISBN(isbn))  # Should return False

isbn = "978-3-16-148410-0"
print(is_valid_ISBN(isbn))  # Should return True
