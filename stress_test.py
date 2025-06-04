
def common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

# Example usage
string1 = "hello"
string2 = "world"
print(common_characters(string1, string2))
