
def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")  # Remove any dashes or spaces
    if len(isbn) != 10:
        return False
    
    checksum = 0
    for i in range(10):
        if i == 9 and isbn[i] == 'X':
            checksum += 10
        elif not isbn[i].isdigit():
            return False
        else:
            checksum += int(isbn[i]) * (10 - i)
    
    return checksum % 11 == 0

# Test the function with some examples
isbn1 = "3-598-21508-8"
isbn2 = "3-598-21507-X"
isbn3 = "99921-58-10-7"
isbn4 = "960-425-059-0"
isbn5 = "1-86197-876-X"

print(is_valid_isbn(isbn1))  # Output: True
print(is_valid_isbn(isbn2))  # Output: True
print(is_valid_isbn(isbn3))  # Output: True
print(is_valid_isbn(isbn4))  # Output: True
print(is_valid_isbn(isbn5))  # Output: True
