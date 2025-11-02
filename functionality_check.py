
def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test the function
lst = [1, 2, 3, 2, 4, 1, 5, 3]
new_lst = remove_duplicates(lst)
print(new_lst)
