
def is_valid_isbn(isbn):
    # Remove any hyphens from the input string
    isbn = isbn.replace("-", "")
    
    # Check if the input string is a valid ISBN number
    if len(isbn) != 10:
        return False
    
    checksum = 0
    for i in range(10):
        if not isbn[i].isdigit() and (i != 9 or isbn[i] != 'X'):
            return False
        if i < 9:
            checksum += int(isbn[i]) * (10 - i)
        else:
            checksum += 10 if isbn[i] == 'X' else int(isbn[i])
    
    return checksum % 11 == 0

# Test the function with some examples
print(is_valid_isbn("3-598-21508-8")) # True
print(is_valid_isbn("3-598-21508-9")) # False
print(is_valid_isbn("3-598-21507-X")) # True
print(is_valid_isbn("359821507X"))    # True
print(is_valid_isbn("359821507A"))    # False
