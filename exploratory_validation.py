
def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    return common_elements

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find the common elements
common_elements = find_common_elements(list1, list2)

# Print the common elements
print("Common Elements:", common_elements)
