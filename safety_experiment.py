
def find_largest_element(input_list):
    max_element = input_list[0]
    
    for element in input_list:
        if element > max_element:
            max_element = element
            
    return max_element

# Test the function
input_list = [10, 5, 20, 15, 8]
largest_element = find_largest_element(input_list)
print("The largest element in the list is:", largest_element)
