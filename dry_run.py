
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit():
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False

    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)
    if isbn[-1] == 'X':
        total += 10
    else:
        total += int(isbn[-1]) * 10

    return total % 11 == 0

isbn_input = input("Enter ISBN number: ")
if is_valid_isbn(isbn_input):
    print("Valid ISBN number")
else:
    print("Invalid ISBN number")
