
def square_elements(input_list):
    squared_list = [elem**2 for elem in input_list]
    return squared_list

input_list = [1, 2, 3, 4, 5]
result_list = square_elements(input_list)

print("Original List:", input_list)
print("Squared List:", result_list)
