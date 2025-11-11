
def find_intersection(list1, list2):
    intersection = [value for value in list1 if value in list2]
    return intersection

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find intersection
intersection = find_intersection(list1, list2)

# Print the intersection
print("Intersection of list1 and list2: ", intersection)
