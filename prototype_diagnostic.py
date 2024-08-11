
def square_elements(input_list):
    squared_list = [x**2 for x in input_list]
    return squared_list

# Test the function
input_list = [1, 2, 3, 4, 5]
output_list = square_elements(input_list)
print(output_list)
