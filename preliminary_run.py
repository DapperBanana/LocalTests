
def find_common_characters(str1, str2):
    common_characters = []
    
    # Convert the input strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find the intersection of the two sets
    common_characters = list(set1.intersection(set2))
    
    return common_characters

# Input strings
str1 = "hello"
str2 = "world"

# Find common characters
common_chars = find_common_characters(str1, str2)

# Print the common characters
print("Common characters:", common_chars)
