
def remove_duplicates(lst):
    result = []
    seen = set()
    
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result

# Test the function
lst = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", lst)
print("List with duplicates removed:", remove_duplicates(lst))
