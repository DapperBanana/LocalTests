
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
original_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
new_list = remove_duplicates(original_list)
print(new_list)
