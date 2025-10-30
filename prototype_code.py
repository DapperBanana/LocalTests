
def find_common_characters(str1, str2):
    common_characters = []
    
    for char in str1:
        if char in str2 and char not in common_characters:
            common_characters.append(char)
    
    return common_characters

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_chars = find_common_characters(str1, str2)

if common_chars:
    print(f"Common characters between '{str1}' and '{str2}':")
    for char in common_chars:
        print(char)
else:
    print("No common characters found.")
