
def square_elements(lst):
    squared_list = [x**2 for x in lst]
    return squared_list

# Test the function with a sample list
sample_list = [1, 2, 3, 4, 5]
result = square_elements(sample_list)
print(result)
