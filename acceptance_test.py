
def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    intersection = set1.intersection(set2)
    
    return list(intersection)

# Example
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(find_intersection(list1, list2))
