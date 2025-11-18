
def is_isogram(s):
    s = s.lower()
    for char in s:
        if s.count(char) > 1:
            return False
    return True

# Test the function
print(is_isogram("hello")) # False
print(is_isogram("world")) # True
print(is_isogram("Python")) # True
print(is_isogram("programming")) # False
