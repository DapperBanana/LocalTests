
def find_max_min(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return max_value, min_value

sample_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 7}

max_val, min_val = find_max_min(sample_dict)

print(f"Maximum value in dictionary: {max_val}")
print(f"Minimum value in dictionary: {min_val}")
