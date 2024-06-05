
def common_characters(str1, str2):
    common_chars = set(str1) & set(str2)
    return common_chars

str1 = "hello"
str2 = "world"
common_chars = common_characters(str1, str2)

print("Common characters between '{}' and '{}': {}".format(str1, str2, common_chars))
