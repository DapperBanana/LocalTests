
def calculate_square(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

numbers = [1, 2, 3, 4, 5]
squared_numbers = calculate_square(numbers)

print("Original List:", numbers)
print("Squared List:", squared_numbers)
