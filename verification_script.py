
def second_largest_element(arr):
    if len(arr) < 2:
        return "List should have at least 2 elements"
    
    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    return second_largest

# Test the function
arr = [10, 20, 30, 40, 50]
print("Second largest element:", second_largest_element(arr))
