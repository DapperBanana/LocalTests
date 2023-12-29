
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
my_list = [1, 3, 2, 2, 1, 4, 3, 5]
print(remove_duplicates(my_list))  # Output: [1, 3, 2, 4, 5]
