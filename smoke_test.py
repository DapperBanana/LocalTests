
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove dashes from the input string
    if len(isbn) != 10:  # ISBN must be 10 characters long
        return False

    if not isbn[:-1].isdigit():  # Check if first 9 characters are digits
        return False
    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):  # Check if last character is digit or 'X'
        return False

    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)
    if isbn[9] == 'X':  # Check if last character is 'X'
        total += 10
    else:
        total += int(isbn[9])

    return total % 11 == 0


# Test the program
sample_isbn = '3-598-21508-8'
if is_valid_isbn(sample_isbn):
    print(f"{sample_isbn} is a valid ISBN number.")
else:
    print(f"{sample_isbn} is not a valid ISBN number.")
