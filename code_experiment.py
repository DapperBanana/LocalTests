
def find_intersection(list1, list2):
    intersect = [value for value in list1 if value in list2]
    return intersect

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = find_intersection(list1, list2)
print("Intersection of List 1 and List 2:", intersection)
