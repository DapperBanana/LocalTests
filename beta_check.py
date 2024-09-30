
def find_sum_of_list_elements(input_list):
    total = 0
    for element in input_list:
        total += element
    return total

# Test the function with an example list
example_list = [1, 2, 3, 4, 5]
print("Sum of elements in the list:", find_sum_of_list_elements(example_list))
