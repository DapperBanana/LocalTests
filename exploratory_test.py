
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Create a sorted list
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 7
index = binary_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
