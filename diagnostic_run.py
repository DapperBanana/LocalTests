
def second_largest(lst):
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])
    
    for num in lst[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
            
    return second_largest

# Test the function
lst = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest(lst))
