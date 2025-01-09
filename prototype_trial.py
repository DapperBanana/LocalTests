
def find_common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

# Example usage
str1 = "abcde"
str2 = "cdefg"
common_chars = find_common_characters(str1, str2)
print("Common characters:", common_chars)
