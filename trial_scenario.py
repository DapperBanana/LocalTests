
def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least 2 elements"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "No second largest element found"
    else:
        return second_largest

# Test the function
numbers = [10, 5, 20, 15, 30]
print("Second largest element in the list:", find_second_largest(numbers))
