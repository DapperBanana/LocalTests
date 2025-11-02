
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Input lists
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

# Find intersection
intersection_list = intersection(lst1, lst2)

# Output
print("List 1:", lst1)
print("List 2:", lst2)
print("Intersection List:", intersection_list)
