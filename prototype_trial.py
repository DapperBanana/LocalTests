
def square_elements(lst):
    squared_list = [num ** 2 for num in lst]
    return squared_list

# Test the function
numbers = [1, 2, 3, 4, 5]
result = square_elements(numbers)
print(result)
