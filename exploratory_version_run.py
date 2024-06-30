
def find_second_largest(arr):
    if len(arr) < 2:
        return "List must contain at least 2 elements"
    
    largest = -float("inf")
    second_largest = -float("inf")
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

# Test the function
arr = [10, 20, 30, 40, 50]
print(find_second_largest(arr))  # Output: 40

arr = [50, 30, 10, 40, 45]
print(find_second_largest(arr))  # Output: 45

arr = [1, 1, 1]
print(find_second_largest(arr))  # Output: "List must contain at least 2 elements"
