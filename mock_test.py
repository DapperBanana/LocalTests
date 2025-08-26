
def find_largest_element(lst):
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# Test the function with a sample list
sample_list = [23, 45, 67, 12, 89, 54]
largest_element = find_largest_element(sample_list)
print(f"The largest element in the list is: {largest_element}")
