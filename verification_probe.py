
def find_largest_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example list
my_list = [10, 20, 5, 45, 30]

largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
