
def find_second_largest(arr):
    if len(arr) < 2:
        return "List must have at least 2 elements"
    
    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])
    
    for num in arr[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

# Test the function
arr = [10, 20, 4, 45, 56, 83, 95]
print("Second largest element in the list is:", find_second_largest(arr))
