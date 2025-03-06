
def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
list_of_numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(list_of_numbers)
print("The sum of all elements in the list is:", result)
