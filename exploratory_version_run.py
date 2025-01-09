
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

# Test the program with sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2:", intersection)
