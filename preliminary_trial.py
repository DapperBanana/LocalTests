
def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the length of both strings are the same
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings and compare them
    return sorted(str1) == sorted(str2)

# Test the function
string1 = "Eleven plus two"
string2 = "Twelve plus one"
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
