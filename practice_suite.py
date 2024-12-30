
def find_max_min(dict):
    values = list(dict.values())
    return max(values), min(values)

# Test the function
data = {'a': 12, 'b': 25, 'c': 10, 'd': 30}
max_value, min_value = find_max_min(data)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
