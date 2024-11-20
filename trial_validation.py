
def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list

input_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(input_list))
