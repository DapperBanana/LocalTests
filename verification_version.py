
def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # remove hyphens from the input string

    if len(isbn) != 10:  # check if the length of the ISBN is 10
        return False

    total = 0
    for i in range(10):
        if isbn[i].isdigit():
            total += int(isbn[i]) * (10 - i)
        elif i == 9 and isbn[i] == 'X':  # handle X as the last character
            total += 10
        else:
            return False

    return total % 11 == 0


# Test the function with some examples
print(is_valid_isbn('3-598-21507-X'))  # True
print(is_valid_isbn('3-598-21508-9'))  # False
print(is_valid_isbn('3-598-21507-1'))  # False
