
def is_valid_isbn(isbn):
    # Remove any dashes or spaces from the input string
    isbn = isbn.replace("-", "").replace(" ", "")

    # Check if the input string is 10 characters long (without dashes or spaces)
    if len(isbn) != 10:
        return False

    # Calculate the sum of the products of each digit and its position in the ISBN number
    total = 0
    for i in range(10):
        if isbn[i].isdigit():
            total += int(isbn[i]) * (10 - i)
        elif i == 9 and isbn[i].upper() == "X":
            total += 10
        else:
            return False

    # Check if the total sum is divisible by 11
    if total % 11 == 0:
        return True
    else:
        return False

# Test the function with some example ISBN numbers
print(is_valid_isbn("3-598-21507-X"))   # Output: True
print(is_valid_isbn("3-598-21507-A"))   # Output: False
print(is_valid_isbn("013609181"))       # Output: False
print(is_valid_isbn("0-306-40615-2"))   # Output: True
