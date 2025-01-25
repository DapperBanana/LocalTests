
def find_largest_element(input_list):
    largest_element = float('-inf')
    for num in input_list:
        if num > largest_element:
            largest_element = num
    return largest_element

# Test the function
input_list = [3, 8, 1, 5, 10, 2]
largest_element = find_largest_element(input_list)
print(f"The largest element in the list is: {largest_element}")
