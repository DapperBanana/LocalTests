
def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Input strings
string1 = "Listen"
string2 = "Silent"

# Check if the strings are anagrams
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
