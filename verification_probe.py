
def calculate_squares(input_list):
    squared_list = [elem ** 2 for elem in input_list]
    return squared_list

# Example usage
input_list = [1, 2, 3, 4, 5]
squared_list = calculate_squares(input_list)

print("Original List:", input_list)
print("Squared List:", squared_list)
