
def calculate_squares(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares

# Example usage
my_list = [1, 2, 3, 4, 5]
squared_list = calculate_squares(my_list)
print(squared_list)
