
def find_common_characters(str1, str2):
    common_characters = []
    for char in str1:
        if char in str2 and char not in common_characters:
            common_characters.append(char)
    
    return common_characters

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common_chars = find_common_characters(string1, string2)

if common_chars:
    print("Common characters between the two strings are:", ', '.join(common_chars))
else:
    print("No common characters between the two strings.")
