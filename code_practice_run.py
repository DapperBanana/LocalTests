
# Function to calculate square of each element in a list
def calculate_square(lst):
    square_lst = [num ** 2 for num in lst]
    return square_lst

# Input list
input_list = [1, 2, 3, 4, 5]

# Calculating square of each element in the list
result = calculate_square(input_list)

# Displaying the result
print("Original List:", input_list)
print("Square of Each Element:", result)
