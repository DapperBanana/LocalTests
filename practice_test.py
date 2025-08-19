
def find_common_characters(str1, str2):
    common_characters = []
    for char in str1:
        if char in str2 and char not in common_characters:
            common_characters.append(char)
            
    return common_characters

string1 = "hello"
string2 = "world"
common_chars = find_common_characters(string1, string2)

print("Common characters between '{}' and '{}': {}".format(string1, string2, common_chars))
