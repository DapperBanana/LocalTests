
def find_common_characters(str1, str2):
    common_chars = set()
    
    for char in str1:
        if char in str2:
            common_chars.add(char)
    
    return common_chars

str1 = "hello"
str2 = "world"

common_chars = find_common_characters(str1, str2)
print("Common characters:", common_chars)
