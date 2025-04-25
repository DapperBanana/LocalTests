
def sum_of_list_elements(lst):
    total_sum = 0
    for num in lst:
        total_sum += num
    return total_sum

# Test the function with a sample list
sample_list = [1, 2, 3, 4, 5]
result = sum_of_list_elements(sample_list)
print(f"The sum of all elements in the list is: {result}")
