
def find_max_min(dictionary):
    if len(dictionary) == 0:
        return None, None
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return max_value, min_value

# Example dictionary
scores = {"Alice": 85, "Bob": 72, "Charlie": 93, "David": 64}

max_score, min_score = find_max_min(scores)

print(f"Maximum value in the dictionary: {max_score}")
print(f"Minimum value in the dictionary: {min_score}")
