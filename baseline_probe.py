
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = find_common_elements(list1, list2)
print("Common elements between list1 and list2:", common_elements)
