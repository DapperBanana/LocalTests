
def remove_duplicates(input_list):
    result = []
    seen = set()

    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

input_list = [1, 2, 3, 3, 4, 2, 5, 6, 7, 7]
output_list = remove_duplicates(input_list)

print(output_list)
