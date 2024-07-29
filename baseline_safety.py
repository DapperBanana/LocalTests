
def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
input_list = [1, 2, 2, 3, 4, 1, 5, 6, 6]
output_list = remove_duplicates(input_list)
print(output_list)
