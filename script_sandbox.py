
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '').replace(' ', '')
    
    if len(isbn) != 10:
        return False
        
    total = 0
    for i, digit in enumerate(isbn):
        if i == 9 and digit == 'X':
            digit = 10
        if not digit.isdigit():
            return False
        total += int(digit) * (10 - i)
        
    return total % 11 == 0

isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
