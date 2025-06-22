
def remove_duplicates(input_list):
    output_list = []
    seen = set()
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    return output_list

input_list = [1, 2, 3, 1, 2, 4, 5, 6, 7, 5]
output_list = remove_duplicates(input_list)
print(output_list)
