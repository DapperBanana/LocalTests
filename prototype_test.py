
def second_largest_element(lst):
    largest = None
    second_largest = None
    
    for num in lst:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
            
    return second_largest

# Test the function
lst = [10, 20, 30, 40, 50]
print("List:", lst)
print("Second largest element:", second_largest_element(lst))
