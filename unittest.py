
def remove_duplicates(input_list):
    new_list = []
    seen = set()
    for item in input_list:
        if item not in seen:
            new_list.append(item)
            seen.add(item)
    return new_list

# Test the function
input_list = [1, 2, 3, 3, 4, 5, 5, 6]
output_list = remove_duplicates(input_list)
print(output_list)
