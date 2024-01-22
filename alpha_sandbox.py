
def find_largest_element(lst):
    max_element = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    return max_element

# Example usage:
my_list = [2, 5, 8, 1, 3, 9]
largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
