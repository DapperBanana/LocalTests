
def find_largest_element(input_list):
    max_element = input_list[0]
    
    for element in input_list:
        if element > max_element:
            max_element = element
    
    return max_element

# Example list
numbers = [7, 2, 10, 4, 5, 9]
largest_element = find_largest_element(numbers)
print("The largest element in the list is:", largest_element)
