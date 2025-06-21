
def square_elements(lst):
    squared_list = [num ** 2 for num in lst]
    return squared_list

# Test the function
lst = [1, 2, 3, 4, 5]
squared_elements = square_elements(lst)
print(squared_elements)
