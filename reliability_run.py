
def is_valid_isbn(isbn):
    # Remove any hyphens or spaces from the input string
    isbn = isbn.replace('-', '').replace(' ', '')
    
    # Check if the input string is a 10-digit ISBN number
    if len(isbn) != 10:
        return False
        
    # Compute the sum of digits weighted by their position
    total = 0
    for i in range(10):
        if isbn[i].isdigit():
            total += int(isbn[i]) * (10 - i)
        elif i == 9 and isbn[i].lower() == 'x':
            total += 10
        else:
            return False
    
    # Verify if the total is divisible by 11
    if total % 11 == 0:
        return True
    else:
        return False

# Test the program
isbn = input("Enter an ISBN number: ")
if is_valid_isbn(isbn):
    print(f"{isbn} is a valid ISBN number.")
else:
    print(f"{isbn} is not a valid ISBN number.")
