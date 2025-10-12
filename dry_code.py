
def remove_duplicates(input_list):
    output_list = []
    seen = set()
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    
    return output_list

input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print(output_list)
