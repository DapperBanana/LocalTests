
def find_intersection(list1, list2):
    intersection = [value for value in list1 if value in list2]
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2 is:", intersection)
