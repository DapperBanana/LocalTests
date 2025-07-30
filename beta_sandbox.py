
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove any hyphens
    if len(isbn) != 10:
        return False
    
    total = 0
    for i, char in enumerate(isbn):
        if i == 9 and char == 'X':
            digit = 10
        else:
            try:
                digit = int(char)
            except ValueError:
                return False
        total += (10 - i) * digit
    
    return total % 11 == 0


# Test the function
isbn = input("Enter an ISBN number to check: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
