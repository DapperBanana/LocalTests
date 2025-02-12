
def find_largest_element(input_list):
    largest_element = input_list[0]
    
    for element in input_list[1:]:
        if element > largest_element:
            largest_element = element
            
    return largest_element

# Test the function with a list
test_list = [10, 5, 20, 15, 30]
result = find_largest_element(test_list)
print(f"The largest element in the list is: {result}")
