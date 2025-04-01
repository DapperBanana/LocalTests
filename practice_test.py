
def calculate_square(lst):
    square_lst = [num**2 for num in lst]
    return square_lst

# Test the function
my_list = [1, 2, 3, 4, 5]
result = calculate_square(my_list)
print(result)
