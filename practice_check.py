
def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Sort both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal (anagram)
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


# Test the function
string1 = "listen"
string2 = "silent"

if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}")
else:
    print(f"{string1} is not an anagram of {string2}")
