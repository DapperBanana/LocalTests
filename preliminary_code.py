
def find_max_min(dictionary):
    values = list(dictionary.values())
    max_value = max(values)
    min_value = min(values)
    return max_value, min_value

# Example dictionary
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_val, min_val = find_max_min(my_dict)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
