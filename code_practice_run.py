
def validate_isbn(isbn):
    isbn = isbn.replace('-', '')
    
    if len(isbn) != 10:
        return False
    
    checksum = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        checksum += (i + 1) * int(isbn[i])
    
    if isbn[9] == 'X':
        checksum += 10
    elif not isbn[9].isdigit():
        return False
    else:
        checksum += int(isbn[9])
    
    if checksum % 11 == 0:
        return True
    else:
        return False

isbn = input("Enter the ISBN number: ")
if validate_isbn(isbn):
    print("Valid ISBN")
else:
    print("Invalid ISBN")
