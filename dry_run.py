
def is_anagram(str1, str2):
    # Removing spaces and converting characters to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Checking if the length of both strings is the same
    if len(str1) != len(str2):
        return False

    # Sorting both strings and comparing them
    return sorted(str1) == sorted(str2)

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Checking if the strings are anagrams
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
