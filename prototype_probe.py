
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have same length
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Input strings
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if is_anagram(input_str1, input_str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
