
def is_valid_isbn(isbn):
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(10):
        if isbn[i] == 'X':
            digit = 10
        elif isbn[i].isdigit():
            digit = int(isbn[i])
        else:
            return False
        
        total += digit * (10 - i)

    return total % 11 == 0

# Test the function
isbn_number = "0345391802"
if is_valid_isbn(isbn_number):
    print(f"{isbn_number} is a valid ISBN number.")
else:
    print(f"{isbn_number} is not a valid ISBN number.")
