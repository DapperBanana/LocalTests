
def find_largest_element(lst):
    largest_element = lst[0]
    for element in lst:
        if element > largest_element:
            largest_element = element
    return largest_element

# Example usage
my_list = [5, 9, 2, 10, 3]
largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
