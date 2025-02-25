
def find_max_min(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    
    return max_value, min_value

# Example dictionary
d = {"a": 10, "b": 5, "c": 15, "d": 3}

max_val, min_val = find_max_min(d)

print(f"Max value: {max_val}")
print(f"Min value: {min_val}")
