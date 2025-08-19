
def second_largest_element(arr):
    if len(arr) < 2:
        return "List should have at least 2 elements"
    
    # Remove duplicates
    unique_elements = list(set(arr))
    
    if len(unique_elements) < 2:
        return "List should have at least 2 unique elements"
    
    unique_elements.sort()
    
    return unique_elements[-2]

# Test the function
arr = [3, 7, 1, 9, 4, 5]
print("Second largest element:", second_largest_element(arr))
