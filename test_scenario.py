
def square_elements(input_list):
    new_list = [elem**2 for elem in input_list]
    return new_list

input_list = [1, 2, 3, 4, 5]
result_list = square_elements(input_list)
print(result_list)
