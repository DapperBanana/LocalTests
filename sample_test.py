
def find_max_min_values(input_dict):
    values = list(input_dict.values())
    
    max_val = max(values)
    min_val = min(values)
    
    return max_val, min_val

# Test the function
my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
max_val, min_val = find_max_min_values(my_dict)

print(f"Maximum value in the dictionary: {max_val}")
print(f"Minimum value in the dictionary: {min_val}")
