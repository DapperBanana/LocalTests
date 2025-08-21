
def find_max_min_values(d):
    if not d:
        return None, None
    
    max_value = max(d.values())
    min_value = min(d.values())
    
    return max_value, min_value

# Test the function
d = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
max_value, min_value = find_max_min_values(d)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
