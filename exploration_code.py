
def is_anagram(str1, str2):
    # remove whitespaces and convert strings to lowercase
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    # check if the length of both strings are same
    if len(str1) != len(str2):
        return False
    
    # sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # compare both sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# input strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if is_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
