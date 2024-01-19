
def find_common_characters(s1, s2):
    common_characters = set(s1) & set(s2)
    return list(common_characters)

# Example usage
string1 = "hello"
string2 = "world"
common_chars = find_common_characters(string1, string2)
print("Common characters:", common_chars)
