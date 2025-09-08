
def is_anagram(str1, str2):
    # Remove all whitespace and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare if they are equal
    return sorted(str1) == sorted(str2)

# Input strings to check for anagrams
string1 = "Listen"
string2 = "Silent"

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
