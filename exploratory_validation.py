
def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print(f"{string1} is an anagram of {string2}.")
else:
    print(f"{string1} is not an anagram of {string2}.")
