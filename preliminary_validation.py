
def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True

# Test the function
string1 = "listen"
string2 = "silent"
if check_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
