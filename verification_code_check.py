
def find_intersection(list1, list2):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of two sets
    intersection = set1.intersection(set2)
    
    # Convert the intersection set back to a list
    intersection_list = list(intersection)
    
    return intersection_list

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print(result)
