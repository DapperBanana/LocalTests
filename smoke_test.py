
def find_largest_element(lst):
    largest_element = lst[0]
    
    for element in lst:
        if element > largest_element:
            largest_element = element
    
    return largest_element

# Test the function
lst = [10, 20, 5, 15, 30]
largest_element = find_largest_element(lst)
print(f"The largest element in the list is: {largest_element}")
