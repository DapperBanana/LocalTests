// Python code to find common characters between two strings
def find_common_characters(str1, str2):
    # Convert strings to sets to find common characters
    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)
    # Return common characters as a string
    return ''.join(sorted(common_chars))

# Example usage
string1 = "apple"
string2 = "pineapple"

print(find_common_characters(string1, string2))