
def find_common_elements(lst1, lst2):
    common_elements = set(lst1) & set(lst2)
    return list(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = find_common_elements(list1, list2)
print("Common elements between the two lists are:", common_elements)
