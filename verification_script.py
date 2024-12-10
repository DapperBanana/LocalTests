
def find_max_min_values(input_dict):
    if not input_dict:
        return None, None
    
    max_value = max(input_dict.values())
    min_value = min(input_dict.values())
    
    return max_value, min_value

# Test the function with a sample dictionary
sample_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
max_val, min_val = find_max_min_values(sample_dict)

print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
