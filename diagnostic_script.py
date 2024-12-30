
# Function to find the union of two sets
def find_union(set1, set2):
    union_set = set1.union(set2)
    return union_set

# Input sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the union of two sets
union = find_union(set1, set2)
print("Union of set1 and set2:", union)
