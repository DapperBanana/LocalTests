
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
test_list = [1, 2, 3, 4, 5]
result = sum_of_list(test_list)
print(f"The sum of all elements in the list is: {result}")
