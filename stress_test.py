
def check_anagram(str1, str2):
    # Removing whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Create a dictionary to store the frequency of each character in str1
    char_freq = {}
    for char in str1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Check if the frequency of each character in str2 matches with the frequency in char_freq
    for char in str2:
        if char in char_freq:
            char_freq[char] -= 1
        else:
            return False
    
    for freq in char_freq.values():
        if freq != 0:
            return False
    
    return True

# Test the function
str1 = "listen"
str2 = "silent"
if check_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
