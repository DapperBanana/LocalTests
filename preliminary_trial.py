
def check_anagram(str1, str2):
    # Check if the lengths of the two strings are the same
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if check_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}.")
else:
    print(f"{string1} is not an anagram of {string2}.")
