
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7]
print(remove_duplicates(my_list))
