
def second_largest_element(arr):
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max2 = num
    
    return max2

# Test the function
arr = [10, 20, 4, 45, 99]
print("Second largest element in the list is:", second_largest_element(arr))
