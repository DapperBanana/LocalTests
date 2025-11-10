
def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list

# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5, 4]
output_list = remove_duplicates(input_list)
print(output_list)
