
def remove_duplicates(input_list):
    seen = set()
    output_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    
    return output_list

# Example list with duplicates
my_list = [1, 2, 3, 1, 4, 3, 5, 6, 2]

# Remove duplicates while preserving order
result = remove_duplicates(my_list)

print(result)
