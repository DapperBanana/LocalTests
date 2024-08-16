
def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    return common_elements

# Test the function with two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = find_common_elements(list1, list2)
print("Common elements between list1 and list2 are:", result)
