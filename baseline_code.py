
def find_common_characters(str1, str2):
    common_characters = set()
    
    for char in str1:
        if char in str2:
            common_characters.add(char)
    
    return common_characters

str1 = "hello"
str2 = "world"

common_characters = find_common_characters(str1, str2)
print("Common characters:", common_characters)
