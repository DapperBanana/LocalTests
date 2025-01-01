
def is_anagram(str1, str2):
    str1 = str1.lower().replace(' ', '')  # Convert both strings to lowercase and remove spaces
    str2 = str2.lower().replace(' ', '')

    if len(str1) != len(str2):  # If the lengths of the two strings are not equal, they cannot be anagrams
        return False

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Test the function
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
