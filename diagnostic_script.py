
def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2:", intersection)
