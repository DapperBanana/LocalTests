
def find_second_largest(arr):
    if len(arr) < 2:
        return "List must have at least two elements"

    max_num = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max_num:
            second_max = max_num
            max_num = arr[i]
        elif arr[i] > second_max:
            second_max = arr[i]

    return second_max

# Test the function
arr = [3, 6, 8, 1, 4, 9, 10, 2]
print(find_second_largest(arr))  # Output: 9
