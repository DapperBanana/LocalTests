
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 7
result = binary_search(arr, x)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the list.")
