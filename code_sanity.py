
def check_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if length of both strings are same
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and check if they are equal
    return sorted(str1) == sorted(str2)

# Get input from user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if check_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
