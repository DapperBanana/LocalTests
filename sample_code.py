
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 7, 9]
print(remove_duplicates(input_list))
