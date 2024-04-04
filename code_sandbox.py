
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
lst = [1, 2, 3, 4, 3, 2, 1, 5]
result = remove_duplicates(lst)
print(result)
