
def common_characters(s1, s2):
    common_chars = set()
    
    for char in s1:
        if char in s2:
            common_chars.add(char)
    
    return common_chars

# Input strings
string1 = "hello"
string2 = "world"

common_chars = common_characters(string1, string2)

print("Common characters:", common_chars)
