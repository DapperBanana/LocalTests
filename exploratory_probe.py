
def find_second_largest(lst):
    # Initialize the variables
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Iterate over the list
    for num in lst:
        # If the current number is larger than the largest, update both largest and second_largest
        if num > largest:
            second_largest = largest
            largest = num
        # If the current number is smaller than the largest but larger than the second_largest, update only second_largest
        elif num > second_largest and num != largest:
            second_largest = num
    
    # Print the second largest element
    if second_largest == float('-inf'):
        print("No second largest element found.")
    else:
        print("The second largest element is:", second_largest)

# Test the function
list1 = [9, 3, 2, 7, 5, 1, 4, 6, 8]
find_second_largest(list1)  # Output: The second largest element is: 8

list2 = [1, 1, 1, 1, 1]
find_second_largest(list2)  # Output: No second largest element found.
