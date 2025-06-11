
def find_largest_element(arr):
    if len(arr) == 0:
        return None

    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element

    return max_element

# Test the function
arr = [5, 2, 9, 15, 3, 7]
largest_element = find_largest_element(arr)
print(f"The largest element in the list is: {largest_element}")
