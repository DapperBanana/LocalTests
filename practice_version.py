
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 1, 3, 6]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5, 6]
