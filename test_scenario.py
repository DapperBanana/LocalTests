
def square_elements(input_list):
    squared_list = [element ** 2 for element in input_list]
    return squared_list

# Test the program with an example list
input_list = [1, 2, 3, 4, 5]
result = square_elements(input_list)
print("Original list:", input_list)
print("Squared list:", result)
