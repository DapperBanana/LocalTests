
def calculate_square(numbers):
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers

# Test the function
numbers = [1, 2, 3, 4, 5]
squared_numbers = calculate_square(numbers)
print(squared_numbers)
