
def common_characters(s1, s2):
    common = ""
    for char in s1:
        if char in s2 and char not in common:
            common += char
    return common

# Example
s1 = "hello"
s2 = "world"
print(common_characters(s1, s2))
