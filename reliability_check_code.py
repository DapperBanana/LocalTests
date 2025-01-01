
def remove_duplicates_preserve_order(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    return output_list

# Test the function
input_list = [1, 2, 3, 3, 4, 2, 5, 6, 7, 7]
output_list = remove_duplicates_preserve_order(input_list)
print(output_list)
