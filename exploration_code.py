
def find_common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

# Take input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Find the common characters
common_chars = find_common_characters(str1, str2)

if len(common_chars) > 0:
    print("Common characters between the two strings are:", common_chars)
else:
    print("There are no common characters between the two strings.")
