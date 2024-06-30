
def is_isogram(s):
    s = s.lower()
    for char in s:
        if s.count(char) > 1 and char.isalpha():
            return False
    return True

# Test the function
string1 = "hello"
string2 = "world"
string3 = "python"

print(is_isogram(string1))  # False
print(is_isogram(string2))  # True
print(is_isogram(string3))  # True
