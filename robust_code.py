
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '').replace(' ', '')  # Remove dashes and spaces
    if len(isbn) != 10:
        return False
    
    # Calculate the checksum
    checksum = 0
    for i in range(10):
        if isbn[i] == 'X':
            checksum += 10
        elif isbn[i].isdigit():
            checksum += int(isbn[i]) * (10 - i)
        else:
            return False

    return checksum % 11 == 0


# Test the program
isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
