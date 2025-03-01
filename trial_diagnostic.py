
def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test the function
original_list = [1, 2, 3, 2, 4, 1, 5, 6, 3]
unique_list = remove_duplicates(original_list)
print(unique_list)
