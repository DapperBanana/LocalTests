
def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the length of both strings are the same
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings and check if they're equal
    return sorted(str1) == sorted(str2)

# Test the function
string1 = "Listen"
string2 = "Silent"
if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}.")
else:
    print(f"{string1} is not an anagram of {string2}.")
