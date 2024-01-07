
def common_characters(str1, str2):
    common = set(str1) & set(str2)  # Find the common characters
    return ''.join(sorted(common))  # Sort and join the characters

# Test the function
string1 = 'hello'
string2 = 'world'
print(common_characters(string1, string2))  # Output: lo

string3 = 'abc'
string4 = 'def'
print(common_characters(string3, string4))  # Output: 

string5 = 'apple'
string6 = 'banana'
print(common_characters(string5, string6))  # Output: a

string7 = 'python'
string8 = 'program'
print(common_characters(string7, string8))  # Output: gopr
