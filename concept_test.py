
def is_anagram(string1, string2):
    # Remove spaces and convert to lowercase
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    
    # Check if the lengths of the strings are the same
    if len(string1) != len(string2):
        return False

    # Sort the characters in both strings and compare if they are equal
    return sorted(string1) == sorted(string2)

# Test the function
string1 = "listen"
string2 = "silent"
if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}")
else:
    print(f"{string1} is not an anagram of {string2}")
