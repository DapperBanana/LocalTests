
def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test the function
original_list = [1, 2, 3, 3, 4, 5, 5, 6]
updated_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with duplicates removed while preserving order:", updated_list)
