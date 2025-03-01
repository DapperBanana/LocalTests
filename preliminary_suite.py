
def check_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in each string
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    # Compare the sorted strings
    if str1_sorted == str2_sorted:
        return True
    else:
        return False

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if check_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
