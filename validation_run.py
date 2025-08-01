
def find_second_largest(arr):
    arr = sorted(arr, reverse=True)
    return arr[1]

# Test the function
arr = [10, 5, 20, 8, 15]
print("Original list:", arr)
print("Second largest element:", find_second_largest(arr))
