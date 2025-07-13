
def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = find_common_elements(list1, list2)
print("Common elements between list1 and list2 are:", common_elements)
