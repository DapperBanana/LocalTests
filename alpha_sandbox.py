
def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Example
original_list = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9, 9]
unique_list = remove_duplicates(original_list)
print(unique_list)
