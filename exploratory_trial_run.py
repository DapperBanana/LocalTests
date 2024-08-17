
def is_anagram(str1, str2):
    # Check if the length of the strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in the strings and compare them
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Input strings to check for anagrams
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Check if the strings are anagrams
if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}")
else:
    print(f"{string1} is not an anagram of {string2}")
