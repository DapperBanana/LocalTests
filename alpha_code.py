
# function to calculate square of each element in a list
def calculate_squares(lst):
    squares = []
    for num in lst:
        squares.append(num ** 2)
    return squares

# example usage
numbers = [1, 2, 3, 4, 5]
squared_numbers = calculate_squares(numbers)
print(squared_numbers)
