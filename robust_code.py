
def find_common_characters(str1, str2):
    common_chars = []
    
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    
    return common_chars

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

common_chars = find_common_characters(input_str1, input_str2)

if common_chars:
    print(f"The common characters between the two strings are: {', '.join(common_chars)}")
else:
    print("There are no common characters between the two strings.")
