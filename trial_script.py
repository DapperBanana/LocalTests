
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Finding intersection
result = intersection(list1, list2)

# Printing the intersection
print("Intersection of the two lists is:", result)
