
def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    if not isbn[:9].isdigit():
        return False
    
    checksum = isbn[9]
    if checksum != 'X' and not checksum.isdigit():
        return False
    
    total = sum(int(isbn[i]) * (i+1) for i in range(9))
    total += 10 if checksum == 'X' else int(checksum)
    
    return total % 11 == 0

# Test the program with some example ISBN numbers
print(is_valid_isbn("3-598-21507-X")) # True
print(is_valid_isbn("3-598-21507-A")) # False
print(is_valid_isbn("3-598-21507-"))  # False
print(is_valid_isbn("123456789X"))    # False
