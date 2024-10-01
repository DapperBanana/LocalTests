
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
original_list = [1, 2, 3, 2, 4, 5, 1, 6]
result_list = remove_duplicates_preserve_order(original_list)
print(result_list)
