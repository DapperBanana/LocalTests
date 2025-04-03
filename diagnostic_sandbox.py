
def find_largest_element(input_list):
    largest_element = input_list[0]
    for num in input_list:
        if num > largest_element:
            largest_element = num
    return largest_element

# Test the function
numbers = [10, 5, 20, 15, 30, 25]
largest_num = find_largest_element(numbers)
print(f"The largest element in the list is: {largest_num}")
