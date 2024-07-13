
def max_min_values_in_dict(d):
    max_value = max(d.values())
    min_value = min(d.values())
    return max_value, min_value

# Example
data = {'a': 100, 'b': 200, 'c': 50, 'd': 300}
max_val, min_val = max_min_values_in_dict(data)

print("Maximum value in the dictionary:", max_val)
print("Minimum value in the dictionary:", min_val)
