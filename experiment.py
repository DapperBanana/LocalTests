
def common_characters(str1, str2):
    common_chars = set(str1) & set(str2)
    return common_chars

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

common_chars = common_characters(string1, string2)

if len(common_chars) == 0:
    print("No common characters found.")
else:
    print("Common characters: ", common_chars)
