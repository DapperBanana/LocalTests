
def square_elements(input_list):
    squared_list = []
    for num in input_list:
        squared_list.append(num**2)
    return squared_list

# Main program
input_list = [1, 2, 3, 4, 5]
result = square_elements(input_list)
print("Original list:", input_list)
print("Squared list:", result)
