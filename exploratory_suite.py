
def find_largest_element(lst):
    if not lst:
        return None
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example list
my_list = [5, 10, 3, 8, 15]

largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
