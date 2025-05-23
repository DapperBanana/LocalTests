
def calculate_square(input_list):
    squared_list = [num**2 for num in input_list]
    return squared_list

# Test the function
input_list = [2, 4, 6, 8]
result = calculate_square(input_list)
print(result)
