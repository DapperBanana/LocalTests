
def find_max_min_values(input_dict):
    if not input_dict:
        return None, None
    
    max_val = max(input_dict.values())
    min_val = min(input_dict.values())
    
    return max_val, min_val

# Example
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 2}
max_val, min_val = find_max_min_values(my_dict)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
