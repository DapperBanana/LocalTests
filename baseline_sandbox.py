
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

lst = [1, 2, 3, 3, 4, 5, 4, 6, 7, 7]
print(remove_duplicates(lst))
