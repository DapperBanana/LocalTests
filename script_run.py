
def find_common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

# Taking input from user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = find_common_characters(str1, str2)

if result:
    print(f"The common characters between the two strings are: {', '.join(result)}")
else:
    print("No common characters found.")
