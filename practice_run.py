
def check_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
        
    # Convert the strings to lists and sort them
    str1_list = sorted(list(str1))
    str2_list = sorted(list(str2))
    
    # Check if the sorted lists are equal
    if str1_list == str2_list:
        return True
    else:
        return False

# Test the function
string1 = "listen"
string2 = "silent"
if check_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
