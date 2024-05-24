
def find_second_largest(arr):
    if len(arr) < 2:
        return "List must have at least two elements"
    
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
arr = [10, 20, 4, 45, 99]
print("Second largest element in the list is:", find_second_largest(arr))
