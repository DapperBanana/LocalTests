
def remove_duplicates(input_list):
    output_list = []
    seen_items = set()

    for item in input_list:
        if item not in seen_items:
            output_list.append(item)
            seen_items.add(item)

    return output_list

input_list = [1, 2, 3, 3, 4, 5, 6, 6, 7]
output_list = remove_duplicates(input_list)

print(output_list)
