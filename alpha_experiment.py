
def remove_duplicates(input_list):
    output_list = []
    
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    
    return output_list

# Test the function
orig_list = [1, 2, 3, 3, 4, 5, 5, 6]
unique_list = remove_duplicates(orig_list)
print(unique_list)
