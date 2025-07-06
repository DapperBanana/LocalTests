
def calculate_square(lst):
    squares = [num**2 for num in lst]
    return squares

# Example list
my_list = [1, 2, 3, 4, 5]

# Calculate squares of each element in the list
result = calculate_square(my_list)

# Print the result
print(result)
