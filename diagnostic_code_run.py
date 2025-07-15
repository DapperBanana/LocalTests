
def find_common_elements(list1, list2):
    common_elements = [value for value in list1 if value in list2]
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = find_common_elements(list1, list2)
print("Common elements between the two lists are:", common_elements)
