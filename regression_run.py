
def find_second_largest(arr):
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] < max1:
            max2 = arr[i]
            
    return max2

# Example
arr = [10, 20, 4, 45, 99]
print("List:", arr)
print("Second largest element:", find_second_largest(arr))
