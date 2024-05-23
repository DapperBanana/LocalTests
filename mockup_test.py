
def find_largest_element(input_list):
    if len(input_list) == 0:
        return "List is empty"
    
    max_element = input_list[0]
    for element in input_list:
        if element > max_element:
            max_element = element
    
    return max_element

# Test the function
my_list = [3, 8, 1, 5, 9]
largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
