
def common_elements(list1, list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find common elements
common_elements_list = common_elements(list1, list2)

print("Common elements between list1 and list2 are:")
print(common_elements_list)
