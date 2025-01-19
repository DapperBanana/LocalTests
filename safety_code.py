
def square_elements(lst):
    squared_list = [num**2 for num in lst]
    return squared_list

# Test the function
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)

print("Original list:", numbers)
print("List with squared elements:", squared_numbers)
