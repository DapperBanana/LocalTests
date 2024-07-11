
def find_max_min(dictionary):
    values = list(dictionary.values())
    max_value = max(values)
    min_value = min(values)
    
    return max_value, min_value

# Example
ages = {'Alice': 25, 'Bob': 30, 'Charlie': 20, 'Diana': 35}
max_age, min_age = find_max_min(ages)

print(f"Maximum age: {max_age}")
print(f"Minimum age: {min_age}")
