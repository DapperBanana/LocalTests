
def calculate_square(lst):
    squared_list = [x**2 for x in lst]
    return squared_list

# Example list
numbers = [1, 2, 3, 4, 5]

# Calculate the square of each element in the list
squared_numbers = calculate_square(numbers)

print("Original List:", numbers)
print("Squared List:", squared_numbers)
