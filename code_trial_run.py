
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    count = {}
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            return False
    
    for char in count:
        if count[char] != 0:
            return False
        
    return True

# Test the function
str1 = "listen"
str2 = "silent"
if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")
