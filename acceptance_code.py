
def find_second_largest(arr):
    first_largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    
    return second_largest

# Test the function
arr = [5, 10, 3, 8, 15]
second_largest = find_second_largest(arr)
print("Second largest element in the list is:", second_largest)
