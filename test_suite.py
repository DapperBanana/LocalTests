
def remove_duplicates(input_list):
    output_list = []
    seen = set()
    
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
            
    return output_list

# Sample Input
input_list = [1, 2, 3, 4, 2, 3, 5, 6, 4]

# Remove duplicates while preserving order
result = remove_duplicates(input_list)

print(result)
