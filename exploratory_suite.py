
def find_common_characters(str1, str2):
    common_chars = set()
    
    for char in str1:
        if char in str2:
            common_chars.add(char)
    
    return common_chars

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find common characters
common_chars = find_common_characters(string1, string2)

# Print the common characters
print("Common characters between the two strings are:", common_chars)
