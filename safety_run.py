
def is_anagram(str1, str2):
    # Remove any spaces and convert both strings to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare both sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Test the function
str1 = "Listen"
str2 = "Silent"
if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
