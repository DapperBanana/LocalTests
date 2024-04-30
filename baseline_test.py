
def square_elements(input_list):
    square_list = [num**2 for num in input_list]
    return square_list

# Example
my_list = [2, 4, 6, 8, 10]
result = square_elements(my_list)
print(result)
