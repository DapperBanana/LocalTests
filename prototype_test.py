
def common_characters(str1, str2):
    common_chars = set(str1) & set(str2)
    return common_chars

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = common_characters(str1, str2)

if common_chars:
    print("Common characters: ", ', '.join(common_chars))
else:
    print("No common characters found.")
