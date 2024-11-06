
def is_valid_isbn(isbn):
    # Remove any hyphens or spaces from the input string
    isbn = isbn.replace('-', '').replace(' ', '')
    
    # Check if the string is a valid ISBN-10 number
    if len(isbn) != 10:
        return False
    if not isbn[:-1].isdigit():
        return False
    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False  
    
    # Calculate the checksum
    checksum = 0
    for i in range(9):
        checksum += int(isbn[i]) * (i + 1)
    if isbn[9] == 'X':
        checksum += 10
    else:
        checksum += int(isbn[9])
    
    return checksum % 11 == 0

# Test the function
isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
