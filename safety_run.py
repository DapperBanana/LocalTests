
def find_largest_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Test the function
lst = [1, 5, 3, 9, 2, 7]
largest_element = find_largest_element(lst)
print(f"The largest element in the list is: {largest_element}")
