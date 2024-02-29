
def find_intersection(list1, list2):
    intersection = set(list1).intersection(list2)
    return list(intersection)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2:", intersection)
