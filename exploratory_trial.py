
def find_largest_element(lst):
    if not lst:
        return None
    
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    
    return largest

# Test the function
lst = [3, 7, 2, 10, 5]
largest_element = find_largest_element(lst)
print(f"The largest element in the list is: {largest_element}")
