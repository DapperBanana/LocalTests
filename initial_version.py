
def square_elements(arr):
    squared_list = [num ** 2 for num in arr]
    return squared_list

# Test the function
input_list = [1, 2, 3, 4, 5]
squared_list = square_elements(input_list)
print(f"The squared list is: {squared_list}")
