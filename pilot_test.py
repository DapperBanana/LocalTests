
# Function to find the union of two sets
def set_union(set1, set2):
    return set1.union(set2)

# Input sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the union of the two sets
union_set = set_union(set1, set2)

# Print the union set
print("Union of set1 and set2:", union_set)
