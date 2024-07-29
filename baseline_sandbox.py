
def find_common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = find_common_characters(str1, str2)

if len(common_chars) == 0:
    print("No common characters found.")
else:
    print("Common characters:", ", ".join(common_chars))
