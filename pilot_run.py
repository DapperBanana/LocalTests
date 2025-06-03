
def check_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the length of the strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings and compare
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Input strings
string1 = "listen"
string2 = "silent"

# Check if the strings are anagrams
if check_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}")
else:
    print(f"{string1} is not an anagram of {string2}")
