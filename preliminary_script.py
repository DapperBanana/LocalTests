
def find_max_min(dictionary):
    values = list(dictionary.values())
    
    max_value = max(values)
    min_value = min(values)
    
    return max_value, min_value

# Example dictionary
d = {1: 10, 2: 20, 3: 30, 4: 5, 5: 15}

max_val, min_val = find_max_min(d)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
