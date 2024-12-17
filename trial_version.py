
def find_largest_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Test the function
my_list = [3, 5, 2, 8, 1, 10]
largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
