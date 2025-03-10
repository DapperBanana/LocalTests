
def find_largest_element(lst):
    if len(lst) == 0:
        return None
    
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
            
    return largest

# Test the function
lst = [10, 20, 4, 45, 99]
largest_element = find_largest_element(lst)
print("The largest element in the list is:", largest_element)
