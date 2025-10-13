
def remove_duplicates(lst):
    seen = set()
    result = []
    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

# Test the function
lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))
