
def intersection(list1, list2):
    # Using set intersection to find common elements
    intersection_set = set(list1) & set(list2)
    
    return list(intersection_set)

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)
