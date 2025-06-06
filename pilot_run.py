
def find_largest_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example list
my_list = [10, 30, 20, 50, 40, 70, 60]

largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
