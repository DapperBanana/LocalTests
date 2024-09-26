
def find_common_characters(str1, str2):
    common_chars = set()
    for char in str1:
        if char in str2:
            common_chars.add(char)
    
    return common_chars

# Get input from user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Find common characters
common_chars = find_common_characters(str1, str2)

# Print the result
if len(common_chars) > 0:
    print(f"The common characters between '{str1}' and '{str2}' are: {' '.join(common_chars)}")
else:
    print("There are no common characters between the two strings.")
