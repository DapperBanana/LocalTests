
def find_second_largest(input_list):
    first_largest = float('-inf')
    second_largest = float('-inf')
    
    for num in input_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    
    return second_largest

# Test the function
input_list = [5, 9, 3, 7, 6, 8, 2]
second_largest = find_second_largest(input_list)
print("The second largest element in the list is:", second_largest)
