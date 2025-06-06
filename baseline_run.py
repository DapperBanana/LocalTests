
def intersection(list1, list2):
    return list(set(list1) & set(list2))

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = intersection(list1, list2)
print("Intersection of the two lists:", result)
