
def calculate_square(lst):
    squared_list = [num**2 for num in lst]
    return squared_list

# Example list
my_list = [1, 2, 3, 4, 5]

# Calculate the square of each element in the list
result = calculate_square(my_list)

print(result)
