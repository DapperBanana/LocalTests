
def find_largest_element(input_list):
    if len(input_list) == 0:
        return "List is empty"
    
    largest_element = input_list[0]
    for element in input_list:
        if element > largest_element:
            largest_element = element
    
    return largest_element

# Example list
my_list = [10, 25, 5, 30, 15]
largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
