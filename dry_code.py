
def common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
            
    return common_chars

# Test the function
str1 = "hello"
str2 = "world"
print(common_characters(str1, str2))  # Output: ['o', 'l']
