
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Sample input list
input_list = [1, 2, 3, 1, 4, 2, 5, 6, 1, 3]

# Remove duplicates while preserving order
output_list = remove_duplicates(input_list)

print(output_list)
