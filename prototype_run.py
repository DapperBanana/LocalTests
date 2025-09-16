
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
original_list = [1, 2, 3, 3, 4, 5, 2, 6, 7, 7]
print("Original list:", original_list)
print("List with duplicates removed:", remove_duplicates(original_list))
