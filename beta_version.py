
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

# Test the binary search function
arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
target = 18
result = binary_search(arr, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print("Target element not found")
