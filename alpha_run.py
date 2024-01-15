
def find_maximum_minimum(dictionary):
    values = list(dictionary.values())
    max_value = max(values)
    min_value = min(values)
    return max_value, min_value

# Example usage:
my_dict = {"a": 10, "b": 5, "c": 15, "d": 20}
max_value, min_value = find_maximum_minimum(my_dict)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
