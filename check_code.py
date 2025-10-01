
def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the length of both strings is the same
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}.")
else:
    print(f"{string1} is not an anagram of {string2}.")
