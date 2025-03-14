
def remove_duplicates(input_list):
    seen = set()
    output_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    
    return output_list

input_list = [1, 2, 3, 2, 4, 1, 5]
output_list = remove_duplicates(input_list)

print(output_list)
